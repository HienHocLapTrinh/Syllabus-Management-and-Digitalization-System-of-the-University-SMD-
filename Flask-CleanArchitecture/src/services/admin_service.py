# src/services/admin_service.py
from infrastructure.repositories.admin_repository import AdminRepository
from domain.exceptions import NotFoundException  # Từ domain/exceptions.py

class AdminService:
    def __init__(self, admin_repo: AdminRepository):
        self.admin_repo = admin_repo

    def get_all_users(self):
        users = self.admin_repo.get_all_users()
        if not users:
            raise NotFoundException("No users found")
        # Logic SMD: Filter chỉ admin role nếu cần
        return [user for user in users if user.role == 'admin']  # Giả sử User có field role