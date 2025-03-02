# Doctor Appointment Booking System

## Domain: Hospital

Scheduling doctor appointments manually can lead to many unpleasant situations such as long wait times, mismanagement of bookings, and difficulty in tracking different patients’ history. This will be a basic doctor appointment booking system, which will be a web and mobile-based app that will allow patients to schedule medical appointments online, manage bookings, and receive reminders. Doctors will use the system to manage their different schedules, while hospital administrators will be able to monitor appointment statistics and optimize scheduling efficiency. A notification service will be included to remind patients about upcoming appointments.


```mermaid
C4Context
    title System Context Diagram for Doctor Appointment Booking System

    Enterprise_Boundary(Hospital, "Hospital Network") {
        Person(patient, "Patient", "Books, cancels, and views appointments.")
        Person(doctor, "Doctor", "Manages daily schedules and patient visits.")
        Person(admin, "Hospital Admin", "Manages system and schedules.")

        System(DABS, "Doctor Appointment Booking System", "Allows patients to book appointments, doctors to manage schedules, and admins to oversee the system.")

        Enterprise_Boundary(HospitalInfra, "Hospital IT Infrastructure") {
            SystemDb_Ext(Database, "Hospital Database", "Stores patient, doctor, and appointment data.")

            System_Boundary(InternalSystems, "Internal Hospital Systems") {
                System(WebApp, "Web/Mobile App", "Interface for patients and doctors.")
                System(AdminDashboard, "Admin Dashboard", "Interface for hospital admins.")
            }

            System_Ext(NotificationService, "E-mail & SMS Service", "Sends appointment reminders.")
            SystemDb(AppointmentRecords, "Appointment Records Database", "Stores all booking records.")

            Boundary(NotificationBoundary, "Notification System") {
                SystemQueue(NotificationQueue, "Notification Queue", "Handles appointment reminders.")
                SystemQueue_Ext(ExternalAPI, "External Messaging API", "Third-party service for notifications.")
            }
        }
    }

    BiRel(patient, DABS, "Books & Cancels Appointments")
    BiRel(doctor, DABS, "Views & Manages Schedules")
    BiRel(admin, DABS, "Oversees System & Schedules")
    BiRel(DABS, Database, "Stores/Retrieves Data")
    Rel(DABS, NotificationService, "Sends Appointment Reminders", "SMTP/SMS")
    Rel(NotificationService, patient, "Notifies Patient of Appointments")
```
```mermaid
C4Container
    title Container Diagram for Doctor Appointment Booking System

    Person(patient, "Patient", "Uses the system to book, reschedule, or cancel appointments.")
    Person(doctor, "Doctor", "Manages appointment schedules and patient visits.")
    Person(admin, "Admin", "Manages system users, schedules, and reports.")

    System_Boundary(DABS, "Doctor Appointment Booking System") {
        Container(WebApp, "Web/Mobile App", "React Native", "Frontend interface for patients and doctors.")
        Container(AdminDashboard, "Admin Dashboard", "React + Node.js", "Provides administrative control and reports.")
        Container(API, "Backend API", "Django/FastAPI", "Handles business logic and data processing.")
        ContainerDb(AppointmentDB, "Appointment Database", "PostgreSQL", "Stores appointment details and history.")
        Container(NotificationService, "Notification Service", "Twilio/SMTP", "Sends automated appointment reminders.")
        Container(AuthService, "Authentication Service", "OAuth2 / JWT", "Handles user authentication and authorization.")
    }

    BiRel(patient, WebApp, "Uses")
    BiRel(doctor, WebApp, "Uses")
    BiRel(admin, AdminDashboard, "Manages system")
    Rel(WebApp, API, "Sends Requests", "REST API")
    Rel(AdminDashboard, API, "Fetches Data", "REST API")
    Rel(API, AppointmentDB, "Stores and retrieves appointments")
    Rel(API, NotificationService, "Triggers notifications")
    Rel(API, AuthService, "Handles authentication")
    Rel(NotificationService, patient, "Sends reminders")
```
```mermaid
C4Component
    title Component Diagram for DABS Backend API

    Container_Boundary(Backend, "Backend API") {
        Component(AppointmentController, "Appointment Controller", "Django/FastAPI", "Handles appointment operations")
        Component(UserController, "User Controller", "Django/FastAPI", "Handles user authentication and management")
        Component(NotificationController, "Notification Controller", "Django/FastAPI", "Sends appointment reminders")
        Component(ServiceLayer, "Service Layer", "Python", "Processes business logic and validations")
        Component(AppointmentRepository, "Appointment Repository", "SQLAlchemy", "Handles database interactions for appointments")
        Component(AuthService, "Authentication Service", "OAuth2 / JWT", "Manages user authentication and authorization")
        ComponentDb(AppointmentDB, "Appointment Database", "PostgreSQL", "Stores appointment records")
        Component(NotificationService, "Notification Service", "Twilio/SMTP", "Handles messaging")
    }

    BiRel(AppointmentController, ServiceLayer, "Processes requests")
    BiRel(UserController, AuthService, "Authenticates users")
    BiRel(AppointmentController, AppointmentRepository, "Retrieves/Saves Appointments")
    BiRel(AppointmentRepository, AppointmentDB, "Stores data")
    BiRel(NotificationController, NotificationService, "Sends notifications")
```
```mermaid
C4Dynamic
    title Dynamic Diagram for Doctor Appointment Booking System - API Application

    ContainerDb(c4, "Database", "Relational Database Schema", "Stores patient and doctor information, appointment records, authentication credentials, etc.")
    Container(c1, "Web/Mobile App", "React Native", "Provides an interface for patients and doctors to interact with the system.")
    Container_Boundary(b, "API Application") {
        Component(c3, "Authentication Component", "Django/FastAPI", "Handles user authentication and session management.")
        Component(c2, "Appointment Controller", "Django/FastAPI", "Manages appointment bookings, cancellations, and scheduling.")
    }
    Rel(c1, c2, "Submits booking requests to", "JSON/HTTPS")
    Rel(c2, c3, "Validates user authentication")
    Rel(c3, c4, "Queries user credentials", "SQL")

    UpdateRelStyle(c1, c2, $textColor="red", $offsetY="-40")
    UpdateRelStyle(c2, c3, $textColor="red", $offsetX="-40", $offsetY="60")
    UpdateRelStyle(c3, c4, $textColor="red", $offsetY="-40", $offsetX="10")
```

