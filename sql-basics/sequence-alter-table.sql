ALTER TABLE public.users
ALTER COLUMN id
SET DEFAULT nextval('users_id_seq')
