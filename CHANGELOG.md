### CHANGELOG

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/).

#### [1.0.0] - 2025-04-18
#### Added
- **Implementation of Class Diagram**:
  - Converted the class diagram into Python code with creational design patterns.
  - Implemented classes, attributes, and methods as per the diagram specifications.
  - Integrated Python-based design principles into modular and reusable code.

- **Simple Factory Pattern**:
  - Implemented `UserFactory` class for creating `Patient`, `Doctor`, and `Admin` users.
  - Added functionality for booking appointments (Patient), approving appointments (Doctor), and generating reports (Admin).

- **Factory Method Pattern**:
  - Introduced `Notification` class with concrete implementations for `EmailNotification` and `SMSNotification`.
  - Added `NotificationFactory` base class with factories for email and SMS notifications.

- **Abstract Factory Pattern**:
  - Added `WebUIFactory` and `MobileUIFactory` to create UI components for different platforms.
  - Implemented `WebButton` and `MobileButton` with rendering functionality.

- **Builder Pattern**:
  - Implemented `AppointmentBuilder` for step-by-step creation of `Appointment` objects.
  - Added attributes such as date, time, doctor, patient, and notes.

- **Prototype Pattern**:
  - Added `Report` class with cloning functionality using the prototype pattern.

- **Singleton Pattern**:
  - Implemented `DatabaseConnection` class ensuring a single instance is created.

#### Changed
- Organized project structure:
  - Created `creational_patterns` package with `__init__.py` to manage pattern implementations.
  - Refactored pattern implementations into separate modules for modularity and reusability.
- Added `__all__` definition in the `creational_patterns` package to expose public APIs.

#### Tests
- Implemented unit tests for all creational patterns:
  - **Simple Factory**: Tests for user creation and invalid inputs.
  - **Factory Method**: Tests for notification creation and message sending.
  - **Abstract Factory**: Tests for rendering UI components for web and mobile platforms.
  - **Builder**: Tests for constructing `Appointment` objects with various configurations.
  - **Prototype**: Tests for cloning `Report` objects.
  - **Singleton**: Tests for ensuring only one database connection instance is created.

---
