# src/infrastructure/repositories/admin_repository.py
from infrastructure.databases.supa import get_supabase_client  # Supabase client từ base.py
from domain.models.user import User  # Domain model (nếu có, hoặc dùng dict)

class AdminRepository:
    def __init__(self, supabase_client):
        self.supabase = supabase_client

    def get_all_users(self):
        """Query all users from Supabase"""
        try:
            response = self.supabase.from_('users').select('*').execute()

            if hasattr(response, 'data') and response.data:
                return response.data  # list of dicts
            else:
                print("No data or error:", response)
                return []
        except Exception as e:
            print("Supabase query error:", str(e))
            return []

    # Thêm methods khác: get_syllabi, etc., cho SMD