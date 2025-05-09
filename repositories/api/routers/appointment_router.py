from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from services.appointment_service import AppointmentService
from appointment import Appointment

router = APIRouter()
appointment_service = AppointmentService()

class AppointmentRequest(BaseModel):
    id: str
    patient_id: str
    doctor_id: str
    date: str

class AppointmentResponse(BaseModel):
    id: str
    patient_id: str
    doctor_id: str
    date: str

@router.get("/appointments", response_model=List[AppointmentResponse], summary="Get all appointments")
def get_all_appointments():
    return appointment_service.get_all_appointments()

@router.get("/appointments/{appointment_id}", response_model=Optional[AppointmentResponse], summary="Get an appointment by ID")
def get_appointment_by_id(appointment_id: str):
    appointment = appointment_service.get_appointment_by_id(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

@router.post("/appointments", response_model=AppointmentResponse, summary="Create a new appointment")
def create_appointment(appointment: AppointmentRequest):
    return appointment_service.create_appointment(appointment.id, appointment.patient_id, appointment.doctor_id, appointment.date)

@router.put("/appointments/{appointment_id}", response_model=AppointmentResponse, summary="Update an appointment")
def update_appointment(appointment_id: str, appointment: AppointmentRequest):
    updated = appointment_service.update_appointment(appointment_id, appointment.patient_id, appointment.doctor_id, appointment.date)
    if not updated:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return updated

@router.delete("/appointments/{appointment_id}", status_code=204, summary="Delete an appointment")
def delete_appointment(appointment_id: str):
    deleted = appointment_service.delete_appointment(appointment_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Appointment not found")
