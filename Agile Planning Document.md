**User Stories**

| Story ID | User Story | Acceptance Criteria | Priority |
|----------|------------|----------------------|----------|
| US1 | As a **patient**, I want to register and authenticate my account so that I can securely access the system. | - User can successfully create an account. <br> - User can log in using valid credentials. <br> - System denies access with invalid credentials. | High |
| US2 | As a **patient**, I want to schedule an appointment with a doctor so that I can receive medical consultation at a convenient time. | - Patient can view available slots. <br> - Patient can successfully book an appointment. <br> - System confirms appointment booking. | High |
| US3 | As a **doctor**, I want to set my availability so that patients can book appointments accordingly. | - Doctor can set available time slots. <br> - Patients can only book within available slots. <br> - Doctor can update availability. | High |
| US4 | As a **patient**, I want to receive automated reminders for my appointments so that I don’t forget them. | - System sends reminders via email/SMS. <br> - Reminder is sent at configured intervals before the appointment. | Medium |
| US5 | As a **doctor**, I want to receive appointment reminders so that I can prepare in advance. | - System notifies doctor of upcoming appointments. <br> - Notifications appear on the dashboard and via email/SMS. | Medium |
| US6 | As a **patient**, I want to reschedule or cancel my appointment so that I can manage my availability without hassle. | - Patient can reschedule or cancel an appointment. <br> - System updates availability accordingly. <br> - Cancellation policies are enforced. | High |
| US7 | As a **receptionist**, I want to update patient appointments so that I can assist with scheduling conflicts. | - Receptionist can modify appointments for patients. <br> - System maintains logs of changes. | Medium |
| US8 | As a **healthcare administrator**, I want to track patient no-shows so that I can enforce penalties if necessary. | - System tracks patient attendance. <br> - No-show penalties are applied based on clinic policies. | Medium |
| US9 | As a **doctor**, I want to be notified about patient no-shows so that I can adjust my schedule accordingly. | - System marks appointments as missed. <br> - Doctor receives no-show notifications. | Medium |
| US10 | As an **IT administrator**, I want to ensure that patient data is securely stored so that it complies with regulatory standards. | - System encrypts and stores data securely. <br> - Access control policies are enforced. <br> - Compliance audits are successful. | High |
| US11 | As a **doctor**, I want to have a dashboard to manage my appointments so that I can track my daily schedule efficiently. | - Dashboard displays daily appointments. <br> - Doctors can filter and manage schedules easily. | High |
| US12 | As a **patient**, I want to book emergency appointments so that I can receive urgent medical care. | - Emergency appointments bypass standard scheduling. <br> - System prioritizes emergency bookings. | High |
| US13 | As a **receptionist**, I want to prioritize emergency bookings so that critical cases are handled first. | - Receptionist can override regular booking rules. <br> - System tracks emergency cases separately. | High |
| US14 | As an **IT administrator**, I want to assign roles and permissions so that users can only access relevant features. | - Admins can assign predefined roles. <br> - Users only access authorized sections. | High |
| US15 | As a **healthcare administrator**, I want to manage staff permissions so that data security is maintained. | - System supports role-based access control (RBAC). <br> - Unauthorized access is restricted. | High |
| US16 | As a **patient**, I want the system to load quickly so that I can book an appointment without delays. | - Page loads within 3 seconds. <br> - System remains responsive under normal load. | High |
| US17 | As a **doctor**, I want the dashboard to respond instantly so that I can manage my schedule efficiently. | - Dashboard loads data within 2 seconds. <br> - System performance remains consistent. | High |
| US18 | As an **IT administrator**, I want system response times to meet performance standards so that users have a smooth experience. | - Performance benchmarks are met. <br> - System optimizes resource usage effectively. | High |

---

&nbsp;

**Product Backlog**

| Story ID | User Story | Priority (MoSCoW) | Effort Estimate | Dependencies |
|----------|------------|------------------|------------------------------|--------------|
| US1 | As a **patient**, I want to register and authenticate my account so that I can securely access the system. | Must-have | 3 | - |
| US2 | As a **patient**, I want to schedule an appointment with a doctor so that I can receive medical consultation at a convenient time. | Must-have | 5 | US1 |
| US3 | As a **doctor**, I want to set my availability so that patients can book appointments accordingly. | Must-have | 3 | - |
| US4 | As a **patient**, I want to receive automated reminders for my appointments so that I don’t forget them. | Should-have | 2 | US2 |
| US5 | As a **doctor**, I want to receive appointment reminders so that I can prepare in advance. | Should-have | 2 | US2 |
| US6 | As a **patient**, I want to reschedule or cancel my appointment so that I can manage my availability without hassle. | Must-have | 4 | US2 |
| US7 | As a **receptionist**, I want to update patient appointments so that I can assist with scheduling conflicts. | Should-have | 3 | US2 |
| US8 | As a **healthcare administrator**, I want to track patient no-shows so that I can enforce penalties if necessary. | Should-have | 3 | US6 |
| US9 | As a **doctor**, I want to be notified about patient no-shows so that I can adjust my schedule accordingly. | Should-have | 2 | US6, US8 |
| US10 | As an **IT administrator**, I want to ensure that patient data is securely stored so that it complies with regulatory standards. | Must-have | 5 | - |
| US11 | As a **doctor**, I want to have a dashboard to manage my appointments so that I can track my daily schedule efficiently. | Must-have | 4 | US2, US3 |
| US12 | As a **patient**, I want to book emergency appointments so that I can receive urgent medical care. | Must-have | 4 | US2 |
| US13 | As a **receptionist**, I want to prioritize emergency bookings so that critical cases are handled first. | Must-have | 3 | US12 |
| US14 | As an **IT administrator**, I want to assign roles and permissions so that users can only access relevant features. | Must-have | 4 | US1, US10 |
| US15 | As a **healthcare administrator**, I want to manage staff permissions so that data security is maintained. | Must-have | 4 | US14 |
| US16 | As a **patient**, I want the system to load quickly so that I can book an appointment without delays. | Could-have | 2 | - |
| US17 | As a **doctor**, I want the dashboard to respond instantly so that I can manage my schedule efficiently. | Could-have | 2 | US11 |
| US18 | As an **IT administrator**, I want system response times to meet performance standards so that users have a smooth experience. | Could-have | 3 | US16, US17 |

---

&nbsp;

**Sprint Planning - Sprint 1**

| Task ID | Task Description                                         | Assigned To        | Estimated Hours | Status |
| ------- | -------------------------------------------------------- | ------------------ | --------------- | ------ |
| T1      | Develop patient registration API                         | Backend Developer  | 8               | To Do  |
| T2      | Design and implement registration UI                     | Frontend Developer | 10              | To Do  |
| T3      | Implement user authentication (login/logout)             | Backend Developer  | 6               | To Do  |
| T4      | Develop appointment booking API                          | Backend Developer  | 12              | To Do  |
| T5      | Design and implement appointment booking UI              | Frontend Developer | 10              | To Do  |
| T6      | Set up database schema for users and appointments        | Database Engineer  | 6               | To Do  |
| T7      | Implement validation for appointment scheduling          | Backend Developer  | 8               | To Do  |
| T8      | Write unit tests for authentication and booking features | QA Engineer        | 10              | To Do  |
| T9      | Deploy initial version to test environment               | DevOps Engineer    | 6               | To Do  |
| T10     | Perform end-to-end testing on booking and authentication | QA Engineer        | 8               | To Do  |
