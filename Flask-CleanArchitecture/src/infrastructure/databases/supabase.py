import os
from supabase import create_client, Client

url: str = os.environ.get("https://jednbjdohmtdxegcgunq.supabase.co")
key: str = os.environ.get("sb_publishable_3vVjdXA9o9FSj03zZHI60A_ySK6lSnh")
supabase: Client = create_client(url, key)

def get_supabase_client() -> Client:
    return supabase #xuat ra mot client de su dung

# ORM: object relational mapping base class
# OOP : object oriented programming

# ERD --> class relational
# Lập trinhf hướng đối tượng (logic) mapping class -> table (database)