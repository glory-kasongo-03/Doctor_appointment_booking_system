# Project Title

Doctor Appointment Booking System

## Project Description

This is a basic doctor appointment booking system, a web and mobile-based app allowing patients to schedule medical appointments online, manage bookings, and receive reminders. Doctors will use the system to manage their different schedules; hospital administrators will be able to monitor appointment statistics and optimize scheduling efficiency. A notification service will be included to remind patients about upcoming appointments.

### Getting Started

#### Prerequisites

- Python 3.10 or higher
- `pip` (Python package manager)
- `git`
- A GitHub account

#### Installation

```bash
git clone https://github.com/your-username/doctor-appointment-booking.git
cd doctor-appointment-booking
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Features for Contribution

| Feature                          | Status     | Contribution Guide       | Label       |
|----------------------------------|------------|---------------------------|------------|
| Integrate Redis for caching doctor availability| Planned | Open Issue     | Enhancement    |
| Support optional email reminders for patients  | Planned | Open Issue     | Enhancement    |
| Add appointment filtering by date and doctor   | Planned | Open Issue     | Enhancement    |
| Improve formatting in README.md                | Planned | Open Issue     | Good First Issue     |
| Add 404 handler for unknown routes             | Planned | Open Issue     | Good First Issue     |
| Fix typo in error message for doctor login failure  | Planned | Open Issue     | Good First Issue     |
| Add unit tests for NotificationService               | Planned | Open Issue     | Good First Issue     |
| Add docstrings to all service methods             | Planned | Open Issue     | Good First Issue      |

### Justification for Repository Interface Design

- **Use of Generics**: Avoids duplication across entity repositories by abstracting common CRUD operations into the `IRepository` interface, reducing repetitive code.
- **Entity-Specific Interfaces**: Allows for specialized queries, such as `find_by_email()` in `IPatientRepository` or `find_by_specialization()` in `IDoctorRepository`.
- **Adherence to SOLID Principles**:
  - Promotes the **Interface Segregation Principle** by ensuring interfaces are specific to the needs of each entity.
  - Encourages the **Dependency Inversion Principle** by making components depend on abstractions rather than concrete implementations.
- **Testability and Flexibility**: Enhances the testability of the data layer, making it easier to perform unit testing and mocking in services.

### Dependency Injection VS Factory Pattern

### Why Dependency Injection (DI) Over Factory Pattern?

#### Dependency Injection Advantages

- **Highly Testable**: Easily inject mocks or stubs during unit testing.
- **Separation of Concerns**: Services depend on abstractions rather than specific implementations.
- **Explicit and Flexible**: Particularly useful when working with multiple implementations (e.g., in-memory, database, cache).
- **Framework Compatibility**: Works seamlessly with frameworks like FastAPI, Django, and Flask (with DI extensions).

#### Factory Pattern Trade-offs

- **Dynamic Instantiation**: Useful for creating multiple variants dynamically.
- **Hidden Dependencies**: Can obscure dependencies, making unit testing more challenging.
- **Potential Tight Coupling**: May lead to tightly coupled code if not carefully managed.

### Justification for Each Pattern

#### Simple Factory

- **Use Case**: Centralized creation of different user roles like Patient, Doctor, Admin.
- **Why**: Simplifies user creation logic and isolates instantiation.

#### Factory Method

- **Use Case**: Sending notifications via different channels (Email, SMS).
- **Why**: Allows flexibility to extend new notification types without changing the core logic.

#### Abstract Factory

- **Use Case**: Rendering UI components (e.g., buttons) depending on platform (Web or Mobile).
- **Why**: Ensures consistent UI elements across platforms.

#### Builder

- **Use Case**: Constructing complex Appointment objects step-by-step.
- **Why**: Enhances clarity and flexibility when creating appointments with multiple fields.

#### Prototype

- **Use Case**: Quickly duplicating report templates for different users.
- **Why**: Avoids costly re-creation and ensures performance.

#### Singleton

- **Use Case**: DatabaseConnection for the backend system.
- **Why**: Ensures only one global connection is created to avoid conflicts and resource waste.

#### [ARCHITECTURE](ARCHITECTURE.md)

#### ACTIVITY DIAGRAMS

- [ACTIVITY DIAGRAMS](Activity%20Diagrams.md)

- [1. PATIENT REGISTRATION WORKFLOW](Patient%20Registration%20Workflow%20Activity%20Diagram.md)

- [2. APPOINTMENT SCHEDULING WORKFLOW](Appointment%20Scheduling%20Workflow%20Activity%20Diagram.md)

- [3. USER LOGIN WORKFLOW](User%20Login%20Workflow%20Activity%20Diagram.md)

- [4. NOTIFICATION DISPATCH](Notification%20Dispatch%20Activity%20Diagram.md)

- [5. EHR](EHR%20Review%20Activity%20Diagram.md)

- [6. ROLE MANAGEMENT](Role%20Management%20Activity%20Diagram.md)

- [7. REPORT GENERATION](Report%20Generation%20Activity%20Diagram.md)

- [8. EMERGENCY BOOKING](Emergency%20Booking%20Activity%20Diagram.md)

#### [ACTIVITY DIAGRAMS EXPLANATIONS](Activity%20Diagrams%20Explanation.md)

#### [AGILE PLANNING DOCUMENT](Agile%20Planning%20Document.md)

#### [CLASS DIAGRAM](Class%20Diagram.md)

#### [DOMAIN MODEL DOCUMENTATION](Domain%20Model%20Documentation.md)

#### [LANGUAGE CHOICE AND KEY DECISIONS](src/language%20choice%20and%20key%20decisions.md)

#### [KANBAN EXPLANATION](Kanban_explanation.md)

#### [REFLECTION](Reflection.md)

#### [SPECIFICATION](SPECIFICATION.md)

#### [STAKEHOLDER ANALYSIS TABLE](Stakeholder%20Analysis%20Table.md)

#### STATE TRANSITION DIAGRAMS

- [STATE TRANSITION DIAGRAMS](State%20Transition%20Diagrams.md)

- [1. PATIENT ACCOUNT](Patient%20Account%20State%20Transition%20Diagram.md)

- [2. DOCTOR ACCOUNT](Doctor%20Account%20State%20Transition%20Diagram.md)

- [3. APPOINTMENT](Appointment%20State%20Transition%20Diagram.md)
  
- [4. NOTIFICATION](Notification%20State%20Transition%20Diagram.md)

- [5. EHR](EHR%20State%20Transition%20Diagram.md)

- [6. USER ROLE & PERMISSIONS](User%20Role%20%26%20Permissions%20State%20Transition%20Diagram.md)

- [7. SYSTEM REPORT](System%20Report%20State%20Transition%20Diagram.md)

- [8. EMERGENCY BOOKING](Emergency%20Booking%20State%20Transition%20Diagram.md)

#### [STATE TRANSITION DIAGRAMS EXPLANATIONS](State%20Transition%20Diagrams%20Explanation.md)

#### [SYSTEM REQUIREMENTS DOCUMENT](System%20Requirements%20Document.md)

#### [TEMPLATE ANALYSIS](Template_analysis.md)

#### [TEST AND USE CASE DOCUMENT](Test%20and%20Use%20Case%20Document.md)
