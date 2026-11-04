-- =========================================================
-- FORMAÇÃO COMERCIAL HI — PROGRESSO DOS COLABORADORES DE VENDAS
-- Usa o MESMO projeto Supabase do site do suporte (Forma-o-HI):
-- mesmo login (auth.users) e mesma tabela de ADMs (admins).
-- Só o progresso é separado, na tabela progresso_vendas.
--
-- Rodar uma vez: SQL Editor → New query → colar → Run.
-- Pode rodar mesmo que o SQL do suporte já tenha rodado
-- (tudo é "if not exists" / "or replace").
-- Usado por Assets/conta.js (alunos) e Assets/admin.html (painel ADM).
-- =========================================================

-- Progresso de cada colaborador de vendas (uma linha por conta)
create table if not exists public.progresso_vendas (
    user_id       uuid primary key references auth.users (id) on delete cascade,
    nome          text not null,
    email         text,
    etapas        integer[] not null default '{}',
    ultima_etapa  integer check (ultima_etapa between 1 and 10),
    ultimo_acesso timestamptz not null default now(),
    criado_em     timestamptz not null default now()
);

-- Tabela de ADMs: compartilhada com o site do suporte.
-- Quem já é ADM lá também vê o painel de vendas.
create table if not exists public.admins (
    user_id uuid primary key references auth.users (id) on delete cascade
);

alter table public.progresso_vendas enable row level security;
alter table public.admins           enable row level security;

-- true se quem está logado é ADM (mesma função do SQL do suporte)
create or replace function public.eh_admin()
returns boolean
language sql
stable
security definer
set search_path = public
as $$
    select exists (select 1 from public.admins where user_id = auth.uid());
$$;

-- Regras de acesso (RLS)
drop policy if exists "progresso_vendas: ler o proprio ou admin" on public.progresso_vendas;
create policy "progresso_vendas: ler o proprio ou admin"
    on public.progresso_vendas for select to authenticated
    using (user_id = auth.uid() or public.eh_admin());

drop policy if exists "progresso_vendas: criar o proprio" on public.progresso_vendas;
create policy "progresso_vendas: criar o proprio"
    on public.progresso_vendas for insert to authenticated
    with check (user_id = auth.uid());

drop policy if exists "progresso_vendas: alterar o proprio" on public.progresso_vendas;
create policy "progresso_vendas: alterar o proprio"
    on public.progresso_vendas for update to authenticated
    using (user_id = auth.uid())
    with check (user_id = auth.uid());

drop policy if exists "admins: ver a propria linha" on public.admins;
create policy "admins: ver a propria linha"
    on public.admins for select to authenticated
    using (user_id = auth.uid());

-- Permissões da API (usuário logado; visitante sem login não acessa nada)
revoke all on public.progresso_vendas from anon;
revoke all on public.admins           from anon;
grant select, insert, update on public.progresso_vendas to authenticated;
grant select                 on public.admins           to authenticated;
grant execute on function public.eh_admin() to authenticated;


-- =========================================================
-- ADM: quem já é ADM no site do suporte não precisa de nada.
-- Para um ADM novo, DEPOIS de ele criar a conta pelo site,
-- rode só a linha abaixo (trocando o e-mail):
--
-- insert into public.admins (user_id)
-- select id from auth.users where email = 'seu.email@exemplo.com';
-- =========================================================
