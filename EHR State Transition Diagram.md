#### 5. Electronic Health Record (EHR) State Transition Diagram
```mermaid
stateDiagram
    %% Initial state
    [*] --> Created_EHR
    Created_EHR --> Reviewed_EHR : Doctor Accesses
    Reviewed_EHR --> Updated_EHR : Doctor Edits
    Updated_EHR --> Archived_EHR : Patient Discharged
    Archived_EHR --> [*]
```
