# Project Title
Doctor Appointment Booking System

### Project Description
This is a basic doctor appointment booking system, a web and mobile-based app allowing patients to schedule medical appointments online, manage bookings, and receive reminders. Doctors will use the system to manage their different schedules; hospital administrators will be able to monitor appointment statistics and optimize scheduling efficiency. A notification service will be included to remind patients about upcoming appointments.

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


