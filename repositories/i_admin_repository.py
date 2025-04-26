from typing import Protocol, Optional, List
from repositories.repository_interface_design import Admin

class IAdminRepository(Protocol):
    def save(self, admin: Admin) -> None:
        ...

    def find_by_id(self, id: str) -> Optional[Admin]:
        ...

    def find_all(self) -> List[Admin]:
        ...

    def delete(self, id: str) -> None:
        ...
