### Domain Model Description
---

| **Entity**      | **Attributes**                                                                 | **Methods**                                                   | **Relationships**                                                               |
|------------------|--------------------------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------------------------|
| **User**         | `userId: int`, `name: string`, `email: string`, `password: string`, `role: enum` | `register()`, `login()`, `updateProfile()`                     | Can be a `Doctor` or `Patient`; linked to `Notification`, `Appointment`         |
| **Patient**      | `patientId: int`, `medicalHistory: string`, `insuranceInfo: string`           | `bookAppointment()`, `cancelAppointment()`                     | A type of `User`; has many `Appointments`, `EHRs`                                |
| **Doctor**       | `doctorId: int`, `specialization: string`, `licenseNumber: string`            | `approveAppointment()`, `viewSchedule()`, `updateEHR()`        | A type of `User`; associated with many `Appointments`, creates `EHR`            |
| **Appointment**  | `appointmentId: int`, `date: datetime`, `status: enum`, `notes: string`       | `reschedule()`, `cancel()`, `confirm()`                        | Belongs to a `Patient` and a `Doctor`                                           |
| **EHR**          | `ehrId: int`, `summary: string`, `dateCreated: datetime`, `updatedBy: Doctor` | `addEntry()`, `review()`, `archive()`                          | Linked to one `Patient`, edited by one or more `Doctors`                        |
| **Notification** | `notificationId: int`, `message: string`, `status: enum`, `timestamp: datetime` | `send()`, `markAsRead()`                                       | Sent to `User`; generated on appointment events                                 |
| **Report**       | `reportId: int`, `type: string`, `generatedOn: datetime`, `data: JSON`         | `generate()`, `export()`                                       | Managed by `Admin`; aggregates system-wide data                                 |

### Business Rules

- A **User** must be either a **Doctor** or **Patient**, determined by the `role` attribute.
- A **Patient** can book a maximum of **3 active appointments** at a time.
- A **Doctor** can only have appointments during their defined schedule.
- An **EHR** can only be edited by licensed **Doctors**.
- Notifications are generated for events such as appointment confirmations, cancellations, or reminders.
- Only users with an **Admin** role can generate system-wide **Reports**.
