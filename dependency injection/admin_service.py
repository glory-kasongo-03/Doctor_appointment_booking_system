from repositories.i_admin_repository import IAdminRepository
from user_account import Admin
from typing import Optional

class AdminService:
    def __init__(self, repository: IAdminRepository):
        self._repository = repository

    def register_admin(self, admin: Admin) -> None:
        self._repository.save(admin)

    def get_admin(self, admin_id: str) -> Optional[Admin]:
        return self._repository.find_by_id(admin_id)

    def list_admins(self) -> list[Admin]:
        return self._repository.find_all()

    def remove_admin(self, admin_id: str) -> None:
        self._repository.delete(admin_id)
