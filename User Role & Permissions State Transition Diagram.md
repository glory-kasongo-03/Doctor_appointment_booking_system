#### 6. User Role & Permissions - State Transition Diagram
```mermaid
stateDiagram
    %% Initial state
    [*] --> Role_Assigned
    Role_Assigned --> Active_Role : User Logs In
    Active_Role --> Role_Updated : Admin Changes
    Role_Updated --> Active_Role
    Active_Role --> Revoked_Role : Access Removed
    Revoked_Role --> [*]
```
