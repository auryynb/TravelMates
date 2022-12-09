from datetime import *

from tours.models import *


def splitBudget(days):
    per = 0.15
    res = 0
    for i in range(days):
        res += per
        per -= 0.02
    each = res / days
    return res, each


def closestSum(arr, k):
    # create a dp dictionary to grow. key is closest sum so far, value is the list of numbers that add up to key
    dp_dict = {0: []}
    for num in arr:
        dict_copy = dict(dp_dict)
        # grow or update the dp dict with the closest sum so far
        for sum in dp_dict:
            if sum + num < k:
                dict_copy[sum + num] = dp_dict[sum] + [num]
        dp_dict = dict_copy
    # traceback - find the item in dp dict that is closest to k
    result = (k, [])
    for sum, number_list in dp_dict.items():
        distance = abs(k - sum)
        if distance < result[0]:
            result = (distance, number_list)
    return result[1]


def destinationBudgetMapping(budget_destinasi, city_to):
    destination = Destinasi.objects.filter(city_id=city_to)
    sample_list = list(destination.values_list('price_max', flat=True))
    target_value = budget_destinasi
    sum_dest = closestSum(sample_list, target_value)
    # print(sum_dest)
    destination_list = list(destination)
    destinasi = []
    for price in sum_dest:
        res = list(filter(lambda x: x.price_max == price, destination_list))
        destinasi.append(res[0])
        destination_list.remove(res[0])
    if len(destinasi) > 1:
        return destinasi
    else:
        return False


def rencanaTransportasi(r, budget_transportasi, city_from, city_to):
    budget = 0.5 * budget_transportasi
    transportasi_pergi = Transportasi.objects.order_by('-price_per_person').filter(city_from=city_from, city_to=city_to, price_per_person__lte=budget).first()
    transportasi_pulang = Transportasi.objects.order_by('-price_per_person').filter(city_from=city_to, city_to=city_from, price_per_person__lte=budget).first()
    if transportasi_pulang and transportasi_pergi:
        cost = transportasi_pergi.price_per_person + transportasi_pulang.price_per_person
        current_time = datetime.strptime(transportasi_pergi.arrive_time.strftime("%H:%M:%S"), '%H:%M:%S')
        return_time = datetime.strptime(transportasi_pulang.depart_time.strftime("%H:%M:%S"), '%H:%M:%S')
        r.transportasi_pergi = transportasi_pergi
        r.transportasi_pulang = transportasi_pulang
        r.save()
        return current_time, return_time, cost
    else:
        return False


def rencanaDestinasi(r, destinasi, plan_days, current_time, return_time):
    print(destinasi)
    rencana = r
    start_time = current_time
    end_time = start_time + timedelta(hours=4)
    if start_time.hour < 8:
        start_time = datetime(1900, 1, 1, 8, 0)
    days = 1
    cost = 0
    while days <= plan_days:
        while start_time.hour <= 19:
            end_time = start_time + timedelta(hours=4)
            res = list(
                filter(lambda x: x.opening_hours < start_time.time() and x.closing_hours > end_time.time(), destinasi))
            if res:
                des = res[0]
                d = RencanaWisataDestinasi(destinasi=des, rencana_wisata=r, day=days, start_time=start_time, end_time=end_time)
                destinasi.remove(des)
                d.save()
                start_time = end_time
                cost += des.price_max
                if end_time.hour+4 >= return_time.hour and days == rencana.days:
                    break
                else:
                    continue
            else:
                break
        days += 1
        start_time = datetime(1900, 1, 1, 8, 0)
        end_time = datetime(1900, 1, 1, 12, 0)
    return cost


def rencanaAkomodasi(r, budget, city_to):
    akomodasi = Akomodasi.objects.order_by('-price_per_night').filter(price_per_night__lte=budget, city=city_to).first()
    if (akomodasi):
        print(akomodasi)
        r.akomodasi = akomodasi
        cost = akomodasi.price_per_night
        r.save()
        return True, cost
    else:
        return False


def rencanaWisata(budget, days, city_from, city_to):
    split = splitBudget(days)
    total_cost = 0
    r = RencanaWisata(title='test', budget=budget, days=days, city_start_id=city_from, city_dest_id=city_to)
    # print('called once')
    r.save()
    tot_akomodasi = split[0] * budget
    budget_akomodasi = split[1] * budget
    if city_from == city_to:
        budget_destinasi = budget - tot_akomodasi
        akom = rencanaAkomodasi(r, budget_akomodasi, city_to)
        destinasi = destinationBudgetMapping(budget_destinasi, city_to)
        # print(destinasi)
        if akom is not False and destinasi is not False:
            start_time = datetime(1900, 1, 1, 8, 0)
            end_time = datetime(1900, 1, 1, 21, 0)
            dest = rencanaDestinasi(r, destinasi, days, start_time, end_time)
            total_cost = (akom[1] * days) + dest
            r.real_cost = total_cost
            r.save()
            print('Berhasil direncanakan')
        else:
            print('Wisata Gagal')
            r.delete()
        return r
    else:
        # print('city not same')
        # print('akomodasi', budget_akomodasi)
        budget_transportasi = (0.6 * (1 - split[0])) * budget
        budget_destinasi = (0.4 * (1 - split[0])) * budget
        # print('transport', budget_transportasi)
        # print('destinasi', budget_destinasi)
        # print(budget_destinasi + tot_akomodasi+budget_transportasi)
        akom = rencanaAkomodasi(r, budget_akomodasi, city_to)
        rt = rencanaTransportasi(r, budget_transportasi, city_from, city_to)
        destinasi = destinationBudgetMapping(budget_destinasi, city_to)
        if akom is not False and rt is not False and destinasi is not False :
            dest = rencanaDestinasi(r, destinasi, days, rt[0], rt[1])
            # print(dest)
            total_cost = (akom[1]*days) + dest + rt[2]
            r.real_cost = total_cost
            r.save()
            print('Rencana Sukses, total cost = ', total_cost)
        else:
            print('Rencana Gagal')
            r.delete()
        return r

#
# budget = 1000000
# city_from = City.objects.filter(city='Malang').get()
# city_to = City.objects.filter(city='Yogyakarta').get()
# days = 2
# rencanaWisata(budget, days, city_from, city_to)
