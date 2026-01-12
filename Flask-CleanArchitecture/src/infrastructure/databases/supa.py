import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv() 

url: str = os.environ.get("supabase_url")
key: str = os.environ.get("supabase_key")

# Kiểm tra nếu chưa đọc được biến
if not url or not key:
    raise ValueError(f"Không tìm thấy biến môi trường! URL: {url}, Key: {key}")

supabase: Client = create_client(url, key)


def get_supabase_client() -> Client:
    return supabase