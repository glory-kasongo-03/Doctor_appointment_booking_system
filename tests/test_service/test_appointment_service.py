import pytest
from services.appointment_service import AppointmentService
from repositories.in_memory.appointment_in_memory import InMemoryAppointmentRepository
from repositories.in_memory.patient_in_memory import InMemoryPatientRepository
from repositories.in_memory.doctor_in_memory import InMemoryDoctorRepository
from appointment import Appointment
from patient import Patient
from doctor import Doctor

@pytest.fixture
def appointment_service():
    patient_repo = InMemoryPatientRepository()
    doctor_repo = InMemoryDoctorRepository()
    appointment_repo = InMemoryAppointmentRepository()
    patient_repo.save(Patient(id="p1", name="Alice"))
    doctor_repo.save(Doctor(id="d1", name="Dr. Smith"))
    return AppointmentService(appointment_repo, patient_repo, doctor_repo)

def test_book_and_get_appointment(appointment_service):
    appt = Appointment(id="a1", patient_id="p1", doctor_id="d1")
    appointment_service.book_appointment(appt)
    result = appointment_service.get_appointment("a1")
    assert result.patient_id == "p1"

def test_book_invalid_patient(appointment_service):
    appt = Appointment(id="a2", patient_id="invalid", doctor_id="d1")
    with pytest.raises(ValueError):
        appointment_service.book_appointment(appt)

def test_patient_appointment_limit(appointment_service):
    for i in range(5):
        appt = Appointment(id=f"a{i}", patient_id="p1", doctor_id="d1")
        appointment_service.book_appointment(appt)
    with pytest.raises(ValueError):
        appointment_service.book_appointment(Appointment(id="a6", patient_id="p1", doctor_id="d1"))
