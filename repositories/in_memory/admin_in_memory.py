from typing import Dict
from repositories.i_admin_repository import IAdminRepository, Admin

class InMemoryAdminRepository(IAdminRepository):
    def __init__(self):
        self._admins: Dict[str, Admin] = {}

    def save(self, admin: Admin) -> None:
        self._admins[admin.id] = admin

    def find_by_id(self, id: str) -> Admin:
        return self._admins.get(id)

    def find_all(self) -> list[Admin]:
        return list(self._admins.values())

    def delete(self, id: str) -> None:
        if id in self._admins:
            del self._admins[id]
