from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from services.admin_service import AdminService
from repository_interface_design import Admin

router = APIRouter()
admin_service = AdminService()

class AdminRequest(BaseModel):
    id: str
    name: str

class AdminResponse(BaseModel):
    id: str
    name: str

@router.get("/admins", response_model=List[AdminResponse], summary="Get all admins")
def get_all_admins():
    return admin_service.get_all_admins()

@router.get("/admins/{admin_id}", response_model=Optional[AdminResponse], summary="Get an admin by ID")
def get_admin_by_id(admin_id: str):
    admin = admin_service.get_admin_by_id(admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    return admin

@router.post("/admins", response_model=AdminResponse, summary="Create a new admin")
def create_admin(admin: AdminRequest):
    return admin_service.create_admin(admin.id, admin.name)

@router.put("/admins/{admin_id}", response_model=AdminResponse, summary="Update an admin")
def update_admin(admin_id: str, admin: AdminRequest):
    updated = admin_service.update_admin(admin_id, admin.name)
    if not updated:
        raise HTTPException(status_code=404, detail="Admin not found")
    return updated

@router.delete("/admins/{admin_id}", status_code=204, summary="Delete an admin")
def delete_admin(admin_id: str):
    deleted = admin_service.delete_admin(admin_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Admin not found")
