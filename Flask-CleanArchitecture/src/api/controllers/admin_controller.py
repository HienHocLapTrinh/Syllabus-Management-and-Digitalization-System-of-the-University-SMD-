from flask import Blueprint, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView  # Nếu dùng SQLAlchemy mix Supabase
from services.admin_service import AdminService  # Mới: Service cho admin logic
from infrastructure.repositories.admin_repository import AdminRepository
from infrastructure.databases.supa import get_supabase_client

admin_bp = Blueprint('smd_admin', __name__, url_prefix='/admin', template_folder='../../views')  # Link đến src/views

admin_repo = AdminRepository(get_supabase_client())
admin_service = AdminService(admin_repo)


# route home
@admin_bp.route('/')
@admin_bp.route('/home')
def admin_home():
    users = admin_service.get_all_users() or [] # từ Supabase
    return render_template('admin/home_ad.html', users=users)

class UserAdminView(ModelView):
    column_list = ['id', 'username', 'email', 'role']  # Custom columns cho SMD
    form_columns = ['username', 'email', 'role']  # Form fields
