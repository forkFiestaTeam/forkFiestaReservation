PGDMP                     	    {            reservation    13.10    13.10 	    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    41036    reservation    DATABASE     j   CREATE DATABASE reservation WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Colombia.1252';
    DROP DATABASE reservation;
                postgres    false            �            1259    41062    reservation_id_seq    SEQUENCE     {   CREATE SEQUENCE public.reservation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.reservation_id_seq;
       public          postgres    false            �            1259    41064    reservation    TABLE       CREATE TABLE public.reservation (
    id integer DEFAULT nextval('public.reservation_id_seq'::regclass) NOT NULL,
    reservation_name character varying(30),
    date date,
    hour time without time zone,
    guest_number integer,
    event_type character varying(50)
);
    DROP TABLE public.reservation;
       public         heap    postgres    false    200            �          0    41064    reservation 
   TABLE DATA           a   COPY public.reservation (id, reservation_name, date, hour, guest_number, event_type) FROM stdin;
    public          postgres    false    201   3	       �           0    0    reservation_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.reservation_id_seq', 1, true);
          public          postgres    false    200            $           2606    41069    reservation reservation_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.reservation
    ADD CONSTRAINT reservation_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.reservation DROP CONSTRAINT reservation_pkey;
       public            postgres    false    201            �   <   x�3�tN-N,�4202�54�56�44�26�20�4�t-K�+�WHIU((*MMJ����� E6�     