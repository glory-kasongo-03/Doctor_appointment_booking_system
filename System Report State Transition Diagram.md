#### 7. System Report - State Transition Diagram
```mermaid
stateDiagram
    %% Initial state
    [*] --> Scheduled_Report
    Scheduled_Report --> Generated_Report : Time Trigger
    Generated_Report --> Reviewed_Report : Admin Opens
    Reviewed_Report --> Archived_Report
    Archived_Report --> [*]
```
