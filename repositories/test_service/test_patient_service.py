import pytest
from services.patient_service import PatientService
from patient import Patient

@pytest.fixture
def patient_service():
    return PatientService()

def test_create_patient(patient_service):
    patient = patient_service.create_patient("p1", "Alice")
    assert isinstance(patient, Patient)
    assert patient.id == "p1"
    assert patient.name == "Alice"

def test_get_patient_by_id(patient_service):
    patient_service.create_patient("p1", "Alice")
    result = patient_service.get_patient_by_id("p1")
    assert result is not None
    assert result.id == "p1"

def test_get_all_patients(patient_service):
    patient_service.create_patient("p1", "Alice")
    patient_service.create_patient("p2", "Bob")
    patients = patient_service.get_all_patients()
    assert len(patients) == 2

def test_update_patient(patient_service):
    patient_service.create_patient("p1", "Alice")
    updated = patient_service.update_patient("p1", "Alicia")
    assert updated is not None
    assert updated.name == "Alicia"

def test_delete_patient(patient_service):
    patient_service.create_patient("p1", "Alice")
    deleted = patient_service.delete_patient("p1")
    assert deleted is True
    assert patient_service.get_patient_by_id("p1") is None
