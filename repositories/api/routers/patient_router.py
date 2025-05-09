from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from services.patient_service import PatientService
from patient import Patient

router = APIRouter()
patient_service = PatientService()

class PatientRequest(BaseModel):
    id: str
    name: str

class PatientResponse(BaseModel):
    id: str
    name: str

@router.get("/patients", response_model=List[PatientResponse], summary="Get all patients")
def get_all_patients():
    return patient_service.get_all_patients()

@router.get("/patients/{patient_id}", response_model=Optional[PatientResponse], summary="Get a patient by ID")
def get_patient_by_id(patient_id: str):
    patient = patient_service.get_patient_by_id(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.post("/patients", response_model=PatientResponse, summary="Create a new patient")
def create_patient(patient: PatientRequest):
    return patient_service.create_patient(patient.id, patient.name)

@router.put("/patients/{patient_id}", response_model=PatientResponse, summary="Update a patient")
def update_patient(patient_id: str, patient: PatientRequest):
    updated = patient_service.update_patient(patient_id, patient.name)
    if not updated:
        raise HTTPException(status_code=404, detail="Patient not found")
    return updated

@router.delete("/patients/{patient_id}", status_code=204, summary="Delete a patient")
def delete_patient(patient_id: str):
    deleted = patient_service.delete_patient(patient_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Patient not found")
