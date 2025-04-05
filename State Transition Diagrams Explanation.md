### State Transition Diagrams Explanation

#### 1. Patient Account

**Object**: Patient Account  
**States**: Registered, Active, Suspended, Deleted  
**Events/Transitions**:  
- **Email Verified**: `Registered → Active`  
- **Admin Action**: `Active → Suspended`  
- **Reinstated**: `Suspended → Active`  
- **User Request**: `Active → Deleted`  

**Functional Requirement Mapping**:  
- **FR1**: Account management — email verification, deletion.  
- **NFR5**: Security — allows suspension.  

**Explanation**:  
The diagram ensures account lifecycle management. Patients benefit from privacy and control. Admins can maintain compliance and deactivate misuse, addressing data protection and user experience concerns.

---

#### 2. Doctor Account

**Object**: Doctor Account  
**States**: Registered, Verified, Active, Suspended, Deactivated  
**Events/Transitions**:  
- **License Approved**: `Registered → Verified`  
- **Admin Activation**: `Verified → Active`  
- **Misconduct**: `Active → Suspended`  
- **Cleared**: `Suspended → Active`  
- **Voluntary Exit**: `Active → Deactivated`  

**Functional Requirement Mapping**:  
- **FR7**: Profile management  

**Explanation**:  
Ensures only verified professionals are active. This helps healthcare administrators maintain compliance and mitigate risks associated with unqualified individuals.

---

#### 3. Appointment

**Object**: Appointment  
**States**: Requested, Confirmed, Attended, Missed, Cancelled  
**Events/Transitions**:  
- **Slot Available**: `Requested → Confirmed`  
- **Patient Attends**: `Confirmed → Attended`  
- **No-show**: `Confirmed → Missed`  
- **Cancellation**: `Confirmed → Cancelled`  

**Functional Requirement Mapping**:  
- **FR2–FR5**: Booking, rescheduling, cancellation, tracking  

**Explanation**:  
Improves scheduling efficiency. Helps reduce no-shows for doctors, supports real-time slot management for receptionists, and ensures timely service for patients.

---

#### 4. Notification

**Object**: Notification  
**States**: Created, Sent, Read, Failed, Archived  
**Events/Transitions**:  
- **Trigger Event**: `Created → Sent`  
- **Opened by User**: `Sent → Read`  
- **Delivery Error**: `Sent → Failed`  
- **Read/Failed**: `→ Archived`  

**Functional Requirement Mapping**:  
- **FR3**: Receive reminders  

**Explanation**:  
Supports timely patient reminders, helping reduce missed appointments (addressing a key patient pain point). Logged failures allow IT to ensure delivery success.

---

#### 5. Electronic Health Record (EHR)

**Object**: Electronic Health Record  
**States**: Created, Reviewed, Updated, Archived  
**Events/Transitions**:  
- **Doctor Accesses**: `Created → Reviewed`  
- **Doctor Edits**: `Reviewed → Updated`  
- **Discharge**: `Updated → Archived`  

**Functional Requirement Mapping**:  
- **FR11**: EHR lifecycle  

**Explanation**:  
Doctors can update care records in real-time, ensuring clinical accuracy. Archived states aid regulatory audits and insurer claims.

---

#### 6. User Role & Permissions

**Object**: User Role & Permissions
**States**: Assigned, Active, Updated, Revoked  
**Events/Transitions**:  
- **User Logs In**: `Assigned → Active`  
- **Admin Changes**: `Active → Updated`  
- **Access Removed**: `Active → Revoked`  

**Functional Requirement Mapping**:  
- **FR12, NFR5.2**: Role and access control  

**Explanation**:  
Helps IT enforce permission levels. Improves system security and supports traceability for regulatory needs.

---

#### 7. System Report

**Object**: System Report  
**States**: Scheduled, Generated, Reviewed, Archived  
**Events/Transitions**:  
- **Time Trigger**: `Scheduled → Generated`  
- **Admin Opens**: `Generated → Reviewed`  
- **Review Complete**: `Reviewed → Archived`  

**Functional Requirement Mapping**:  
- **FR10**: View analytics  

**Explanation**:  
Provides administrators with real-time operational insights. Supports cost-saving initiatives and informed decision-making efforts.

---

#### 8. Emergency Booking

**Object**: Emergency Booking  
**States**: Initiated, Confirmed, Attended, Cancelled  
**Events/Transitions**:  
- **Slot Override**: `Initiated → Confirmed`  
- **Emergency Visit**: `Confirmed → Attended`  
- **Not Needed**: `Confirmed → Cancelled`  

**Functional Requirement Mapping**:  
- **FR8**: Emergency flow  

**Explanation**:  
Reduces wait time for critical care. Benefits patients and ensures receptionists and doctors are instantly notified of emergencies.
