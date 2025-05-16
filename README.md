# 🩺 Doctor Appointment Booking System

## 📋 Project Description

A basic doctor appointment booking system – a web and mobile-based application enabling patients to:

* Schedule medical appointments online
* Manage bookings
* Receive automated reminders

Doctors can manage their schedules, and hospital administrators can track statistics and optimize operations. A notification service is integrated for upcoming appointment reminders.

---

## 🚀 Getting Started

```bash
git clone https://github.com/your-username/doctor-appointment-booking.git
cd doctor-appointment-booking
python -m venv venv
source venv/bin/activate          # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt
uvicorn doctor_appointment_booking.main:app --reload
pytest
```

---

## 🛠️ Features for Contribution

| Feature                     | Status  | Contribution Guide |
| --------------------------- | ------- | ------------------ |
| Unit tests for all services | Ongoing | Open Issue         |
| Redis caching               | Planned | `ROADMAP.md`       |
| Email reminder system       | Planned | `ROADMAP.md`       |
| Admin dashboard             | Planned | `ROADMAP.md`       |
| Docker containerization     | Ongoing | Open Issue         |

---

## 📐 Justification for Repository Interface Design

* **Use of Generics**
  Abstracts common CRUD operations into `IRepository` to reduce duplication.

* **Entity-Specific Interfaces**
  Enables custom queries such as `find_by_email()` in `IPatientRepository`.

* **Adherence to SOLID Principles**

  * Interface Segregation: Interfaces tailored for each entity
  * Dependency Inversion: Components depend on abstractions

* **Testability and Flexibility**
  Improves unit testing and service mocking via dependency injection.

---

## ⚔️ Dependency Injection vs Factory Pattern

### ✅ Why Dependency Injection?

* **Highly Testable** – Easy mock injection
* **Separation of Concerns** – Abstraction-driven design
* **Flexible** – Supports multiple implementations (e.g., DB, cache)
* **Framework Friendly** – Integrates well with FastAPI, Django, Flask

### ❗ Factory Pattern Trade-offs

* **Good For** – Dynamic object creation
* **Downsides** – Obscured dependencies, tighter coupling, harder to test

---

## 🧱 Design Pattern Justifications

| Pattern          | Use Case                                   | Justification                                 |
| ---------------- | ------------------------------------------ | --------------------------------------------- |
| Simple Factory   | Create user roles (Patient, Doctor, Admin) | Centralized logic, easier role management     |
| Factory Method   | Sending notifications (Email, SMS)         | Flexibility to extend new channels            |
| Abstract Factory | Render platform-specific UI (Web/Mobile)   | Consistent UI components per platform         |
| Builder          | Constructing complex Appointment objects   | Step-by-step clarity and flexibility          |
| Prototype        | Duplicate report templates                 | Efficient cloning, saves performance          |
| Singleton        | Maintain a single database connection      | Avoids conflicts and excessive resource usage |

---

## 📂 Documentation Index

### 📄 Architecture & Planning

* [ARCHITECTURE.md](ARCHITECTURE.md)
* [Agile Planning Document](Agile%20Planning%20Document.md)
* [Language Choice & Key Decisions](src/language%20choice%20and%20key%20decisions.md)
* [Kanban Explanation](Kanban_explanation.md)
* [Specification](SPECIFICATION.md)
* [Reflection](Reflection.md)
* [Stakeholder Analysis Table](Stakeholder%20Analysis%20Table.md)

---

### 📊 Activity Diagrams

* [Activity Diagrams](Activity%20Diagrams.md)

  * [Patient Registration](Patient%20Registration%20Workflow%20Activity%20Diagram.md)
  * [Appointment Scheduling](Appointment%20Scheduling%20Workflow%20Activity%20Diagram.md)
  * [User Login](User%20Login%20Workflow%20Activity%20Diagram.md)
  * [Notification Dispatch](Notification%20Dispatch%20Activity%20Diagram.md)
  * [EHR Review](EHR%20Review%20Activity%20Diagram.md)
  * [Role Management](Role%20Management%20Activity%20Diagram.md)
  * [Report Generation](Report%20Generation%20Activity%20Diagram.md)
  * [Emergency Booking](Emergency%20Booking%20Activity%20Diagram.md)
* [Activity Diagram Explanations](Activity%20Diagrams%20Explanation.md)

---

### 🔄 State Transition Diagrams

* [State Transition Diagrams](State%20Transition%20Diagrams.md)

  * [Patient Account](Patient%20Account%20State%20Transition%20Diagram.md)
  * [Doctor Account](Doctor%20Account%20State%20Transition%20Diagram.md)
  * [Appointment](Appointment%20State%20Transition%20Diagram.md)
  * [Notification](Notification%20State%20Transition%20Diagram.md)
  * [EHR](EHR%20State%20Transition%20Diagram.md)
  * [User Role & Permissions](User%20Role%20%26%20Permissions%20State%20Transition%20Diagram.md)
  * [System Report](System%20Report%20State%20Transition%20Diagram.md)
  * [Emergency Booking](Emergency%20Booking%20State%20Transition%20Diagram.md)
* [State Diagram Explanations](State%20Transition%20Diagrams%20Explanation.md)

---

### 🧪 Testing & Templates

* [Test and Use Case Document](Test%20and%20Use%20Case%20Document.md)
* [Template Analysis](Template_analysis.md)

---

### 🧬 Class & Domain Models

* [Class Diagram](Class%20Diagram.md)
* [Domain Model Documentation](Domain%20Model%20Documentation.md)


