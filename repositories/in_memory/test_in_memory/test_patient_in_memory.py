import pytest
from repositories.in_memory.patient_in_memory import InMemoryPatientRepository
from patient import Patient

@pytest.fixture
def patient_repo():
    return InMemoryPatientRepository()

def test_save_and_find_by_id(patient_repo):
    patient = Patient(id="p1", name="Alice")
    patient_repo.save(patient)
    result = patient_repo.find_by_id("p1")
    assert result is not None
    assert result.id == "p1"
    assert result.name == "Alice"

def test_find_all(patient_repo):
    patient1 = Patient(id="p1", name="Alice")
    patient2 = Patient(id="p2", name="Bob")
    patient_repo.save(patient1)
    patient_repo.save(patient2)
    results = patient_repo.find_all()
    assert len(results) == 2

def test_delete(patient_repo):
    patient = Patient(id="p1", name="Alice")
    patient_repo.save(patient)
    patient_repo.delete("p1")
    result = patient_repo.find_by_id("p1")
    assert result is None
