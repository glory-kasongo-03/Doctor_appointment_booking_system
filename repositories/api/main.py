# main.py
# This is the main entry point for the FastAPI application.

from fastapi import FastAPI
from routers.patient_router import router as patient_router
from routers.doctor_router import router as doctor_router
from routers.appointment_router import router as appointment_router
from routers.admin_router import router as admin_router
from routers.notification_router import router as notification_router

app = FastAPI(
    title="Doctor Appointment Booking API",
    description="Manage appointments, users, and notifications.",
    version="1.0.0"
)

# Include all routers
app.include_router(patient_router, prefix="/patients", tags=["Patients"])
app.include_router(doctor_router, prefix="/doctors", tags=["Doctors"])
app.include_router(appointment_router, prefix="/appointments", tags=["Appointments"])
app.include_router(admin_router, prefix="/admins", tags=["Admins"])
app.include_router(notification_router, prefix="/notifications", tags=["Notifications"])
