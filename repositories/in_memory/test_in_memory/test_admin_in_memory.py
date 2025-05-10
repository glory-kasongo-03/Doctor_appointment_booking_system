import pytest
from repositories.in_memory.admin_in_memory import InMemoryAdminRepository, Admin

@pytest.fixture
def repo():
    return InMemoryAdminRepository()

def test_save_and_find_by_id(repo):
    a = Admin(id="a1", name="Admin One")
    repo.save(a)
    assert repo.find_by_id("a1").name == "Admin One"

def test_find_all(repo):
    repo.save(Admin(id="a1", name="A"))
    repo.save(Admin(id="a2", name="B"))
    assert len(repo.find_all()) == 2

def test_delete(repo):
    repo.save(Admin(id="a1", name="Delete Me"))
    repo.delete("a1")
    assert repo.find_by_id("a1") is None
