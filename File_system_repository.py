# repositories/filesystem/file_system_repository.py

import json
import os
from typing import TypeVar, Generic, Dict, Optional, List, Type

T = TypeVar('T')  # Entity type
ID = TypeVar('ID')  # ID type

class FileSystemRepository(Generic[T, ID]):
    def __init__(self, file_path: str, entity_cls: Type[T]):
        self._file_path = file_path
        self._entity_cls = entity_cls  # Class with from_dict()

    def save(self, entity: T) -> None:
        data = self._load_all()
        data[str(entity.id)] = entity.to_dict()
        self._save_all(data)

    def find_by_id(self, entity_id: ID) -> Optional[T]:
        data = self._load_all()
        record = data.get(str(entity_id))
        return self._entity_cls.from_dict(record) if record else None

    def find_all(self) -> List[T]:
        data = self._load_all()
        return [self._entity_cls.from_dict(item) for item in data.values()]

    def delete(self, entity_id: ID) -> None:
        data = self._load_all()
        if str(entity_id) in data:
            del data[str(entity_id)]
            self._save_all(data)

    def _load_all(self) -> Dict[str, dict]:
        if not os.path.exists(self._file_path):
            return {}
        with open(self._file_path, 'r') as f:
            return json.load(f)

    def _save_all(self, data: Dict[str, dict]) -> None:
        with open(self._file_path, 'w') as f:
            json.dump(data, f, indent=4)
