### Class Diagram
---

```mermaid
classDiagram
    class UserAccount {
        -userId: String
        -username: String
        -password: String
        -role: String
        +login()
        +logout()
        +changePassword()
    }

    class Patient {
        -patientId: String
        -name: String
        -email: String
        -phone: String
        -insuranceInfo: String
        +register()
        +bookAppointment()
        +cancelAppointment()
    }

    class Doctor {
        -doctorId: String
        -name: String
        -specialization: String
        -licenseNumber: String
        -availability: String
        +approveAppointment()
        +updateEHR()
    }

    class Appointment {
        -appointmentId: String
        -dateTime: Date
        -status: String
        -type: String
        +confirm()
        +reschedule()
        +cancel()
    }

    class EHR {
        -ehrId: String
        -medicalHistory: String
        -diagnosis: String
        -treatmentPlan: String
        +viewRecord()
        +updateRecord()
    }

    class Notification {
        -notificationId: String
        -message: String
        -status: String
        -timestamp: DateTime
        +send()
        +markAsRead()
    }

    class SystemReport {
        -reportId: String
        -type: String
        -content: String
        +generate()
        +export()
    }

    %% Relationships
    UserAccount <|-- Patient
    UserAccount <|-- Doctor
    Patient "1" --> "0..*" Appointment : books
    Doctor "1" --> "0..*" Appointment : manages
    Patient "1" --> "0..*" EHR : has
    Doctor "1" --> "0..*" EHR : creates
    Appointment "1" --> "0..*" Notification : triggers
    UserAccount "1" --> "0..*" Notification : receives
    SystemReport --> UserAccount : generatedBy

```
&nbsp;

### Key Design Decisions
---

#### Inheritance
- **Patient** and **Doctor** inherit from `UserAccount`, as both share common authentication features such as:
  - `login()`
  - `logout()`
  - `changePassword()`
- However, they also have distinct domain-specific behaviors:
  - `bookAppointment()` for **Patients**
  - `approveAppointment()` for **Doctors**

#### Association Multiplicity
- A **Patient** can book **multiple Appointments**.
- Each **Appointment** must be associated with **one Patient** and **one Doctor**.
- Each **Doctor** can create or update many **EHR (Electronic Health Record)** entries.
- Each **EHR** is associated with exactly **one Patient**.
- **Notifications** are tied to user actions (e.g., appointment changes) and are sent to relevant `UserAccount` instances (either Patients or Doctors).

#### Encapsulation
- All **attributes are private** (`-`) to enforce data encapsulation.
- Only **public methods** are exposed to allow controlled interaction with objects.

#### Modularity and Responsibility
- Each class is designed with a **single responsibility** to maintain modularity.
- For example, the `SystemReport` class is intended only for **Admins** and is **not linked** to `Appointment`, maintaining a **clear separation of concerns**.
