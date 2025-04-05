### Activity Diagrams

#### 1. Patient Registration Workflow
```mermaid
flowchart TD
    subgraph User
    A[Start] --> B[Fill Registration Form]
    B --> C[Submit Form]
    end
    subgraph System
    C --> D{Is Data Valid?}
    D -- No --> E[Show Error Message]
    D -- Yes --> F[Store Patient Info]
    F --> G[Send Confirmation Email]
    G --> H[End]
    end
```

#### 2. Appointment Scheduling Workflow
```mermaid
flowchart TD
    subgraph User
    A[Start] --> B[Choose Date & Time]
    end
    subgraph System
    B --> C[Check Availability]
    C --> D{Is Slot Available?}
    D -- No --> E[Show Alternative Options]
    D -- Yes --> F[Confirm Appointment]
    F --> G[Send Confirmation]
    G --> H[End]
    end
```

 #### 3. User Login Workflow
 ```mermaid
 flowchart TD
    subgraph User
    A[Start] --> B[Enter Credentials]
    end
    subgraph System
    B --> C[Validate Credentials]
    C --> D{Are credentials correct?}
    D -- No --> E[Show Error]
    D -- Yes --> F[Login Success]
    F --> G[Redirect to Dashboard]
    G --> H[End]
    end
```

#### 4. Notification Dispatch
```mermaid
flowchart TD
    subgraph System
    A[Start] --> B[Trigger Event]
    B --> C[Generate Notification]
    C --> D[Send Notification]
    D --> E[Log Status]
    E --> F[End]
    end
```

#### 5. EHR Review
```mermaid
flowchart TD
    subgraph Doctor
    A[Start] --> B[Login]
    B --> C[Select Patient]
    end
    subgraph System
    C --> D[Open EHR]
    D --> E[Review or Edit]
    E --> F[Save Changes]
    F --> G[End]
    end
```

#### 6. Role Management
```mermaid
flowchart TD
    subgraph Admin
    A[Start] --> B[Select User]
    B --> C[Assign Role]
    end
    subgraph System
    C --> D[Set Permissions]
    D --> E[Confirm Access Level]
    E --> F[End]
    end
```

#### 7. Report Generation
```mermaid
flowchart TD
    subgraph Admin
    A[Start] --> B[Select Report Type]
    end
    subgraph System
    B --> C[Fetch Data]
    C --> D[Generate Graphs]
    D --> E[Export Report]
    E --> F[End]
    end
```

#### 8. Emergency Booking
```mermaid
flowchart TD
    subgraph User
    A[Start] --> B[Mark as Emergency]
    end
    subgraph System
    B --> C[Override Availability]
    C --> D[Book Slot]
    D --> E[Send Alert]
    E --> F[End]
    end
```
