from repositories.IAdminRepository import IAdminRepository
from user_account import Admin
from typing import Optional

class InMemoryAdminRepository(IAdminRepository):
    def __init__(self):
        self._admins: dict[str, Admin] = {}

    def save(self, admin: Admin) -> None:
        self._admins[admin.id] = admin

    def find_by_id(self, admin_id: str) -> Optional[Admin]:
        return self._admins.get(admin_id)

    def find_all(self) -> list[Admin]:
        return list(self._admins.values())

    def delete(self, admin_id: str) -> None:
        self._admins.pop(admin_id, None)
