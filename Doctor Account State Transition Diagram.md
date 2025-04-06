#### 2. Doctor Account - State Transition Diagram
```mermaid
stateDiagram-v2
    %% Initial state
    [*] --> Registered_Doctor
    Registered_Doctor --> Verified_Doctor : License Approved
    Verified_Doctor --> Active_Doctor : Admin Activation
    Active_Doctor --> Suspended_Doctor : Misconduct
    Suspended_Doctor --> Active_Doctor : Cleared
    Active_Doctor --> Deactivated_Doctor : Voluntary Exit
    Deactivated_Doctor --> [*]
```
