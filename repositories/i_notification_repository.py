from typing import Protocol, Optional, List
from repositories.repository_interface_design import Notification

class INotificationRepository(Protocol):
    def save(self, notification: Notification) -> None:
        ...

    def find_by_id(self, id: str) -> Optional[Notification]:
        ...

    def find_all(self) -> List[Notification]:
        ...

    def delete(self, id: str) -> None:
        ...
