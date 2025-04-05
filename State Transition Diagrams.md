### State Transitions Diagrams
```mermaid
%% 1. Patient Account - State Transition Diagram
stateDiagram
    %% Initial state
    [*] --> Registered_Patient
    Registered_Patient --> Active_Patient : Email Verified
    Active_Patient --> Suspended_Patient : Admin Action
    Suspended_Patient --> Active_Patient : Reinstated
    Active_Patient --> Deleted_Patient : User Request
    Deleted_Patient --> [*]
```

%% 2. Doctor Account - State Transition Diagram
```mermaid
stateDiagram
    %% Initial state
    [*] --> Registered_Doctor
    Registered_Doctor --> Verified_Doctor : License Approved
    Verified_Doctor --> Active_Doctor : Admin Activation
    Active_Doctor --> Suspended_Doctor : Misconduct
    Suspended_Doctor --> Active_Doctor : Cleared
    Active_Doctor --> Deactivated_Doctor : Voluntary Exit
    Deactivated_Doctor --> [*]
```

%% 3. Appointment - State Transition Diagram
```mermaid
stateDiagram-v2
    %% Initial state
    [*] --> Requested_Appointment
    Requested_Appointment --> Confirmed_Appointment : Slot Available
    Confirmed_Appointment --> Attended_Appointment : Patient Attends
    Confirmed_Appointment --> Missed_Appointment : No-show
    Confirmed_Appointment --> Cancelled_Appointment : Patient/Doctor Cancels
    Cancelled_Appointment --> [*]
    Missed_Appointment --> [*]
    Attended_Appointment --> [*]
```

%% 4. Notification - State Transition Diagram
```mermaid
stateDiagram-v2
    %% Initial state
    [*] --> Created_Notification
    Created_Notification --> Sent_Notification : Trigger Event
    Sent_Notification --> Read_Notification : Opened by User
    Sent_Notification --> Failed_Notification : Delivery Error
    Read_Notification --> Archived_Notification
    Failed_Notification --> Archived_Notification
    Archived_Notification --> [*]
```

%% 5. Electronic Health Record (EHR) State Transition Diagram
```mermaid
stateDiagram-v2
    %% Initial state
    [*] --> Created_EHR
    Created_EHR --> Reviewed_EHR : Doctor Accesses
    Reviewed_EHR --> Updated_EHR : Doctor Edits
    Updated_EHR --> Archived_EHR : Patient Discharged
    Archived_EHR --> [*]
```

%% 6. User Role & Permissions - State Transition Diagram
```mermaid
stateDiagram-v2
    %% Initial state
    [*] --> Role_Assigned
    Role_Assigned --> Active_Role : User Logs In
    Active_Role --> Role_Updated : Admin Changes
    Role_Updated --> Active_Role
    Active_Role --> Revoked_Role : Access Removed
    Revoked_Role --> [*]
```

%% 7. System Report - State Transition Diagram
```mermaid
stateDiagram-v2
    %% Initial state
    [*] --> Scheduled_Report
    Scheduled_Report --> Generated_Report : Time Trigger
    Generated_Report --> Reviewed_Report : Admin Opens
    Reviewed_Report --> Archived_Report
    Archived_Report --> [*]
```

%% 8. Emergency Booking - State Transition Diagram
```mermaid
stateDiagram-v2
    %% Initial state
    [*] --> Initiated_Booking
    Initiated_Booking --> Confirmed_Booking : Slot Override
    Confirmed_Booking --> Attended_Booking : Emergency Visit
    Confirmed_Booking --> Cancelled_Booking : Not Needed
    Attended_Booking --> [*]
    Cancelled_Booking --> [*]
```
