CREATE TABLE public.videos(
id integer PRIMARY KEY,
user_id integer REFERENCES public.users,
name character varying(255) NOT NULL
)
