import pytest
from services.admin_service import AdminService
from repositories.in_memory.admin_in_memory import InMemoryAdminRepository
from repository_interface_design import Admin

@pytest.fixture
def admin_service():
    repo = InMemoryAdminRepository()
    return AdminService(repo)

def test_add_and_get_admin(admin_service):
    admin = Admin(id="a1", name="Super Admin")
    admin_service.add_admin(admin)
    result = admin_service.get_admin("a1")
    assert result.name == "Super Admin"

def test_add_invalid_admin(admin_service):
    with pytest.raises(ValueError):
        admin_service.add_admin(Admin(id="", name=""))

def test_list_admins(admin_service):
    admin_service.add_admin(Admin(id="a1", name="Admin1"))
    admin_service.add_admin(Admin(id="a2", name="Admin2"))
    assert len(admin_service.list_admins()) == 2

def test_remove_admin(admin_service):
    admin = Admin(id="a1", name="Admin")
    admin_service.add_admin(admin)
    admin_service.remove_admin("a1")
    with pytest.raises(ValueError):
        admin_service.get_admin("a1")
