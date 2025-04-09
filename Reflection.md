### Balancing Stakeholders' needs.
It was challenging to balance Stakeholders' needs because each stakeholder and their role in the system had to be considered. For instance, patients required a user-friendly system that reduced the steps in scheduling appointments and ensured that their data would be secured and well-protected. Doctors should be able to manage their schedules and their availability efficiently.

### Translating Requirements to Use Cases/Tests
Translating the functional and non-functional into use cases/tests was challenging because it required a long thinking process about each actor's role and the different actions they will have to undertake while using the system. Every step needed to be mentioned and explained.

### Reflection: Challenges in prioritization, estimation, or aligning Agile with stakeholder needs
As the only manager overseeing an Agile project, I often find it difficult to prioritize tasks and estimate how much time each will take. Ensuring that the project aligns with user needs is also challenging. When I depend entirely on my judgment, it can result in confusion and deadlines that aren't met. To improve, I should actively seek feedback and engage more with users to understand their needs. Additionally, staying flexible can help the project meet its objectives effectively.

### Reflection: Choosing and Editing GitHub Templates
When it comes to choosing a template on GitHub, it is a bit challenging as it doesn't offer a preview option or a demo to play around with, so that you can choose an option for your project without having to try different templates to choose the suitable one.
Customising the template can take a while, as you have to familiarise yourself with the workflow and have an idea of how to link the issues to the project. The other challenge is that once a template has been chosen, you can't go back and choose another one; you will have to create a new project and start from scratch.

### Reflection: Comparison between Github Templates, Trello and Jira

- **GitHub Templates**: They're easy to set up but offer limited customization. They are ideal for projects focused on software development. They work smoothly with GitHub repositories but don't offer a lot of reporting options.

- **Trello**: This tool is simple to use and can be customized. It's a good choice for small teams or personal projects. Trello supports connections to various tools, but doesn't have strong features for Agile project management.

- **Jira**: Jira is very customizable and suits complicated and big projects well. It offers a lot of support for Agile methods, detailed reporting, and is built to handle the needs of large enterprises.

### Assignment 8 Reflection

One of the main challenges when making UML diagrams, especially state and activity diagrams, is deciding how detailed they should be. If the diagrams have too much detail, they can become confusing and hard to understand, making it difficult for people to read them and increasing the mental effort needed. On the other hand, if there is too much generalization, important system behaviors or decision points might be missed. These are necessary for developing the system and checking if it works as expected. It's important to find the right balance. This means identifying the key transitions and actions that match what users need and grouping or simplifying less important processes that can be understood without details or found in other documents.

Another challenge is matching these diagrams with Agile user stories. User stories are often vague as they focus on business value and what the user wants, while diagrams need to show how the system works. For example, turning a user story like “As a patient, I want to book an appointment to see a doctor” into specific states like Requested, Confirmed, or Cancelled, or into steps like Choose Time and Confirm Slot, requires careful thought. Each diagram must be linked accurately to the user’s goal, making sure it doesn't go beyond what the story intends.

State diagrams and activity diagrams serve different, yet important roles. State diagrams show how an object behaves in response to events over time. They capture the lifecycle of things like appointments or notifications and are essential for systems that rely on status-driven logic. In contrast, activity diagrams illustrate workflows or processes. They show a sequence of tasks and decisions across various roles and effectively highlight business processes and user interactions. Together, they give a complete view—state diagrams show what can happen to objects over time, while activity diagrams detail how tasks are carried out.

### Reflection on Designing the Domain Model and Class Diagram

#### 1. Challenges in Designing the Domain Model and Class Diagram

Creating the domain model and class diagram for a doctor appointment booking system came with several challenges. We had to decide on the right levels of detail, understand how different parts connect, and assign the right roles to each class.

Initially, one of the biggest challenges was to find the right level of abstraction for things like Appointment, User, and Doctor. We thought about combining or simplifying these parts to make our work easier, but that would make the model less flexible and harder to expand later on.

Another hurdle was accurately representing how entities relate to each other within real-world constraints. The relationship between a Patient and an Appointment initially looked simple: a patient makes an appointment. But considering cancellations, rescheduling, and emergency bookings made this relationship became more complicated. Similarly, understanding doctors' availability required looking beyond just their schedules. We also needed to account for their interactions with the Receptionist team and how emergencies would be handled.

It was also challenging to decide what actions each class should perform. We needed to determine if certain tasks should belong to a class or be managed by external services. For instance, should a Doctor object handle the approval of appointments, or should an Appointment object manage its status? Balancing between data and actions took time and required insight into both business needs and programming best practices.

#### 2. Alignment with Previous Work

The class diagram fits well with other prior work, such as use cases, state transition diagrams, activity diagrams, and functional requirements. For example, use cases like "Book Appointment" or "Register Patient" are directly related to functions like bookAppointment() or registerPatient(). The Appointment state transition diagram includes stages like Requested, Confirmed, Cancelled, and Attended, which influenced the attributes and state methods of the Appointment class.

Additionally, the class responsibilities reflect action flows from activity diagrams. For instance, the Notification class aligns with the "Notification Dispatch" activity diagram, where events result in notifications being sent or logged. By anchoring the class diagram in these existing workflows, we maintain consistency in the system, making it easier to support and enhance in the future.

#### 3. Trade-Offs Made

We made some decisions to simplify and clarify the design. One major choice was to avoid complex inheritance hierarchies. While modeling User, Doctor, and Patient with inheritance might be tempting, it could complicate permissions and create rigid structures. Instead, we treated Doctor and Patient as separate entities while sharing user account information or managing access through a Role class.

We also simplified how components are combined and connected. For example, instead of tightly integrating Electronic Health Records (EHRs) with a Patient and multiple Appointments, we let EHRs reference patients independently. This results in better modularity.

#### 4. Lessons Learned in Object-Oriented Design

Working on this project provided valuable lessons in object-oriented design. It's crucial for each class to have a clear purpose and to encapsulate both the data and the actions relevant to that purpose. Relationships should mirror real-life connections without being overly complex or tightly linked.

Maintaining alignment among design documents—like use cases, diagrams, and code—is also important. Consistency across these elements makes the system easier to understand, discuss, and build. The exercise highlighted design as an iterative process. Initial versions may function, but often require refinements. Through feedback and an understanding of business rules and technical limitations, a solid and scalable model emerges.

Overall, this experience deepened my understanding of object-oriented design principles and demonstrated how thoughtful design decisions can improve system clarity, scalability, and maintainability.
