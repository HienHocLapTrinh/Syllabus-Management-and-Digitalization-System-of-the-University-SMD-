from infrastructure.databases.fac import FactoryDatabase
# from infrastructure.databases.mssql import init_mssql
# from infrastructure.databases.postgres import init_postgres
from infrastructure.models import course_register_model, todo_model, user_model, course_model, consultant_model, appointment_model, program_model, feedback_model,survey_model
from infrastructure.models.auth import auth_user_model, auth_role_model,auth_funtion_model
from infrastructure.models.sell import sell_customer_model, sell_product_model, sell_invoice_model

def init_db(app):
    # init_supabase(app)
    FactoryDatabase.get_database('SUPABASE').init_database(app)
    
# Migration Entities -> tables
from infrastructure.databases.supa import get_supabase_client