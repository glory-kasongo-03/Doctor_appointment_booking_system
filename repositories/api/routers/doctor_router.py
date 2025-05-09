from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from services.doctor_service import DoctorService
from doctor import Doctor

router = APIRouter()
doctor_service = DoctorService()

class DoctorRequest(BaseModel):
    id: str
    name: str

class DoctorResponse(BaseModel):
    id: str
    name: str

@router.get("/doctors", response_model=List[DoctorResponse], summary="Get all doctors")
def get_all_doctors():
    return doctor_service.get_all_doctors()

@router.get("/doctors/{doctor_id}", response_model=Optional[DoctorResponse], summary="Get a doctor by ID")
def get_doctor_by_id(doctor_id: str):
    doctor = doctor_service.get_doctor_by_id(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@router.post("/doctors", response_model=DoctorResponse, summary="Create a new doctor")
def create_doctor(doctor: DoctorRequest):
    return doctor_service.create_doctor(doctor.id, doctor.name)

@router.put("/doctors/{doctor_id}", response_model=DoctorResponse, summary="Update a doctor")
def update_doctor(doctor_id: str, doctor: DoctorRequest):
    updated = doctor_service.update_doctor(doctor_id, doctor.name)
    if not updated:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return updated

@router.delete("/doctors/{doctor_id}", status_code=204, summary="Delete a doctor")
def delete_doctor(doctor_id: str):
    deleted = doctor_service.delete_doctor(doctor_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Doctor not found")
