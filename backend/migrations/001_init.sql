-- NovaKB Initial Schema Migration
-- This creates the core tables for the NovaKB application
-- Apply this migration to your Supabase Postgres database

create extension if not exists "uuid-ossp";

-- Tenants table - represents organizations/workspaces
create table if not exists tenants (
  id uuid primary key default uuid_generate_v4(),
  name text not null,
  slug text unique not null,
  created_at timestamptz not null default now()
);

-- Users table - represents users within tenants
create table if not exists users (
  id uuid primary key default uuid_generate_v4(),
  tenant_id uuid not null references tenants(id) on delete cascade,
  email text not null,
  display_name text,
  role text not null default 'member',
  created_at timestamptz not null default now(),
  unique (tenant_id, email)
);

-- Knowledge bases table - represents collections of documents
create table if not exists knowledge_bases (
  id uuid primary key default uuid_generate_v4(),
  tenant_id uuid not null references tenants(id) on delete cascade,
  name text not null,
  description text,
  is_default boolean not null default false,
  created_at timestamptz not null default now()
);

-- Documents table - represents uploaded files
create table if not exists documents (
  id uuid primary key default uuid_generate_v4(),
  tenant_id uuid not null references tenants(id) on delete cascade,
  kb_id uuid not null references knowledge_bases(id) on delete cascade,
  filename text not null,
  storage_path text not null,
  status text not null default 'uploaded', -- uploaded | ingested | failed
  num_chunks integer not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- Chat sessions table - represents conversation sessions
create table if not exists chat_sessions (
  id uuid primary key default uuid_generate_v4(),
  tenant_id uuid not null references tenants(id) on delete cascade,
  kb_id uuid references knowledge_bases(id) on delete set null,
  title text,
  created_by_user_id uuid references users(id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- Messages table - represents individual messages in chat sessions
create table if not exists messages (
  id bigserial primary key,
  session_id uuid not null references chat_sessions(id) on delete cascade,
  sender_type text not null, -- 'user' | 'assistant' | 'system'
  content text not null,
  role text not null default 'user',
  created_at timestamptz not null default now()
);

-- Create indexes for better performance
create index if not exists idx_users_tenant_id on users(tenant_id);
create index if not exists idx_users_email on users(email);
create index if not exists idx_knowledge_bases_tenant_id on knowledge_bases(tenant_id);
create index if not exists idx_documents_tenant_id on documents(tenant_id);
create index if not exists idx_documents_kb_id on documents(kb_id);
create index if not exists idx_chat_sessions_tenant_id on chat_sessions(tenant_id);
create index if not exists idx_chat_sessions_kb_id on chat_sessions(kb_id);
create index if not exists idx_messages_session_id on messages(session_id);