from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from services.notification_service import NotificationService
from notification import Notification

router = APIRouter()
notification_service = NotificationService()

class NotificationRequest(BaseModel):
    id: str
    recipient_id: str
    message: str

class NotificationResponse(BaseModel):
    id: str
    recipient_id: str
    message: str

@router.get("/notifications", response_model=List[NotificationResponse], summary="Get all notifications")
def get_all_notifications():
    return notification_service.get_all_notifications()

@router.get("/notifications/{notification_id}", response_model=Optional[NotificationResponse], summary="Get a notification by ID")
def get_notification_by_id(notification_id: str):
    notification = notification_service.get_notification_by_id(notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification

@router.post("/notifications", response_model=NotificationResponse, summary="Create a new notification")
def create_notification(notification: NotificationRequest):
    return notification_service.create_notification(notification.id, notification.recipient_id, notification.message)

@router.put("/notifications/{notification_id}", response_model=NotificationResponse, summary="Update a notification")
def update_notification(notification_id: str, notification: NotificationRequest):
    updated = notification_service.update_notification(notification_id, notification.recipient_id, notification.message)
    if not updated:
        raise HTTPException(status_code=404, detail="Notification not found")
    return updated

@router.delete("/notifications/{notification_id}", status_code=204, summary="Delete a notification")
def delete_notification(notification_id: str):
    deleted = notification_service.delete_notification(notification_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Notification not found")
