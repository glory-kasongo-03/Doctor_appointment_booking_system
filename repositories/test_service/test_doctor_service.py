import pytest
from services.doctor_service import DoctorService
from repositories.in_memory.doctor_in_memory import InMemoryDoctorRepository
from doctor import Doctor

@pytest.fixture
def doctor_service():
    repo = InMemoryDoctorRepository()
    return DoctorService(repo)

def test_register_and_get_doctor(doctor_service):
    doc = Doctor(id="d1", name="Dr. Smith")
    doctor_service.register_doctor(doc)
    result = doctor_service.get_doctor("d1")
    assert result.name == "Dr. Smith"

def test_register_invalid_doctor(doctor_service):
    with pytest.raises(ValueError):
        doctor_service.register_doctor(Doctor(id="", name=""))

def test_list_doctors(doctor_service):
    doctor_service.register_doctor(Doctor(id="d1", name="Dr. Smith"))
    doctor_service.register_doctor(Doctor(id="d2", name="Dr. Jane"))
    doctors = doctor_service.list_doctors()
    assert len(doctors) == 2

def test_delete_doctor(doctor_service):
    doc = Doctor(id="d1", name="Dr. Smith")
    doctor_service.register_doctor(doc)
    doctor_service.delete_doctor("d1")
    with pytest.raises(ValueError):
        doctor_service.get_doctor("d1")
