--
-- PostgreSQL database dump
--

-- Dumped from database version 15.0
-- Dumped by pg_dump version 15.0

-- Started on 2022-11-22 09:20:09

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3546 (class 0 OID 16766)
-- Dependencies: 221
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3542 (class 0 OID 16752)
-- Dependencies: 217
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_content_type VALUES (1, 'tours', 'city');
INSERT INTO public.django_content_type VALUES (2, 'tours', 'destination');
INSERT INTO public.django_content_type VALUES (3, 'admin', 'logentry');
INSERT INTO public.django_content_type VALUES (4, 'auth', 'permission');
INSERT INTO public.django_content_type VALUES (5, 'auth', 'group');
INSERT INTO public.django_content_type VALUES (6, 'auth', 'user');
INSERT INTO public.django_content_type VALUES (7, 'contenttypes', 'contenttype');
INSERT INTO public.django_content_type VALUES (8, 'sessions', 'session');
INSERT INTO public.django_content_type VALUES (9, 'tours', 'transportation');
INSERT INTO public.django_content_type VALUES (10, 'tours', 'accomodation');
INSERT INTO public.django_content_type VALUES (11, 'tours', 'rencanawisata');
INSERT INTO public.django_content_type VALUES (12, 'tours', 'imagealbum');
INSERT INTO public.django_content_type VALUES (13, 'tours', 'image');


--
-- TOC entry 3544 (class 0 OID 16760)
-- Dependencies: 219
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_permission VALUES (1, 'Can add city', 1, 'add_city');
INSERT INTO public.auth_permission VALUES (2, 'Can change city', 1, 'change_city');
INSERT INTO public.auth_permission VALUES (3, 'Can delete city', 1, 'delete_city');
INSERT INTO public.auth_permission VALUES (4, 'Can view city', 1, 'view_city');
INSERT INTO public.auth_permission VALUES (5, 'Can add destination', 2, 'add_destination');
INSERT INTO public.auth_permission VALUES (6, 'Can change destination', 2, 'change_destination');
INSERT INTO public.auth_permission VALUES (7, 'Can delete destination', 2, 'delete_destination');
INSERT INTO public.auth_permission VALUES (8, 'Can view destination', 2, 'view_destination');
INSERT INTO public.auth_permission VALUES (9, 'Can add log entry', 3, 'add_logentry');
INSERT INTO public.auth_permission VALUES (10, 'Can change log entry', 3, 'change_logentry');
INSERT INTO public.auth_permission VALUES (11, 'Can delete log entry', 3, 'delete_logentry');
INSERT INTO public.auth_permission VALUES (12, 'Can view log entry', 3, 'view_logentry');
INSERT INTO public.auth_permission VALUES (13, 'Can add permission', 4, 'add_permission');
INSERT INTO public.auth_permission VALUES (14, 'Can change permission', 4, 'change_permission');
INSERT INTO public.auth_permission VALUES (15, 'Can delete permission', 4, 'delete_permission');
INSERT INTO public.auth_permission VALUES (16, 'Can view permission', 4, 'view_permission');
INSERT INTO public.auth_permission VALUES (17, 'Can add group', 5, 'add_group');
INSERT INTO public.auth_permission VALUES (18, 'Can change group', 5, 'change_group');
INSERT INTO public.auth_permission VALUES (19, 'Can delete group', 5, 'delete_group');
INSERT INTO public.auth_permission VALUES (20, 'Can view group', 5, 'view_group');
INSERT INTO public.auth_permission VALUES (21, 'Can add user', 6, 'add_user');
INSERT INTO public.auth_permission VALUES (22, 'Can change user', 6, 'change_user');
INSERT INTO public.auth_permission VALUES (23, 'Can delete user', 6, 'delete_user');
INSERT INTO public.auth_permission VALUES (24, 'Can view user', 6, 'view_user');
INSERT INTO public.auth_permission VALUES (25, 'Can add content type', 7, 'add_contenttype');
INSERT INTO public.auth_permission VALUES (26, 'Can change content type', 7, 'change_contenttype');
INSERT INTO public.auth_permission VALUES (27, 'Can delete content type', 7, 'delete_contenttype');
INSERT INTO public.auth_permission VALUES (28, 'Can view content type', 7, 'view_contenttype');
INSERT INTO public.auth_permission VALUES (29, 'Can add session', 8, 'add_session');
INSERT INTO public.auth_permission VALUES (30, 'Can change session', 8, 'change_session');
INSERT INTO public.auth_permission VALUES (31, 'Can delete session', 8, 'delete_session');
INSERT INTO public.auth_permission VALUES (32, 'Can view session', 8, 'view_session');
INSERT INTO public.auth_permission VALUES (33, 'Can add transportation', 9, 'add_transportation');
INSERT INTO public.auth_permission VALUES (34, 'Can change transportation', 9, 'change_transportation');
INSERT INTO public.auth_permission VALUES (35, 'Can delete transportation', 9, 'delete_transportation');
INSERT INTO public.auth_permission VALUES (36, 'Can view transportation', 9, 'view_transportation');
INSERT INTO public.auth_permission VALUES (37, 'Can add accomodation', 10, 'add_accomodation');
INSERT INTO public.auth_permission VALUES (38, 'Can change accomodation', 10, 'change_accomodation');
INSERT INTO public.auth_permission VALUES (39, 'Can delete accomodation', 10, 'delete_accomodation');
INSERT INTO public.auth_permission VALUES (40, 'Can view accomodation', 10, 'view_accomodation');
INSERT INTO public.auth_permission VALUES (41, 'Can add rencana wisata', 11, 'add_rencanawisata');
INSERT INTO public.auth_permission VALUES (42, 'Can change rencana wisata', 11, 'change_rencanawisata');
INSERT INTO public.auth_permission VALUES (43, 'Can delete rencana wisata', 11, 'delete_rencanawisata');
INSERT INTO public.auth_permission VALUES (44, 'Can view rencana wisata', 11, 'view_rencanawisata');
INSERT INTO public.auth_permission VALUES (45, 'Can add image album', 12, 'add_imagealbum');
INSERT INTO public.auth_permission VALUES (46, 'Can change image album', 12, 'change_imagealbum');
INSERT INTO public.auth_permission VALUES (47, 'Can delete image album', 12, 'delete_imagealbum');
INSERT INTO public.auth_permission VALUES (48, 'Can view image album', 12, 'view_imagealbum');
INSERT INTO public.auth_permission VALUES (49, 'Can add image', 13, 'add_image');
INSERT INTO public.auth_permission VALUES (50, 'Can change image', 13, 'change_image');
INSERT INTO public.auth_permission VALUES (51, 'Can delete image', 13, 'delete_image');
INSERT INTO public.auth_permission VALUES (52, 'Can view image', 13, 'view_image');


--
-- TOC entry 3548 (class 0 OID 16774)
-- Dependencies: 223
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3550 (class 0 OID 16780)
-- Dependencies: 225
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_user VALUES (1, 'pbkdf2_sha256$390000$UFRRyqVwwfQtTIuiddTpr0$yADVMx+mj9FJ980SjLO6bnOF3rRm5JuedlkAgLMZuiI=', '2022-11-16 22:55:29.372593+07', true, 'admin', '', '', 'richo@gmail.com', true, true, '2022-10-31 13:13:40.732907+07');
INSERT INTO public.auth_user VALUES (2, 'pbkdf2_sha256$390000$JJ3PFIJJ1lP68G8PQYN2se$FS05FSmbtl/8rJjKyo20UHQ8YdElA8PxynZhH/W5pek=', '2022-11-18 21:24:36+07', false, 'Asu', 'Asu', 'Kowe', 'asukowe@gmail.com', false, true, '2022-11-18 21:24:19+07');


--
-- TOC entry 3552 (class 0 OID 16788)
-- Dependencies: 227
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3554 (class 0 OID 16794)
-- Dependencies: 229
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3556 (class 0 OID 16852)
-- Dependencies: 231
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_admin_log VALUES (1, '2022-10-31 13:15:28.019989+07', 'Malang', 'City object (Malang)', 1, '[{"added": {}}, {"added": {"name": "destination", "object": "Destination object (1)"}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (2, '2022-10-31 13:18:18.880221+07', 'Yogyakarta', 'City object (Yogyakarta)', 1, '[{"added": {}}, {"added": {"name": "destination", "object": "Destination object (2)"}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (3, '2022-10-31 21:22:32.370443+07', 'Batu', 'City object (Batu)', 1, '[{"added": {}}, {"added": {"name": "destination", "object": "Destination object (3)"}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (4, '2022-10-31 21:22:43.344218+07', 'Malang', 'City object (Malang)', 3, '', 1, 1);
INSERT INTO public.django_admin_log VALUES (5, '2022-10-31 21:23:13.601053+07', 'Yogyakarta', 'City object (Yogyakarta)', 2, '[{"changed": {"name": "destination", "object": "Destination object (2)", "fields": ["Name"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (6, '2022-10-31 21:24:48.545033+07', 'Batu', 'City object (Batu)', 2, '[{"added": {"name": "destination", "object": "Destination object (4)"}}, {"deleted": {"name": "destination", "object": "Destination object (None)"}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (7, '2022-10-31 21:31:44.689129+07', 'Batu', 'City object (Batu)', 2, '[{"added": {"name": "destination", "object": "Destination object (5)"}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (8, '2022-10-31 21:39:40.531112+07', 'Batu', 'City object (Batu)', 2, '[{"changed": {"name": "destination", "object": "Destination object (4)", "fields": ["Image path"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (9, '2022-10-31 22:01:32.554514+07', 'Batu', 'City object (Batu)', 2, '[{"changed": {"name": "destination", "object": "Destination object (5)", "fields": ["Image path"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (10, '2022-10-31 22:02:17.238775+07', 'Yogyakarta', 'City object (Yogyakarta)', 2, '[{"changed": {"name": "destination", "object": "Destination object (2)", "fields": ["Image path"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (11, '2022-10-31 22:03:05.813297+07', 'Batu', 'City object (Batu)', 2, '[{"added": {"name": "destination", "object": "Destination object (6)"}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (12, '2022-11-01 23:32:12.548557+07', 'Malang', 'City object (Malang)', 1, '[{"added": {}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (13, '2022-11-02 00:00:52.50406+07', 'Malang', 'City object (Malang)', 2, '[{"added": {"name": "destination", "object": "Destination object (7)"}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (14, '2022-11-02 20:48:57.828498+07', 'Yogyakarta', 'City object (Yogyakarta)', 2, '[{"added": {"name": "destination", "object": "Destination object (8)"}}, {"added": {"name": "destination", "object": "Destination object (9)"}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (15, '2022-11-02 21:29:53.676729+07', '1', 'Transportation object (1)', 1, '[{"added": {}}]', 9, 1);
INSERT INTO public.django_admin_log VALUES (16, '2022-11-02 21:30:04.911561+07', '1', 'Transportation object (1)', 2, '[{"changed": {"fields": ["Arrive time"]}}]', 9, 1);
INSERT INTO public.django_admin_log VALUES (17, '2022-11-02 21:33:59.168577+07', 'Malang', 'City object (Malang)', 2, '[{"changed": {"fields": ["Image", "Description"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (18, '2022-11-02 21:34:38.112144+07', 'Yogyakarta', 'City object (Yogyakarta)', 2, '[{"changed": {"fields": ["Image", "Description"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (19, '2022-11-02 21:35:01.389762+07', 'Batu', 'City object (Batu)', 2, '[{"changed": {"fields": ["Image", "Description"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (20, '2022-11-03 10:43:46.539633+07', 'Malang', 'City object (Malang)', 2, '[{"added": {"name": "destination", "object": "Destination object (10)"}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (21, '2022-11-03 12:58:25.503426+07', 'Batu', 'City object (Batu)', 2, '[{"changed": {"name": "destination", "object": "Destination object (4)", "fields": ["Categories"]}}, {"changed": {"name": "destination", "object": "Destination object (5)", "fields": ["Categories"]}}, {"changed": {"name": "destination", "object": "Destination object (6)", "fields": ["Categories"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (22, '2022-11-03 12:58:42.169457+07', 'Malang', 'City object (Malang)', 2, '[{"changed": {"name": "destination", "object": "Destination object (7)", "fields": ["Categories"]}}, {"changed": {"name": "destination", "object": "Destination object (10)", "fields": ["Categories"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (23, '2022-11-03 12:58:55.415631+07', 'Yogyakarta', 'City object (Yogyakarta)', 2, '[{"changed": {"name": "destination", "object": "Destination object (2)", "fields": ["Categories"]}}, {"changed": {"name": "destination", "object": "Destination object (8)", "fields": ["Categories"]}}, {"changed": {"name": "destination", "object": "Destination object (9)", "fields": ["Categories"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (24, '2022-11-03 13:02:21.040547+07', 'Yogyakarta', 'City object (Yogyakarta)', 2, '[{"changed": {"name": "destination", "object": "Destination object (2)", "fields": ["Categories"]}}, {"changed": {"name": "destination", "object": "Destination object (8)", "fields": ["Categories"]}}, {"changed": {"name": "destination", "object": "Destination object (9)", "fields": ["Categories"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (25, '2022-11-03 13:02:36.898438+07', 'Malang', 'City object (Malang)', 2, '[{"changed": {"name": "destination", "object": "Destination object (7)", "fields": ["Categories"]}}, {"changed": {"name": "destination", "object": "Destination object (10)", "fields": ["Categories"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (26, '2022-11-03 13:02:54.162187+07', 'Batu', 'City object (Batu)', 2, '[{"changed": {"name": "destination", "object": "Destination object (4)", "fields": ["Categories"]}}, {"changed": {"name": "destination", "object": "Destination object (5)", "fields": ["Categories"]}}, {"changed": {"name": "destination", "object": "Destination object (6)", "fields": ["Categories"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (27, '2022-11-16 22:55:43.821337+07', 'Yogyakarta', 'City object (Yogyakarta)', 2, '[{"changed": {"fields": ["Province"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (28, '2022-11-16 22:55:52.042215+07', 'Malang', 'City object (Malang)', 2, '[{"changed": {"fields": ["Province"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (29, '2022-11-16 22:56:06.485996+07', 'Batu', 'City object (Batu)', 2, '[{"changed": {"fields": ["Province"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (30, '2022-11-16 22:56:22.164099+07', 'Yogyakarta', 'City object (Yogyakarta)', 2, '[{"changed": {"fields": ["Province"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (31, '2022-11-17 11:28:31.643703+07', '2', '[''KA Malioboro Express'', <City: Malang>, <City: Yogyakarta>, 195000]', 1, '[{"added": {}}]', 9, 1);
INSERT INTO public.django_admin_log VALUES (32, '2022-11-17 11:29:03.11327+07', '1', '[''Bus Bagong'', <City: Malang>, <City: Batu>, 20000]', 2, '[{"changed": {"fields": ["Name"]}}]', 9, 1);
INSERT INTO public.django_admin_log VALUES (33, '2022-11-17 11:32:24.100254+07', '3', '[''KA  Kertanegara'', <City: Yogyakarta>, <City: Malang>, 195000]', 1, '[{"added": {}}]', 9, 1);
INSERT INTO public.django_admin_log VALUES (34, '2022-11-17 13:43:16.111533+07', '1', 'Accomodation object (1)', 1, '[{"added": {}}]', 10, 1);
INSERT INTO public.django_admin_log VALUES (35, '2022-11-17 13:46:03.624225+07', 'Yogyakarta', 'Yogyakarta', 2, '[{"added": {"name": "destination", "object": "[''Pantai Parangtritis'', 15000]"}}, {"added": {"name": "destination", "object": "[''Gembira Loka Zoo'', 60000]"}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (36, '2022-11-17 13:47:04.606297+07', 'Yogyakarta', 'Yogyakarta', 2, '[{"added": {"name": "destination", "object": "[''Jogja City Mall'', 0]"}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (37, '2022-11-18 09:51:45.08801+07', 'Yogyakarta', 'Yogyakarta', 2, '[{"changed": {"name": "destination", "object": "[''Candi Prambanan'', 50000]", "fields": ["Kecamatan"]}}, {"changed": {"name": "destination", "object": "[''Gembira Loka Zoo'', 60000]", "fields": ["Kecamatan"]}}, {"changed": {"name": "destination", "object": "[''Jogja City Mall'', 0]", "fields": ["Kecamatan"]}}, {"changed": {"name": "destination", "object": "[''Malioboro Street'', 0]", "fields": ["Kecamatan"]}}, {"changed": {"name": "destination", "object": "[''Museum Gunungapi Merapi'', 0]", "fields": ["Kecamatan"]}}, {"changed": {"name": "destination", "object": "[''Pantai Parangtritis'', 15000]", "fields": ["Kecamatan"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (38, '2022-11-18 10:02:15.695999+07', '1', 'ImageAlbum object (1)', 1, '[{"added": {}}]', 12, 1);
INSERT INTO public.django_admin_log VALUES (39, '2022-11-18 10:18:50.311589+07', '1', 'Image object (1)', 1, '[{"added": {}}]', 13, 1);
INSERT INTO public.django_admin_log VALUES (40, '2022-11-18 10:19:50.552805+07', '2', 'ImageAlbum object (2)', 1, '[{"added": {}}]', 12, 1);
INSERT INTO public.django_admin_log VALUES (41, '2022-11-18 10:19:53.803321+07', '3', 'ImageAlbum object (3)', 1, '[{"added": {}}]', 12, 1);
INSERT INTO public.django_admin_log VALUES (42, '2022-11-18 10:19:56.279375+07', '4', 'ImageAlbum object (4)', 1, '[{"added": {}}]', 12, 1);
INSERT INTO public.django_admin_log VALUES (43, '2022-11-18 10:19:58.749637+07', '5', 'ImageAlbum object (5)', 1, '[{"added": {}}]', 12, 1);
INSERT INTO public.django_admin_log VALUES (44, '2022-11-18 10:20:01.251621+07', '6', 'ImageAlbum object (6)', 1, '[{"added": {}}]', 12, 1);
INSERT INTO public.django_admin_log VALUES (45, '2022-11-18 10:20:04.387852+07', 'Yogyakarta', 'Yogyakarta', 2, '[{"changed": {"name": "destination", "object": "[''Candi Prambanan'', 50000]", "fields": ["Album"]}}, {"changed": {"name": "destination", "object": "[''Gembira Loka Zoo'', 60000]", "fields": ["Album"]}}, {"changed": {"name": "destination", "object": "[''Jogja City Mall'', 0]", "fields": ["Album"]}}, {"changed": {"name": "destination", "object": "[''Malioboro Street'', 0]", "fields": ["Album"]}}, {"changed": {"name": "destination", "object": "[''Museum Gunungapi Merapi'', 0]", "fields": ["Album"]}}, {"changed": {"name": "destination", "object": "[''Pantai Parangtritis'', 15000]", "fields": ["Album"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (46, '2022-11-18 10:54:04.499215+07', '2', 'Image object (2)', 1, '[{"added": {}}]', 13, 1);
INSERT INTO public.django_admin_log VALUES (47, '2022-11-18 11:05:51.923134+07', 'Yogyakarta', 'Yogyakarta', 2, '[{"changed": {"name": "destination", "object": "[''Candi Prambanan'', 50000]", "fields": ["Image path"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (48, '2022-11-18 11:14:54.571588+07', 'Yogyakarta', 'Yogyakarta', 2, '[{"changed": {"name": "destination", "object": "[''Candi Prambanan'', 50000]", "fields": ["Description"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (49, '2022-11-18 11:16:52.581859+07', 'Yogyakarta', 'Yogyakarta', 2, '[{"changed": {"name": "destination", "object": "[''Candi Prambanan'', 50000]", "fields": ["Description"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (50, '2022-11-18 11:17:09.41924+07', 'Yogyakarta', 'Yogyakarta', 2, '[{"changed": {"name": "destination", "object": "[''Candi Prambanan'', 50000]", "fields": ["Description"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (51, '2022-11-18 11:34:06.827986+07', 'Yogyakarta', 'Yogyakarta', 2, '[{"changed": {"name": "destination", "object": "[''Candi Prambanan'', 50000]", "fields": ["Description"]}}, {"changed": {"name": "destination", "object": "[''Gembira Loka Zoo'', 60000]", "fields": ["Description"]}}, {"changed": {"name": "destination", "object": "[''Jogja City Mall'', 0]", "fields": ["Description"]}}, {"changed": {"name": "destination", "object": "[''Malioboro Street'', 0]", "fields": ["Description"]}}, {"changed": {"name": "destination", "object": "[''Museum Gunungapi Merapi'', 0]", "fields": ["Description"]}}, {"changed": {"name": "destination", "object": "[''Pantai Parangtritis'', 15000]", "fields": ["Description"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (52, '2022-11-18 12:02:44.556375+07', 'Yogyakarta', 'Yogyakarta', 2, '[{"changed": {"name": "destination", "object": "[''Candi Prambanan'', 50000]", "fields": ["Maps", "Panorama"]}}, {"changed": {"name": "destination", "object": "[''Gembira Loka Zoo'', 60000]", "fields": ["Maps", "Panorama"]}}, {"changed": {"name": "destination", "object": "[''Jogja City Mall'', 0]", "fields": ["Maps", "Panorama"]}}, {"changed": {"name": "destination", "object": "[''Malioboro Street'', 0]", "fields": ["Maps", "Panorama"]}}, {"changed": {"name": "destination", "object": "[''Museum Gunungapi Merapi'', 0]", "fields": ["Maps", "Panorama"]}}, {"changed": {"name": "destination", "object": "[''Pantai Parangtritis'', 15000]", "fields": ["Maps", "Panorama"]}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (53, '2022-11-18 18:00:50.249526+07', '1', 'RencanaWisata object (1)', 1, '[{"added": {}}]', 11, 1);
INSERT INTO public.django_admin_log VALUES (54, '2022-11-18 20:42:05.142747+07', '1', 'Explore Yogyakarta 2D 1N', 2, '[{"changed": {"fields": ["Theme"]}}]', 11, 1);
INSERT INTO public.django_admin_log VALUES (55, '2022-11-18 21:24:19.792521+07', '2', 'Asu', 1, '[{"added": {}}]', 6, 1);
INSERT INTO public.django_admin_log VALUES (56, '2022-11-18 21:24:37.265118+07', '2', 'Asu', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address", "Last login"]}}]', 6, 1);
INSERT INTO public.django_admin_log VALUES (57, '2022-11-19 10:35:40.735939+07', '1', 'Explore Yogyakarta 2D 1N', 2, '[{"changed": {"fields": ["Cover"]}}]', 11, 1);


--
-- TOC entry 3540 (class 0 OID 16744)
-- Dependencies: 215
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_migrations VALUES (1, 'contenttypes', '0001_initial', '2022-10-31 13:12:50.959525+07');
INSERT INTO public.django_migrations VALUES (2, 'auth', '0001_initial', '2022-10-31 13:12:51.068896+07');
INSERT INTO public.django_migrations VALUES (3, 'admin', '0001_initial', '2022-10-31 13:12:51.100159+07');
INSERT INTO public.django_migrations VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2022-10-31 13:12:51.100159+07');
INSERT INTO public.django_migrations VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2022-10-31 13:12:51.115785+07');
INSERT INTO public.django_migrations VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2022-10-31 13:12:51.115785+07');
INSERT INTO public.django_migrations VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2022-10-31 13:12:51.131411+07');
INSERT INTO public.django_migrations VALUES (8, 'auth', '0003_alter_user_email_max_length', '2022-10-31 13:12:51.131411+07');
INSERT INTO public.django_migrations VALUES (9, 'auth', '0004_alter_user_username_opts', '2022-10-31 13:12:51.147037+07');
INSERT INTO public.django_migrations VALUES (10, 'auth', '0005_alter_user_last_login_null', '2022-10-31 13:12:51.147037+07');
INSERT INTO public.django_migrations VALUES (11, 'auth', '0006_require_contenttypes_0002', '2022-10-31 13:12:51.147037+07');
INSERT INTO public.django_migrations VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2022-10-31 13:12:51.147037+07');
INSERT INTO public.django_migrations VALUES (13, 'auth', '0008_alter_user_username_max_length', '2022-10-31 13:12:51.162653+07');
INSERT INTO public.django_migrations VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2022-10-31 13:12:51.178292+07');
INSERT INTO public.django_migrations VALUES (15, 'auth', '0010_alter_group_name_max_length', '2022-10-31 13:12:51.178292+07');
INSERT INTO public.django_migrations VALUES (16, 'auth', '0011_update_proxy_permissions', '2022-10-31 13:12:51.178292+07');
INSERT INTO public.django_migrations VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2022-10-31 13:12:51.193904+07');
INSERT INTO public.django_migrations VALUES (18, 'sessions', '0001_initial', '2022-10-31 13:12:51.20954+07');
INSERT INTO public.django_migrations VALUES (19, 'tours', '0001_initial', '2022-10-31 13:12:51.240783+07');
INSERT INTO public.django_migrations VALUES (20, 'tours', '0002_alter_city_related_city', '2022-10-31 13:18:12.944093+07');
INSERT INTO public.django_migrations VALUES (21, 'tours', '0003_alter_destination_image_path', '2022-10-31 21:37:56.178343+07');
INSERT INTO public.django_migrations VALUES (22, 'tours', '0004_city_description_city_image_and_more', '2022-11-02 21:06:48.850133+07');
INSERT INTO public.django_migrations VALUES (23, 'tours', '0005_alter_transportation_moda', '2022-11-02 21:18:21.370146+07');
INSERT INTO public.django_migrations VALUES (24, 'tours', '0006_transportation_duration', '2022-11-02 21:23:39.981353+07');
INSERT INTO public.django_migrations VALUES (25, 'tours', '0007_alter_transportation_duration', '2022-11-02 21:29:49.637057+07');
INSERT INTO public.django_migrations VALUES (26, 'tours', '0008_destination_categories', '2022-11-03 12:57:54.500467+07');
INSERT INTO public.django_migrations VALUES (27, 'tours', '0009_alter_destination_categories', '2022-11-03 13:00:49.431876+07');
INSERT INTO public.django_migrations VALUES (28, 'tours', '0010_city_province_alter_destination_categories', '2022-11-16 22:49:14.823142+07');
INSERT INTO public.django_migrations VALUES (29, 'tours', '0011_rencanawisata', '2022-11-17 11:15:46.136089+07');
INSERT INTO public.django_migrations VALUES (30, 'tours', '0012_alter_accomodation_options_alter_city_options_and_more', '2022-11-17 11:19:08.403991+07');
INSERT INTO public.django_migrations VALUES (31, 'tours', '0013_alter_accomodation_options_alter_city_options_and_more', '2022-11-17 11:26:55.760263+07');
INSERT INTO public.django_migrations VALUES (32, 'tours', '0014_rename_transportasi_rencanawisata_transportasi_pergi_and_more', '2022-11-17 11:31:13.821085+07');
INSERT INTO public.django_migrations VALUES (33, 'tours', '0015_destination_kecamatan_rencanawisata_title_and_more', '2022-11-18 09:49:10.57358+07');
INSERT INTO public.django_migrations VALUES (34, 'tours', '0016_imagealbum_image_destination_album', '2022-11-18 09:58:30.167881+07');
INSERT INTO public.django_migrations VALUES (35, 'tours', '0017_alter_destination_description', '2022-11-18 11:16:32.362102+07');
INSERT INTO public.django_migrations VALUES (36, 'tours', '0018_alter_destination_description', '2022-11-18 11:29:43.28089+07');
INSERT INTO public.django_migrations VALUES (37, 'tours', '0019_destination_maps_destination_panorama', '2022-11-18 12:01:25.630149+07');
INSERT INTO public.django_migrations VALUES (38, 'tours', '0020_rencanawisata_theme', '2022-11-18 19:54:49.470012+07');
INSERT INTO public.django_migrations VALUES (39, 'tours', '0021_rencanawisata_cover', '2022-11-19 10:34:22.672276+07');
INSERT INTO public.django_migrations VALUES (40, 'tours', '0022_accomodation_created_at_accomodation_updated_at_and_more', '2022-11-19 12:58:58.085403+07');


--
-- TOC entry 3557 (class 0 OID 16880)
-- Dependencies: 232
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_session VALUES ('qipo6jvyh3cg3ky76mn9pjsu0xt9m6o4', '.eJxVjEsOAiEQBe_C2pBu-Qgu3XsG0tAgowaSYWZlvLtOMgvdvqp6LxFoXWpYR57DxOIsUBx-t0jpkdsG-E7t1mXqbZmnKDdF7nTIa-f8vOzu30GlUb_1kUmxQeud9ZC1pgIIZB1AJmcck2NIET1ohcjGRWMw6nzyCkqyUMT7A8hYNzA:1opO3N:iGU9k2eWje5NlVJUco2uHpNoFBlzA4NM7IEmn1yx6ug', '2022-11-14 13:13:45.045898+07');
INSERT INTO public.django_session VALUES ('kybe9lruhtyltp2zbkfazb8whv6xi9xj', '.eJxVjEsOAiEQBe_C2pBu-Qgu3XsG0tAgowaSYWZlvLtOMgvdvqp6LxFoXWpYR57DxOIsUBx-t0jpkdsG-E7t1mXqbZmnKDdF7nTIa-f8vOzu30GlUb_1kUmxQeud9ZC1pgIIZB1AJmcck2NIET1ohcjGRWMw6nzyCkqyUMT7A8hYNzA:1opjrA:DaqdoQS3zG1PtP-8DKEaRUCo33TPxnKNEA-Pu3wDdnA', '2022-11-15 12:30:36.596778+07');
INSERT INTO public.django_session VALUES ('73m176zmybz0eqmns6wyk7zn0vcceaqp', '.eJxVjEsOAiEQBe_C2pBu-Qgu3XsG0tAgowaSYWZlvLtOMgvdvqp6LxFoXWpYR57DxOIsUBx-t0jpkdsG-E7t1mXqbZmnKDdF7nTIa-f8vOzu30GlUb_1kUmxQeud9ZC1pgIIZB1AJmcck2NIET1ohcjGRWMw6nzyCkqyUMT7A8hYNzA:1ovKl7:mFQq4rU2kpegITu_lMS2oa3wA3Y6u--MIr4K6ZNAZOg', '2022-11-30 22:55:29.377606+07');


--
-- TOC entry 3558 (class 0 OID 16889)
-- Dependencies: 233
-- Data for Name: tours_city; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_city VALUES ('Malang', 'Batu', 'Kota Malang (diucapkan [malaŋ], bahasa Jawa: Hanacaraka: ꦩꦭꦁ, Pegon: مالاڠ, Osob kiwalan: Ngalam) adalah sebuah kota yang terletak di provinsi Jawa Timur, Indonesia,[5] Kota terbesar kedua di Jawa Timur setelah Surabaya, dan kota terbesar ke-12 di Indonesia.[6] Kota ini didirikan pada masa Pemerintahan Belanda pada tanggal 1 April 1914, yang dimana E.K Broeveldt sebagai wali kota pertama,Kota ini terletak di dataran tinggi seluas 145,28 km²[7] yang merupakan enklave Kabupaten Malang.[8] Bersama dengan Kota Batu dan Kabupaten Malang, Kota Malang merupakan bagian dari kesatuan wilayah yang dikenal dengan Malang Raya.  Kota Malang dikenal baik sebagai kota pendidikan. Kota ini memiliki berbagai perguruan tinggi terbaik seperti Universitas Brawijaya,[9] Universitas Negeri Malang,[9] UIN Maulana Malik Ibrahim Malang, dan Politeknik Negeri Malang. Selain itu, kota ini merupakan kota pariwisata karena alamnya yang menawan yang dikelilingi oleh pegunungan[10] serta udaranya yang sejuk.[11] Malang pun terkenal sebagai kota bunga karena banyaknya bunga yang menghiasi kota.[12] Kota Malang juga merupakan kota seni[13] karena banyaknya kesenian khas dari kota ini, mulai dari tarian hingga pertunjukan.', 'image/63764-pemandangan-kota-malang-instagramcomchristianjazzy.jpg', 'Jawa Timur', '2022-11-19 12:58:58.031811+07', '2022-11-19 12:58:58.038381+07');
INSERT INTO public.tours_city VALUES ('Batu', 'Malang', 'Batu (bahasa Jawa: Hanacaraka: ꦧꦠꦸ Pegon: باتو osob kiwalan: Utab[5]) adalah sebuah kota di Provinsi Jawa Timur, Indonesia. Kota ini terletak 90 km sebelah barat daya Surabaya atau 15 km sebelah barat laut Malang. Kota Batu berada di jalur yang menghubungkan Malang-Kediri dan Malang-Jombang. Kota Batu berbatasan dengan Kabupaten Mojokerto dan Kabupaten Pasuruan di sebelah utara serta dengan Kabupaten Malang di sebelah timur, selatan, dan barat. Wilayah kota ini berada di ketinggian 700-2.000 meter dan ketinggian rata-rata yaitu 871 meter[6] di atas permukaan laut dengan suhu udara rata-rata mencapai 11-19 derajat Celsius.  Kota Batu dahulu merupakan bagian dari Kabupaten Malang, yang kemudian ditetapkan menjadi kota administratif pada 6 Maret 1993. Pada tanggal 17 Oktober 2001, Batu ditetapkan sebagai kota otonom yang terpisah dari Kabupaten Malang', 'image/download_1.jpg', 'Jawa Timur', '2022-11-19 12:58:58.031811+07', '2022-11-19 12:58:58.038381+07');
INSERT INTO public.tours_city VALUES ('Yogyakarta', '', 'Kota Yogyakarta (bahasa Jawa: ꦪꦺꦴꦒꦾꦏꦂꦠ, translit. Ngayogyakarta, pengucapan bahasa Jawa: [kuʈɔ ŋajogjɔˈkart̪ɔ]) atau dikenal oleh masyarakat setempat dengan nama Kota Jogja atau Kota Yogya adalah ibu kota dan pusat pemerintahan provinsi Daerah Istimewa Yogyakarta, Indonesia. Kota ini adalah kota besar yang mempertahankan konsep tradisional dan budaya Jawa. Kota Yogyakarta menjadi kediaman bagi Sultan Hamengkubuwana dan Adipati Paku Alam.  Salah satu kecamatan di Yogyakarta, yaitu Kotagede pernah menjadi pusat Kesultanan Mataram antara kurun tahun 1575–1640. Keraton (Istana) yang masih berfungsi dalam arti yang sesungguhnya adalah Keraton Ngayogyakarta dan Puro Paku Alaman, yang merupakan pecahan dari Kesultanan Mataram. Pada masa revolusi, Yogyakarta juga pernah menjadi ibu kota Indonesia antara tahun 1946 hingga 1950.', 'image/yogyakarta-indonesia-motorbike-guide-main-image.jpg', 'Daerah Istimewa Yogyakarta', '2022-11-19 12:58:58.031811+07', '2022-11-19 12:58:58.038381+07');


--
-- TOC entry 3564 (class 0 OID 16929)
-- Dependencies: 239
-- Data for Name: tours_accomodation; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_accomodation VALUES (1, 150000, 'Jalan Giwangan Yogyakarta', 'images/SCH-2.jpg', 'Yogyakarta', 'Hotel Alpha', '2022-11-19 12:58:58.004771+07', '2022-11-19 12:58:58.025337+07');


--
-- TOC entry 3576 (class 0 OID 25150)
-- Dependencies: 251
-- Data for Name: tours_imagealbum; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_imagealbum VALUES (1);
INSERT INTO public.tours_imagealbum VALUES (2);
INSERT INTO public.tours_imagealbum VALUES (3);
INSERT INTO public.tours_imagealbum VALUES (4);
INSERT INTO public.tours_imagealbum VALUES (5);
INSERT INTO public.tours_imagealbum VALUES (6);


--
-- TOC entry 3560 (class 0 OID 16895)
-- Dependencies: 235
-- Data for Name: tours_destination; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_destination VALUES (7, 'Malang Smart Arena', 'images/download_FA9R6jv.jpg', 'fdsf', 'dsfsdf', '00:00:48', '00:00:48', 3242, 323423, 'Malang', 'Taman Bermain', NULL, NULL, NULL, NULL, '2022-11-19 12:58:58.045395+07', '2022-11-19 12:58:58.051408+07');
INSERT INTO public.tours_destination VALUES (10, 'Hawaii Waterpark Malang', 'images/bns_fZzxSgW.jpeg', 'dfsdf', 'dfssd', '10:43:42', '10:43:43', 12312, 123123, 'Malang', 'Taman Bermain', NULL, NULL, NULL, NULL, '2022-11-19 12:58:58.045395+07', '2022-11-19 12:58:58.051408+07');
INSERT INTO public.tours_destination VALUES (4, 'Batu Night Spectacular (BNS)', 'images/bns.jpeg', 'Jl. Hayam Wuruk No.1, Oro-Oro Ombo, Kec. Batu, Kota Batu, Jawa Timur 65316, Indonesia', 'Rasakan kemeriahan pasar malam di Batu Night Spectacular Nikmati beragam wahana yang cocok untuk seluruh anggota keluarga Jelajahi taman lampionnya dan abadikan cantiknya lampion berwarna-warni Saksikan pertunjukan air mancur dan multimedia yang spektakuler digelar setiap hari pada pukul 20:30', '15:00:00', '23:00:00', 35000, 120000, 'Batu', 'Taman Bermain', NULL, NULL, NULL, NULL, '2022-11-19 12:58:58.045395+07', '2022-11-19 12:58:58.051408+07');
INSERT INTO public.tours_destination VALUES (5, 'Jawa Timur Park 1', 'images/wisata-jatim-park_169.jpeg', 'dfasdfsd', 'dffsdf', '21:31:40', '21:31:41', 12, 12, 'Batu', 'Taman Bermain', NULL, NULL, NULL, NULL, '2022-11-19 12:58:58.045395+07', '2022-11-19 12:58:58.051408+07');
INSERT INTO public.tours_destination VALUES (6, 'Jawa Timur Park 3', 'images/download.jpg', 'fgsdg', 'dfgdfg', '22:02:58', '22:02:59', 342, 143, 'Batu', 'Taman Bermain', NULL, NULL, NULL, NULL, '2022-11-19 12:58:58.045395+07', '2022-11-19 12:58:58.051408+07');
INSERT INTO public.tours_destination VALUES (12, 'Gembira Loka Zoo', 'images/transmart-malang.jpeg', 'hthdghdhgdfh', '<p>dfgfdg</p>', '13:45:48', '13:45:51', 60000, 60000, 'Yogyakarta', 'Kebun Binatang', 'Umbulharjo', 2, 's', 's', '2022-11-19 12:58:58.045395+07', '2022-11-19 12:58:58.051408+07');
INSERT INTO public.tours_destination VALUES (13, 'Jogja City Mall', 'images/JCM-Jogja_City_Mall_Panyogan.jpg', 'fvfsvffssfsdfds', '<p>fsgfsfdafsdfsdfds</p>', '13:46:58', '13:46:59', 0, 0, 'Yogyakarta', 'Pusat Belanja', 'Sleman', 3, 's', 's', '2022-11-19 12:58:58.045395+07', '2022-11-19 12:58:58.051408+07');
INSERT INTO public.tours_destination VALUES (2, 'Malioboro Street', 'images/5ee208425be9b.jpg', 'Jalan Malioboro, Kota Yogyakarta, Indonesia', '<p>Jalan Malioboro adalah nama salah satu kawasan jalan dari tiga jalan di Kota Yogyakarta yang membentang dari Tugu Yogyakarta hingga ke perempatan Kantor Pos Yogyakarta. Secara keseluruhan terdiri atas Jalan Margo Utomo, Jalan Malioboro, dan Jalan Margo Mulyo. Jalan ini merupakan poros Garis Imajiner Kraton Yogyakarta.</p>', '00:00:00', '23:59:00', 0, 0, 'Yogyakarta', 'Pusat Belanja', 'Malioboro', 4, 's', 's', '2022-11-19 12:58:58.045395+07', '2022-11-19 12:58:58.051408+07');
INSERT INTO public.tours_destination VALUES (9, 'Museum Gunungapi Merapi', 'images/Museum-Gunung-Merapi-Yogyakarta.jpeg', 'Jln. Boyong, Dusun Banteng, Desa Hargobinangun, Kecamatan Pakem, Kabupaten Sleman, Daerah Istimewa Yogyakarta', '<p>Museum Gunung Merapi (bahasa Jawa: ꦩꦸꦱꦶꦪꦸꦩ꧀ꦒꦸꦤꦸꦁꦩꦼꦫꦥꦶ, translit. Musiyum Gunung Merapi) merupakan museum bersejarah yang terdapat di Yogyakarta tepatnya di Jln. Boyong, Dusun Banteng, Desa Hargobinangun, Kecamatan Pakem, Kabupaten Sleman, Daerah Istimewa Yogyakarta [1] sekitar lima kilometer dari kawasan objek wisata Kaliurang. Museum Gunung Merapi telah diresmikan pada tanggal 1 Oktober 2009 oleh Menteri Energi dan Sumber Daya Mineral (ESDM), Purnomo Yusgiantoro. Dengan luas bangunan sekitar 4</p>', '08:00:00', '15:00:00', 0, 0, 'Yogyakarta', 'Tempat Bersejarah', 'Kaliurang', 5, 's', 's', '2022-11-19 12:58:58.045395+07', '2022-11-19 12:58:58.051408+07');
INSERT INTO public.tours_destination VALUES (11, 'Pantai Parangtritis', 'images/1652843776_1.jpg', 'dsfsd', '<p>sdfds</p>', '13:44:20', '13:44:19', 15000, 15000, 'Yogyakarta', 'Wisata Alam', 'Bantul', 6, 's', 's', '2022-11-19 12:58:58.045395+07', '2022-11-19 12:58:58.051408+07');
INSERT INTO public.tours_destination VALUES (8, 'Candi Prambanan', 'images/Candi_Hindu_Prambanan_a5bc0cg.jpg', 'Jl. Raya Solo - Yogyakarta No.16, Kranggan, Bokoharjo, Kec. Prambanan, Kabupaten Sleman, Daerah Istimewa Yogyakarta 55571', '<p style="box-sizing: border-box; margin: 0px 0px 36px; font-size: 16px; line-height: 28px; letter-spacing: 0.3px; color: #333333; font-family: proxima-nova-alt, sans-serif; background-color: #ffffff;">Candi Prambanan merupakan candi Hindu yang terbesar di Indonesia. Sampai saat ini belum dapat dipastikan kapan candi ini dibangun dan atas perintah siapa, namun kuat dugaan bahwa Candi Prambanan dibangun sekitar pertengahan abad ke-9 oleh raja dari Wangsa Sanjaya, yaitu Raja Balitung Maha Sambu. Dugaan tersebut didasarkan pada isi Prasasti Syiwagrha yang ditemukan di sekitar Prambanan dan saat ini tersimpan di Museum Nasional di Jakarta. Prasasti berangka tahun 778 Saka (856 M) ini ditulis pada masa pemerintahan Rakai Pikatan.</p>
<p style="box-sizing: border-box; margin: 0px 0px 20px; font-size: 16px; line-height: 28px; letter-spacing: 0.3px; color: #333333; font-family: proxima-nova-alt, sans-serif; background-color: #ffffff;">Denah asli Candi Prambanan berbentuk persegi panjang, terdiri atas halaman luar dan tiga pelataran, yaitu Jaba (pelataran luar), Tengahan (pelataran tengah) dan Njeron (pelataran dalam). Halaman luar merupakan areal terbuka yang mengelilingi pelataran luar. Pelataran luar berbentuk bujur dengan luas 390 m2. Pelataran ini dahulu dikelilingi oleh pagar batu yang kini sudah tinggal reruntuhan. Pelataran luar saat ini hanya merupakan pelataran kosong. Belum diketahui apakah semula terdapat bangunan atau hiasan lain di pelataran ini.</p>
<p style="box-sizing: border-box; margin: 0px 0px 20px; font-size: 16px; line-height: 28px; letter-spacing: 0.3px; color: #333333; font-family: proxima-nova-alt, sans-serif; background-color: #ffffff;">Di tengah pelataran luar, terdapat pelataran kedua, yaitu pelataran tengah yang berbentuk persegi panjang seluas 222 m2. Pelataran tengah dahulu juga dikelilingi pagar batu yang saat ini juga sudah runtuh. Pelataran ini terdiri atas empat teras berundak, makin ke dalam makin tinggi. Di teras pertama, yaitu teras yang terbawah, terdapat 68 candi kecil yang berderet berkeliling, terbagi dalam empat baris oleh jalan penghubung antarpintu pelataran. Di teras kedua terdapat 60 candi, di teras ketiga terdapat 52 candi, dan di teras keempat, atau teras teratas, terdapat 44 candi. Seluruh candi di pelataran tengah ini mempunyai bentuk dan ukuran yang sama, yaitu luas denah dasar 6 m2 dan tinggi 14 m. Hampir semua candi di pelataran tengah tersebut saat ini dalam keadaan hancur. Yang tersisa hanya reruntuhannya saja.</p>
<p style="box-sizing: border-box; margin: 0px 0px 20px; font-size: 16px; line-height: 28px; letter-spacing: 0.3px; color: #333333; font-family: proxima-nova-alt, sans-serif; background-color: #ffffff;">Pelataran dalam, merupakan pelataran yang paling tinggi letaknya dan yang dianggap sebagai tempat yang paling suci. Pelataran ini berdenah persegi empat seluas 110 m2, dengan tinggi sekitar 1,5 m dari permukaan teras teratas pelataran tengah. Pelataran ini dikelilingi oleh turap dan pagar batu. Di keempat sisinya terdapat gerbang berbentuk gapura paduraksa. Saat ini hanya gapura di sisi selatan yang masih utuh. Di depan masing-masing gerbang pelataran teratas terdapat sepasang candi kecil, berdenah dasar bujur sangkar seluas 1, 5 m2 dengan tinggi 4 m.</p>
<p style="box-sizing: border-box; margin: 0px 0px 20px; font-size: 16px; line-height: 28px; letter-spacing: 0.3px; color: #333333; font-family: proxima-nova-alt, sans-serif; background-color: #ffffff;">Di pelataran dalam terdapat 2 barisan candi yang membujur arah utara selatan. Di barisan barat terdapat 3 buah candi yang menghadap ke timur. Candi yang letaknya paling utara adalah Candi Wisnu, di tengah adalah Candi Syiwa, dan di selatan adalah Candi Brahma. Di barisan timur juga terdapat 3 buah candi yang menghadap ke barat. Ketiga candi ini disebut candi wahana (wahana = kendaraan), karena masing-masing candi diberi nama sesuai dengan binatang yang merupakan tunggangan dewa yang candinya terletak di hadapannya.</p>
<p style="box-sizing: border-box; margin: 0px 0px 20px; font-size: 16px; line-height: 28px; letter-spacing: 0.3px; color: #333333; font-family: proxima-nova-alt, sans-serif; background-color: #ffffff;">Candi yang berhadapan dengan Candi Wisnu adalah Candi Garuda, yang berhadapan dengan Candi Syiwa adalah Candi Nandi (lembu), dan yang berhadapan dengan Candi Brahma adalah Candi Angsa. Dengan demikian, keenam candi ini saling berhadapan membentuk lorong. Candi Wisnu, Brahma, Angsa, Garuda dan Nandi mempunyai bentuk dan ukuran yang sama, yaitu berdenah dasar bujur sangkar seluas 15 m2 dengan tinggi 25 m. Di ujung utara dan selatan lorong masing-masing terdapat sebuah candi kecil yang saling berhadapan, yang disebut Candi Apit.</p>', '06:30:00', '17:00:00', 50000, 50000, 'Yogyakarta', 'Tempat Bersejarah', 'Prambanan', 1, '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3953.355933734317!2d110.48927871440186!3d-7.752020594412806!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e7a5ae3dbd859d1%3A0x19e7a03b25955a2d!2sCandi%20Prambanan!5e0!3m2!1sid!2sid!4v1668747261137!5m2!1sid!2sid"                             width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy"                             referrerpolicy="no-referrer-when-downgrade"></iframe>', '<iframe src="https://www.google.com/maps/embed?pb=!4v1668747497304!6m8!1m7!1sCAoSLEFGMVFpcE9yZktWV3NVSS1tRG82VFlGNmZJMll3QXVBdjJiSld6NGJyR3JQ!2m2!1d-7.752071!2d110.491371!3f314.63714063495473!4f-3.579420635749088!5f0.7820865974627469"                             width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"                             referrerpolicy="no-referrer-when-downgrade"></iframe>', '2022-11-19 12:58:58.045395+07', '2022-11-19 12:58:58.051408+07');


--
-- TOC entry 3578 (class 0 OID 25156)
-- Dependencies: 253
-- Data for Name: tours_image; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_image VALUES (1, 's', 'images/wendy-winarno-timeiBVLB8E-unsplash.jpg', false, 100, 100, 1, '2022-11-19 12:58:58.056406+07', '2022-11-19 12:58:58.059408+07');
INSERT INTO public.tours_image VALUES (2, 'rwet', 'images/Candi_Hindu_Prambanan_BtPlKb7.jpg', false, 100, 100, 1, '2022-11-19 12:58:58.056406+07', '2022-11-19 12:58:58.059408+07');


--
-- TOC entry 3566 (class 0 OID 16956)
-- Dependencies: 241
-- Data for Name: tours_rencanawisata; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_rencanawisata VALUES (1, '700000', 2, 'Yogyakarta', 'Malang', 'Explore Yogyakarta 2D 1N', 610000, 'Mixed', 'indonesia-4516115_1920.jpg', '2022-11-19 12:58:58.066411+07', '2022-11-19 12:58:58.07287+07');


--
-- TOC entry 3568 (class 0 OID 16962)
-- Dependencies: 243
-- Data for Name: tours_rencanawisata_akomodasi; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_rencanawisata_akomodasi VALUES (1, 1, 1);


--
-- TOC entry 3570 (class 0 OID 16968)
-- Dependencies: 245
-- Data for Name: tours_rencanawisata_destination; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_rencanawisata_destination VALUES (1, 1, 2);
INSERT INTO public.tours_rencanawisata_destination VALUES (2, 1, 8);
INSERT INTO public.tours_rencanawisata_destination VALUES (3, 1, 9);
INSERT INTO public.tours_rencanawisata_destination VALUES (4, 1, 11);
INSERT INTO public.tours_rencanawisata_destination VALUES (5, 1, 13);


--
-- TOC entry 3562 (class 0 OID 16923)
-- Dependencies: 237
-- Data for Name: tours_transportation; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_transportation VALUES (2, 'TRAIN', '08:20:00', '14:42:00', 195000, 'Malang', 'Yogyakarta', '06:22:00', 'KA Malioboro Express', '2022-11-19 12:58:58.0784+07', '2022-11-19 12:58:58.084412+07');
INSERT INTO public.tours_transportation VALUES (1, 'BUS', '07:00:00', '08:15:00', 20000, 'Malang', 'Batu', '01:15:00', 'Bus Bagong', '2022-11-19 12:58:58.0784+07', '2022-11-19 12:58:58.084412+07');
INSERT INTO public.tours_transportation VALUES (3, 'TRAIN', '20:50:01', '03:06:00', 195000, 'Yogyakarta', 'Malang', '-1 days +06:15:59', 'KA  Kertanegara', '2022-11-19 12:58:58.0784+07', '2022-11-19 12:58:58.084412+07');


--
-- TOC entry 3572 (class 0 OID 16974)
-- Dependencies: 247
-- Data for Name: tours_rencanawisata_transportasi_pergi; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_rencanawisata_transportasi_pergi VALUES (1, 1, 2);


--
-- TOC entry 3574 (class 0 OID 17040)
-- Dependencies: 249
-- Data for Name: tours_rencanawisata_transportasi_pulang; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_rencanawisata_transportasi_pulang VALUES (1, 1, 3);


--
-- TOC entry 3584 (class 0 OID 0)
-- Dependencies: 220
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- TOC entry 3585 (class 0 OID 0)
-- Dependencies: 222
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 3586 (class 0 OID 0)
-- Dependencies: 218
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 52, true);


--
-- TOC entry 3587 (class 0 OID 0)
-- Dependencies: 226
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- TOC entry 3588 (class 0 OID 0)
-- Dependencies: 224
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 2, true);


--
-- TOC entry 3589 (class 0 OID 0)
-- Dependencies: 228
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 3590 (class 0 OID 0)
-- Dependencies: 230
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 57, true);


--
-- TOC entry 3591 (class 0 OID 0)
-- Dependencies: 216
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 13, true);


--
-- TOC entry 3592 (class 0 OID 0)
-- Dependencies: 214
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 40, true);


--
-- TOC entry 3593 (class 0 OID 0)
-- Dependencies: 238
-- Name: tours_accomodation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_accomodation_id_seq', 1, true);


--
-- TOC entry 3594 (class 0 OID 0)
-- Dependencies: 234
-- Name: tours_destination_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_destination_id_seq', 13, true);


--
-- TOC entry 3595 (class 0 OID 0)
-- Dependencies: 252
-- Name: tours_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_image_id_seq', 2, true);


--
-- TOC entry 3596 (class 0 OID 0)
-- Dependencies: 250
-- Name: tours_imagealbum_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_imagealbum_id_seq', 6, true);


--
-- TOC entry 3597 (class 0 OID 0)
-- Dependencies: 242
-- Name: tours_rencanawisata_akomodasi_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_rencanawisata_akomodasi_id_seq', 1, true);


--
-- TOC entry 3598 (class 0 OID 0)
-- Dependencies: 244
-- Name: tours_rencanawisata_destination_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_rencanawisata_destination_id_seq', 5, true);


--
-- TOC entry 3599 (class 0 OID 0)
-- Dependencies: 240
-- Name: tours_rencanawisata_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_rencanawisata_id_seq', 1, true);


--
-- TOC entry 3600 (class 0 OID 0)
-- Dependencies: 246
-- Name: tours_rencanawisata_transportasi_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_rencanawisata_transportasi_id_seq', 1, true);


--
-- TOC entry 3601 (class 0 OID 0)
-- Dependencies: 248
-- Name: tours_rencanawisata_transportasi_pulang_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_rencanawisata_transportasi_pulang_id_seq', 1, true);


--
-- TOC entry 3602 (class 0 OID 0)
-- Dependencies: 236
-- Name: tours_transportation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_transportation_id_seq', 3, true);


-- Completed on 2022-11-22 09:20:10

--
-- PostgreSQL database dump complete
--

