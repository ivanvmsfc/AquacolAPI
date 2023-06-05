--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2 (Debian 15.2-1.pgdg110+1)
-- Dumped by pg_dump version 15.2

-- Started on 2023-06-05 10:14:22

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
-- TOC entry 214 (class 1259 OID 16389)
-- Name: seq_ft_inst1_data; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.seq_ft_inst1_data
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.seq_ft_inst1_data OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16390)
-- Name: ft_ins_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ft_ins_data (
    ft_ins_id bigint DEFAULT nextval('public.seq_ft_inst1_data'::regclass) NOT NULL,
    ft_ins_inst integer,
    ft_ins_timestamp bigint NOT NULL,
    ft_ins_t1 real,
    ft_ins_t2 real,
    ft_ins_ph real,
    ft_ins_o2 real,
    ft_ins_ec real,
    ft_ins_ta1 real,
    ft_ins_ha1 real,
    ft_ins_ta2 real,
    ft_ins_ha2 real,
    ft_ins_ns real,
    ft_ins_ni real
);


ALTER TABLE public.ft_ins_data OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16404)
-- Name: seq_fta_1day_inst1_data; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.seq_fta_1day_inst1_data
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.seq_fta_1day_inst1_data OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16405)
-- Name: fta_1day_ins_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fta_1day_ins_data (
    fta1d_ins_id bigint DEFAULT nextval('public.seq_fta_1day_inst1_data'::regclass) NOT NULL,
    fta1d_ins_inst integer,
    fta1d_ins_timestamp bigint NOT NULL,
    fta1d_ins_t1 real,
    fta1d_ins_t2 real,
    fta1d_ins_ph real,
    fta1d_ins_o2 real,
    fta1d_ins_ec real,
    fta1d_ins_ta1 real,
    fta1d_ins_ha1 real,
    fta1d_ins_ta2 real,
    fta1d_ins_ha2 real,
    fta1d_ins_ns real,
    fta1d_ins_ni real
);


ALTER TABLE public.fta_1day_ins_data OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16419)
-- Name: seq_fta_1hour_inst1_data; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.seq_fta_1hour_inst1_data
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.seq_fta_1hour_inst1_data OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16420)
-- Name: fta_1hour_ins_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fta_1hour_ins_data (
    fta1h_ins_id bigint DEFAULT nextval('public.seq_fta_1hour_inst1_data'::regclass) NOT NULL,
    fta1h_ins_inst integer,
    fta1h_ins_timestamp bigint NOT NULL,
    fta1h_ins_t1 real,
    fta1h_ins_t2 real,
    fta1h_ins_ph real,
    fta1h_ins_o2 real,
    fta1h_ins_ec real,
    fta1h_ins_ta1 real,
    fta1h_ins_ha1 real,
    fta1h_ins_ta2 real,
    fta1h_ins_ha2 real,
    fta1h_ins_ns real,
    fta1h_ins_ni real
);


ALTER TABLE public.fta_1hour_ins_data OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 16434)
-- Name: seq_inst_features; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.seq_inst_features
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.seq_inst_features OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 16435)
-- Name: inst_features; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.inst_features (
    ins_fea_id integer DEFAULT nextval('public.seq_inst_features'::regclass) NOT NULL,
    ins_fea_name character varying NOT NULL,
    ins_fea_desc character varying,
    ins_fea_lat real,
    ins_fea_lon real,
    ins_fea_own character varying
);


ALTER TABLE public.inst_features OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16394)
-- Name: seq_ft_inst2_data; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.seq_ft_inst2_data
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.seq_ft_inst2_data OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16399)
-- Name: seq_ft_inst3_data; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.seq_ft_inst3_data
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.seq_ft_inst3_data OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16409)
-- Name: seq_fta_1day_inst2_data; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.seq_fta_1day_inst2_data
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.seq_fta_1day_inst2_data OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16414)
-- Name: seq_fta_1day_inst3_data; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.seq_fta_1day_inst3_data
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.seq_fta_1day_inst3_data OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16424)
-- Name: seq_fta_1hour_inst2_data; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.seq_fta_1hour_inst2_data
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.seq_fta_1hour_inst2_data OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16429)
-- Name: seq_fta_1hour_inst3_data; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.seq_fta_1hour_inst3_data
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.seq_fta_1hour_inst3_data OWNER TO postgres;

--
-- TOC entry 3349 (class 0 OID 16390)
-- Dependencies: 215
-- Data for Name: ft_ins_data; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ft_ins_data (ft_ins_id, ft_ins_inst, ft_ins_timestamp, ft_ins_t1, ft_ins_t2, ft_ins_ph, ft_ins_o2, ft_ins_ec, ft_ins_ta1, ft_ins_ha1, ft_ins_ta2, ft_ins_ha2, ft_ins_ns, ft_ins_ni) FROM stdin;
26	1	0	0	0	0	0	0	0	0	0	0	\N	\N
27	1	0	0	0	0	0	0	0	0	0	0	\N	\N
28	1	0	0	0	0	0	0	0	0	0	0	\N	\N
29	1	0	0	0	0	0	0	0	0	0	0	\N	\N
23	1	0	0	0	0	0	0	0	0	0	0	\N	\N
\.


--
-- TOC entry 3353 (class 0 OID 16405)
-- Dependencies: 219
-- Data for Name: fta_1day_ins_data; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fta_1day_ins_data (fta1d_ins_id, fta1d_ins_inst, fta1d_ins_timestamp, fta1d_ins_t1, fta1d_ins_t2, fta1d_ins_ph, fta1d_ins_o2, fta1d_ins_ec, fta1d_ins_ta1, fta1d_ins_ha1, fta1d_ins_ta2, fta1d_ins_ha2, fta1d_ins_ns, fta1d_ins_ni) FROM stdin;
3	1	1	1.1	1.1	1.1	1.1	1.1	1.1	1.1	1.1	1.1	\N	\N
5	1	0	0	0	0	0	0	0	0	0	0	0	0
\.


--
-- TOC entry 3357 (class 0 OID 16420)
-- Dependencies: 223
-- Data for Name: fta_1hour_ins_data; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fta_1hour_ins_data (fta1h_ins_id, fta1h_ins_inst, fta1h_ins_timestamp, fta1h_ins_t1, fta1h_ins_t2, fta1h_ins_ph, fta1h_ins_o2, fta1h_ins_ec, fta1h_ins_ta1, fta1h_ins_ha1, fta1h_ins_ta2, fta1h_ins_ha2, fta1h_ins_ns, fta1h_ins_ni) FROM stdin;
3	1	1	1.11	1.11	1.11	1.11	1.11	1.11	1.11	1.11	1.11	\N	\N
5	2	0	0	0	0	0	0	0	0	0	0	0	0
\.


--
-- TOC entry 3361 (class 0 OID 16435)
-- Dependencies: 227
-- Data for Name: inst_features; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.inst_features (ins_fea_id, ins_fea_name, ins_fea_desc, ins_fea_lat, ins_fea_lon, ins_fea_own) FROM stdin;
1	Instalacion_1	Detalles de la inst 1	5.049344e+06	-528173.6	US
2	Instalacion_2	Detalles de la inst 2	4.60971	-74.08175	Colombia1
3	Instalacion_3	Detalles de la inst 3	4.43889	-75.23222	Colombia2
44	Instalacion de prueba	Detalles de prueba	6.6	5.6	ES Prueba
\.


--
-- TOC entry 3367 (class 0 OID 0)
-- Dependencies: 214
-- Name: seq_ft_inst1_data; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.seq_ft_inst1_data', 29, true);


--
-- TOC entry 3368 (class 0 OID 0)
-- Dependencies: 216
-- Name: seq_ft_inst2_data; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.seq_ft_inst2_data', 3, true);


--
-- TOC entry 3369 (class 0 OID 0)
-- Dependencies: 217
-- Name: seq_ft_inst3_data; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.seq_ft_inst3_data', 2, true);


--
-- TOC entry 3370 (class 0 OID 0)
-- Dependencies: 218
-- Name: seq_fta_1day_inst1_data; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.seq_fta_1day_inst1_data', 5, true);


--
-- TOC entry 3371 (class 0 OID 0)
-- Dependencies: 220
-- Name: seq_fta_1day_inst2_data; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.seq_fta_1day_inst2_data', 3, true);


--
-- TOC entry 3372 (class 0 OID 0)
-- Dependencies: 221
-- Name: seq_fta_1day_inst3_data; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.seq_fta_1day_inst3_data', 1, true);


--
-- TOC entry 3373 (class 0 OID 0)
-- Dependencies: 222
-- Name: seq_fta_1hour_inst1_data; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.seq_fta_1hour_inst1_data', 5, true);


--
-- TOC entry 3374 (class 0 OID 0)
-- Dependencies: 224
-- Name: seq_fta_1hour_inst2_data; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.seq_fta_1hour_inst2_data', 1, true);


--
-- TOC entry 3375 (class 0 OID 0)
-- Dependencies: 225
-- Name: seq_fta_1hour_inst3_data; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.seq_fta_1hour_inst3_data', 1, true);


--
-- TOC entry 3376 (class 0 OID 0)
-- Dependencies: 226
-- Name: seq_inst_features; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.seq_inst_features', 44, true);


--
-- TOC entry 3202 (class 2606 OID 16442)
-- Name: inst_features inst_features_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inst_features
    ADD CONSTRAINT inst_features_pkey PRIMARY KEY (ins_fea_id);


--
-- TOC entry 3205 (class 2606 OID 16453)
-- Name: fta_1hour_ins_data ins_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fta_1hour_ins_data
    ADD CONSTRAINT ins_id FOREIGN KEY (fta1h_ins_inst) REFERENCES public.inst_features(ins_fea_id) NOT VALID;


--
-- TOC entry 3204 (class 2606 OID 16458)
-- Name: fta_1day_ins_data ins_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fta_1day_ins_data
    ADD CONSTRAINT ins_id FOREIGN KEY (fta1d_ins_inst) REFERENCES public.inst_features(ins_fea_id) NOT VALID;


--
-- TOC entry 3203 (class 2606 OID 16473)
-- Name: ft_ins_data ins_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ft_ins_data
    ADD CONSTRAINT ins_id FOREIGN KEY (ft_ins_inst) REFERENCES public.inst_features(ins_fea_id) NOT VALID;


-- Completed on 2023-06-05 10:14:24

--
-- PostgreSQL database dump complete
--

