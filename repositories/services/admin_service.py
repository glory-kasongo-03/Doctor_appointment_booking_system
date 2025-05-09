from repositories.i_admin_repository import IAdminRepository
from repositories.repository_interface_design import Admin

class AdminService:
    def __init__(self, repository: IAdminRepository):
        self._repository = repository

    def add_admin(self, admin: Admin):
        if not admin.id or not admin.name:
            raise ValueError("Admin must have ID and name")
        self._repository.save(admin)

    def get_admin(self, admin_id: str) -> Admin:
        admin = self._repository.find_by_id(admin_id)
        if not admin:
            raise ValueError("Admin not found")
        return admin

    def list_admins(self):
        return self._repository.find_all()

    def remove_admin(self, admin_id: str):
        if not self._repository.find_by_id(admin_id):
            raise ValueError("Cannot remove non-existent admin")
        self._repository.delete(admin_id)
