from typing import Dict, Generic, List, Optional, TypeVar
from Repository_Interface_Design import IRepository  # Assuming you already defined this

T = TypeVar('T')
ID = TypeVar('ID')

class InMemoryRepository(IRepository[T, ID], Generic[T, ID]):
    def __init__(self):
        self._storage: Dict[ID, T] = {}

    def get_all(self) -> List[T]:
        return list(self._storage.values())

    def get_by_id(self, entity_id: ID) -> Optional[T]:
        return self._storage.get(entity_id)

    def add(self, entity: T) -> None:
        self._storage[getattr(entity, 'id')] = entity

    def update(self, entity: T) -> None:
        entity_id = getattr(entity, 'id')
        if entity_id in self._storage:
            self._storage[entity_id] = entity

    def delete(self, entity_id: ID) -> None:
        if entity_id in self._storage:
            del self._storage[entity_id]
