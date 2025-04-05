### Activity Diagrams Explanations

#### **1. Patient Registration Workflow**

- **Start/End Nodes**:
  - Start: Patient initiates the registration process
  - End: Confirmation email is sent

- **Actions**:
  - Fill and submit registration form
  - System validates data
  - Store patient info
  - Send confirmation email

- **Decisions**:
  - Is Data Valid?

- **Parallel Actions**:
  - Not applicable

- **Swimlanes**:
  - User: Fills and submits form
  - System: Validates and processes registration

- **Stakeholder Concerns Addressed**:
  - Patients: Provides ease of use, instant feedback on form errors
  - IT/Admin: Validated and structured data input improves integrity
  - Healthcare Admins: Less manual cleanup, improves data reliability

---

#### **2. Appointment Scheduling Workflow**

- **Start/End Nodes**:
  - Start: Patient chooses a date and time
  - End: Appointment is confirmed and a notification is sent

- **Actions**:
  - Choose date/time
  - Check availability
  - Confirm booking
  - Send confirmation message

- **Decisions**:
  - Is Slot Available?

- **Parallel Actions**:
  - Could parallelize confirmation with calendar updates

- **Swimlanes**:
  - User: Picks slot
  - System: Manages scheduling logic

- **Stakeholder Concerns Addressed**:
  - Patients: Reduces frustration by suggesting alternatives
  - Doctors/Receptionists: Fewer scheduling conflicts
  - Admins: Higher booking efficiency, better time utilization

---

#### **3. User Login Workflow**

- **Start/End Nodes**:
  - Start: User attempts login
  - End: Redirected to dashboard

- **Actions**:
  - Enter credentials
  - Validate credentials
  - Redirect to dashboard

- **Decisions**:
  - Are credentials correct?

- **Parallel Actions**:
  - None

- **Swimlanes**:
  - User: Inputs credentials
  - System: Authenticates and manages session

- **Stakeholder Concerns Addressed**:
  - All users: Secure and quick access
  - IT Admins: Prevents unauthorized access

---

#### **4. Notification Dispatch**

- **Start/End Nodes**:
  - Start: Trigger event occurs
  - End: Notification is logged

- **Actions**:
  - Trigger notification
  - Generate and send notification
  - Log status

- **Decisions**:
  - None

- **Parallel Actions**:
  - Possible future improvement: Send + Log concurrently

- **Swimlanes**:
  - System: Handles entire flow automatically

- **Stakeholder Concerns Addressed**:
  - Patients/Doctors: Timely communication
  - Receptionists: Fewer missed appointments
  - IT: Improved traceability and error detection

---

#### **5. EHR Review**

- **Start/End Nodes**:
  - Start: Doctor logs in
  - End: Changes are saved

- **Actions**:
  - Login
  - Select patient
  - Review/edit EHR
  - Save changes

- **Decisions**:
  - None

- **Parallel Actions**:
  - May include multiple edits/reviews

- **Swimlanes**:
  - Doctor: Navigates and updates
  - System: Handles data retrieval and save

- **Stakeholder Concerns Addressed**:
  - Doctors: Access to up-to-date records
  - Admins: Accuracy and audit support
  - Regulatory: Supports compliance

---

#### **6. Role Management**

- **Start/End Nodes**:
  - Start: Admin initiates action
  - End: Access level confirmed

- **Actions**:
  - Select user
  - Assign role
  - Set permissions
  - Confirm access

- **Decisions**:
  - None

- **Parallel Actions**:
  - Could log action while setting permissions

- **Swimlanes**:
  - Admin: Initiates and manages changes
  - System: Applies updates

- **Stakeholder Concerns Addressed**:
  - IT/Admins: Clear access control
  - Regulatory: Role-based restrictions support audits

---

#### **7. Report Generation**

- **Start/End Nodes**:
  - Start: Admin selects report type
  - End: Report is exported

- **Actions**:
  - Fetch data
  - Generate visuals
  - Export report

- **Decisions**:
  - None

- **Parallel Actions**:
  - Generate and export in parallel

- **Swimlanes**:
  - Admin: Requests report
  - System: Processes data and generates output

- **Stakeholder Concerns Addressed**:
  - Admins: Enables operational insight
  - Regulatory: Facilitates compliance
  - Insurers: Supports claims review

---

#### **8. Emergency Booking**

- **Start/End Nodes**:
  - Start: User marks emergency
  - End: Slot booked and alert sent

- **Actions**:
  - Mark emergency
  - Override slot availability
  - Book appointment
  - Send alert

- **Decisions**:
  - None

- **Parallel Actions**:
  - Book slot and send alert simultaneously

- **Swimlanes**:
  - User: Triggers emergency booking
  - System: Executes overrides and communication

- **Stakeholder Concerns Addressed**:
  - Patients: Fast emergency care
  - Doctors: Real-time alerts
  - Admins: Effective triage and resource allocation
 
&nbsp;

#### Activity Diagrams Traceability

| Workflow               | Functional Requirement | User Story            | Sprint Task    |
|------------------------|------------------------|------------------------|----------------|
| Patient Registration   | FR1                    | Register               | T1, T2         |
| Appointment Scheduling | FR2, FR4               | Book or cancel         | T4, T5, T7     |
| User Login             | FR1                    | Login                  | T3             |
| Notification Dispatch  | FR3                    | Receive reminders      | T8             |
| EHR Review             | FR11                   | Access patient data    | T1             |
| Role Management        | FR12, NFR5.2           | Manage roles           | T6             |
| Report Generation      | FR10                   | Generate reports       | T10            |
| Emergency Booking      | FR8                    | Handle urgent booking  | T4             |

