# Database Migrations

This directory contains SQL migration files for the NovaKB application.

## Applying Migrations

Migrations should be applied manually to your Supabase Postgres database using one of the following methods:

### Method 1: Supabase SQL Editor
1. Open your Supabase project dashboard
2. Navigate to the SQL Editor
3. Copy and paste the contents of the migration file
4. Execute the SQL

### Method 2: psql Command Line
```bash
# Set your connection string in .env first
psql "$SUPABASE_DB_CONNECTION_STRING" -f backend/migrations/001_init.sql
```

## Migration Files

- `001_init.sql` - Initial schema with core tables (tenants, users, knowledge_bases, documents, chat_sessions, messages)

## Future Migrations

Additional migration files should be numbered sequentially (002_*, 003_*, etc.) and applied in order.