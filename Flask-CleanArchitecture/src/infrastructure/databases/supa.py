import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv() 

url: str = os.environ.get("supabase_url")
key: str = os.environ.get("supabase_key")


supabase: Client = create_client(url, key)

class SupabaseDatabase:
    def __init__(self):
        self.client = supabase

    def init_database(self, app):
        # Thực hiện các cấu hình liên quan đến Flask app nếu cần
        # Nếu không cần làm gì, chỉ cần để 'pass'
        print("Supabase initialized with Flask App")
        pass

def get_supabase_client():
    return SupabaseDatabase()