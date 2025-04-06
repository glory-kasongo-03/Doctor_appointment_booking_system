#### 8. Emergency Booking - State Transition Diagram
```mermaid
stateDiagram
    %% Initial state
    [*] --> Initiated_Booking
    Initiated_Booking --> Confirmed_Booking : Slot Override
    Confirmed_Booking --> Attended_Booking : Emergency Visit
    Confirmed_Booking --> Cancelled_Booking : Not Needed
    Attended_Booking --> [*]
    Cancelled_Booking --> [*]
```
