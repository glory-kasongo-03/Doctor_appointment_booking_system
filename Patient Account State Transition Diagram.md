#### 1. Patient Account - State Transition Diagram
```mermaid
stateDiagram-v2
    %% Initial state
    [*] --> Registered_Patient
    Registered_Patient --> Active_Patient : Email Verified
    Active_Patient --> Suspended_Patient : Admin Action
    Suspended_Patient --> Active_Patient : Reinstated
    Active_Patient --> Deleted_Patient : User Request
    Deleted_Patient --> [*]
```
