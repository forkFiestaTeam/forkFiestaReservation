--
-- PostgreSQL database dump
--

-- Dumped from database version 13.10
-- Dumped by pg_dump version 13.10

-- Started on 2023-12-17 23:59:58

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

DROP DATABASE reservation_5o68;
--
-- TOC entry 2990 (class 1262 OID 41036)
-- Name: reservation_5o68; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE reservation_5o68 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Colombia.1252';


ALTER DATABASE reservation_5o68 OWNER TO postgres;

\connect reservation_5o68

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
-- TOC entry 200 (class 1259 OID 41062)
-- Name: reservation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reservation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reservation_id_seq OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 201 (class 1259 OID 41064)
-- Name: reservation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reservation (
    id integer DEFAULT nextval('public.reservation_id_seq'::regclass) NOT NULL,
    reservation_name character varying(30),
    date date,
    hour time without time zone,
    guest_number integer,
    event_type character varying(50)
);


ALTER TABLE public.reservation OWNER TO postgres;

--
-- TOC entry 2984 (class 0 OID 41064)
-- Dependencies: 201
-- Data for Name: reservation; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.reservation (id, reservation_name, date, hour, guest_number, event_type) VALUES (2, 'camilaaa', '2023-10-30', '15:30:00', 7, 'fiesttt');
INSERT INTO public.reservation (id, reservation_name, date, hour, guest_number, event_type) VALUES (3, 'Camila', '2023-11-15', '14:30:00', 5, 'Fiesta');
INSERT INTO public.reservation (id, reservation_name, date, hour, guest_number, event_type) VALUES (1, 'Cesar', '2023-10-30', '14:30:00', 4, 'holaaaaa');
INSERT INTO public.reservation (id, reservation_name, date, hour, guest_number, event_type) VALUES (4, 'Jose', '2023-11-15', '14:30:00', 5, 'Fiesta');


--
-- TOC entry 2991 (class 0 OID 0)
-- Dependencies: 200
-- Name: reservation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reservation_id_seq', 4, true);


--
-- TOC entry 2852 (class 2606 OID 41069)
-- Name: reservation reservation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservation
    ADD CONSTRAINT reservation_pkey PRIMARY KEY (id);


-- Completed on 2023-12-17 23:59:59

--
-- PostgreSQL database dump complete
--

