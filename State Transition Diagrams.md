### State Transitions Diagrams

#### 1. Patient Account - State Transition Diagram
```mermaid
stateDiagram-v2
    [*] --> Registered
    Registered --> Active : Email Verified
    Active --> Suspended : Admin Action
    Suspended --> Active : Reinstated
    Active --> Deleted : User Request
    Deleted --> [*]
```

#### 2. Doctor Account - State Transition Diagram
```mermaid
stateDiagram-v2
    [*] --> Registered
    Registered --> Verified : License Approved
    Verified --> Active : Admin Activation
    Active --> Suspended : Misconduct
    Suspended --> Active : Cleared
    Active --> Deactivated : Voluntary Exit
    Deactivated --> [*]
```

#### 3. Appointment - State Transition Diagram
```mermaid
stateDiagram-v2
    [*] --> Requested
    Requested --> Confirmed : Slot Available
    Confirmed --> Attended : Patient Attends
    Confirmed --> Missed : No-show
    Confirmed --> Cancelled : Patient/Doctor Cancels
    Cancelled --> [*]
    Missed --> [*]
    Attended --> [*]
```

####  4. Notification - State Transition Diagram
```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Sent : Trigger Event
    Sent --> Read : Opened by User
    Sent --> Failed : Delivery Error
    Read --> Archived
    Failed --> Archived
    Archived --> [*]
```

#### 5. EHR - State Transition Diagram
```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Reviewed : Doctor Accesses
    Reviewed --> Updated : Doctor Edits
    Updated --> Archived : Patient Discharged
    Archived --> [*]
```

#### 6. User Role & Permissions - State Transition Diagram
```mermaid
stateDiagram-v2
    [*] --> Role_Assigned
    Role_Assigned --> Active : User Logs In
    Active --> Role_Updated : Admin Changes
    Role_Updated --> Active
    Active --> Revoked : Access Removed
    Revoked --> [*]
```

#### 7. System Report - State Transition Diagram
```mermaid
stateDiagram-v2
    [*] --> Scheduled
    Scheduled --> Generated : Time Trigger
    Generated --> Reviewed : Admin Opens
    Reviewed --> Archived
    Archived --> [*]
```

#### 8. Emergency Booking - State Transition Diagram
```mermaid
stateDiagram-v2
    [*] --> Initiated
    Initiated --> Confirmed : Slot Override
    Confirmed --> Attended : Emergency Visit
    Confirmed --> Cancelled : Not Needed
    Attended --> [*]
    Cancelled --> [*]
```
