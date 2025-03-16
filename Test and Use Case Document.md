# Use Case Specifications

## 1. Register and Login

### Actor
Patient

### Preconditions
- The patient must have a valid email or phone number.
- The system must be online.

### Postconditions
- The patient is successfully registered and logged in.
- The system creates a user profile.

### Basic Flow
1. The patient enters an email or phone number.
2. The system sends an OTP to the provided contact.
3. The patient enters the OTP.
4. The system verifies the OTP and creates an account.
5. The patient is redirected to the dashboard.

### Alternative Flows
- **Invalid OTP**: If the OTP is incorrect, the system prompts the user to retry.
- **Expired OTP**: The system allows requesting a new OTP.
- **Existing User Login**: If the patient already has an account, they are directed to login.

## 2. Book Appointment

### Actor
Patient

### Preconditions
- The patient must be logged in.
- The doctor must have available slots.

### Postconditions
- The appointment is scheduled and stored in the system.
- A confirmation is sent to the patient.

### Basic Flow
1. The patient selects a preferred doctor.
2. The system displays available time slots.
3. The patient selects a date and time.
4. The system confirms availability and schedules the appointment.
5. A confirmation email/SMS is sent.

### Alternative Flows
- **No Available Slots**: The system displays an error and suggests alternative dates.
- **Technical Issues**: If booking fails, the system logs the issue and prompts the user to retry.

## 3. Cancel/Reschedule Appointment

### Actor
Patient

### Preconditions
- The patient must have a booked appointment.
- Rescheduling is allowed only before the cancellation deadline.

### Postconditions
- The appointment is either canceled or rescheduled.
- Notifications are sent to the doctor and patient.

### Basic Flow
1. The patient navigates to the appointment list.
2. The patient selects an appointment to cancel or reschedule.
3. If rescheduling, the patient selects a new time slot.
4. The system updates the appointment.
5. A confirmation is sent.
6. If cancelling, the appointment is removed.
7. the system records the cancellation.
8. Notifications are sent to the doctor and patient. 

### Alternative Flows
- **Too Late to Cancel**: If cancellation is past the deadline, the system restricts action.
- **No Available Reschedule Slots**: The system prompts the user to try another time.

## 4. Receive Appointment Reminders

### Actor
Patient

### Preconditions
- The patient must have a booked appointment.
- The system is configured for notifications.

### Postconditions
- The patient receives an SMS or email reminder.

### Basic Flow
1. 24 hours before the appointment, the system sends a reminder.
2. 1 hour before the appointment, a final reminder is sent.

### Alternative Flows
- **Patient Opts Out**: If notifications are disabled, no reminders are sent.
- **Delivery Failure**: If SMS/email fails, the system retries and logs the issue.

## 5. Manage Doctor Availability

### Actor
Doctor

### Preconditions
- The doctor must be logged in.
- The system must support schedule changes.

### Postconditions
- The updated availability is reflected in the system.

### Basic Flow
1. The doctor accesses the scheduling panel.
2. The doctor selects available and unavailable time slots.
3. The system updates the schedule.

### Alternative Flows
- **Conflicting Changes**: If availability conflicts with existing bookings, the system alerts the doctor.

## 6. View & Approve Appointments

### Actor
Doctor

### Preconditions
- The doctor must be logged in.
- There must be pending appointments.

### Postconditions
- Appointments are confirmed and scheduled.

### Basic Flow
1. The doctor navigates to the appointment dashboard.
2. The doctor reviews pending appointment requests.
3. The doctor approves or rejects the request.
4. If approved, the appointment is confirmed.
5. If rejected, the system notifies the patient.

### Alternative Flows
- **Doctor Rejects Appointment**: The patient is notified and prompted to reschedule.

## 7. Manually Book Appointment (Walk-ins)

### Actor
Hospital Receptionist

### Preconditions
- The receptionist must have receptionist privileges.
- The doctor must have available slots.

### Postconditions
- The appointment is stored in the system.
- A confirmation is sent to the patient.

### Basic Flow
1. The receptionist searches for the patient’s profile or creates a new one.
2. The receptionist selects a doctor and time slot.
3. The system confirms the appointment.
4. A confirmation message is sent.

### Alternative Flows
- **No Available Slots**: The system suggests alternative dates.
- **Duplicate Booking**: If the patient already has an appointment, a warning is displayed.

## 8. Generate Reports

### Actor
Administrator

### Preconditions
- The user must be an administrator.
- There must be sufficient data in the system.

### Postconditions
- Reports are generated and displayed.

### Basic Flow
1. The administrator selects the report type.
2. The system retrieves and processes data.
3. The report is displayed and can be exported.

### Alternative Flows
- **No Data Available**: The system displays an error message.
- **Large Dataset**: The system takes extra processing time and notifies the user.

&nbsp;

# Test Cases

## Functional Requirements Test Cases

| Test ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status |
|---------|---------------|-------------|-------|----------------|---------------|--------|
| TC1 | FR1 | Verify patient registration and authentication | 1. Navigate to the registration page. 2. Enter valid details. 3. Submit form. 4. Try logging in. | Patient is registered and can log in successfully. |...|...|
| TC2 | FR2 | Validate appointment scheduling | 1. Log in as a patient. 2. Select a doctor and available slot. 3. Confirm appointment. | Appointment is scheduled successfully. |...|...|
| TC3 | FR3 | Verify automated appointment reminders | 1. Schedule an appointment. 2. Wait for the reminder time. | Patient receives a reminder via email/SMS. |...|...|
| TC4 | FR4 | Validate rescheduling & cancellation | 1. Log in as a patient. 2. Navigate to existing appointment. 3. Reschedule or cancel appointment. | Appointment is updated or cancelled successfully. |...|...|
| TC5 | FR5 | Test non-attendance tracking & penalties | 1. Schedule an appointment. 2. Do not attend. 3. Check penalty application. | Penalty is applied as per policy. |...|...|
| TC6 | FR6 | Ensure secure patient data storage & compliance | 1. Access patient records as an unauthorized user. 2. Attempt to modify records. | Unauthorized access is denied. |...|...|
| TC7 | FR7 | Verify doctor’s schedule management dashboard | 1. Log in as a doctor. 2. Check appointment dashboard. 3. Modify availability. | Dashboard shows correct schedule, modifications saved. |...|...|
| TC8 | FR8 | Validate emergency & priority booking | 1. Log in as a patient. 2. Try booking an emergency appointment. 3. Confirm priority status. | Emergency appointment is successfully created. |...|...|
| TC9 | FR9 | Verify multi-channel booking (web & mobile) | 1. Attempt appointment booking via web. 2. Attempt via mobile app. | Appointments can be booked through both platforms. |...|...|
| TC10 | FR10 | Validate clinic performance reports & analytics | 1. Log in as a healthcare admin. 2. Navigate to reports. 3. Generate performance analytics. | Reports are generated accurately. |...|...|
| TC11 | FR11 | Ensure integration with Electronic Health Records (EHR) | 1. Log in as a doctor. 2. Access a patient's medical history from EHR. | Patient’s history is accessible from EHR system. |...|...|
| TC12 | FR12 | Validate user role & permissions management | 1. Log in as an IT admin. 2. Assign roles to users. 3. Validate access permissions. | Roles & permissions are enforced correctly. |...|...|

&nbsp;

## Non-Functional Requirements Test Cases

#### NFR1.1 - Intuitive User Interface
- **Scenario**: Verify the ease of navigation and usability.
- **Steps**: Perform usability testing with end users, track ease of completing tasks.
- **Expected Result**: Users can easily navigate the system without confusion.

#### NFR2.1 - Cloud & On-Premise Deployment
- **Scenario**: Test system deployment on both cloud and on-premise environments.
- **Steps**: Deploy application in both environments and validate feature consistency.
- **Expected Result**: Application works seamlessly in both setups.

#### NFR5.2 - Role-Based Access Control (RBAC)

- **Scenario**: Validate that users can only access features according to their assigned roles.

- **Steps**: Log in as different user roles (Doctor, Patient, Admin) and attempt unauthorized actions.

- **Expected Result**: Access is restricted based on roles, unauthorized actions are denied.

#### NFR6.1 - Fast Response Time
- **Scenario**: Measure system response time for different operations.
- **Steps**: Perform actions like login, booking, and report generation while logging response times.
- **Expected Result**: System response remains under the acceptable threshold (< 3 sec).

