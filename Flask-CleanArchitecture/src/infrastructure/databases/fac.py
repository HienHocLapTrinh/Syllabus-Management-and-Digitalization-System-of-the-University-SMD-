from infrastructure.databases.supa import get_supabase_client

class FactoryDatabase:
    @staticmethod
    def get_database(database_type)-> get_supabase_client:
        if database_type == 'SUPABASE':
            return get_supabase_client()
        raise ValueError(f"Unsupported database type: {database_type}")