# SoSe-2024-Group-C
## Studentify 
The application is designed to assist prospective, newly admitted, and already admitted students who want to socialize, make friends, and join interesting activities within the university area.

This software will be installed on a single computer where students can come to browse, add, or join events. Every month, all student organizations will update their information accordingly, ensuring that students have access to the latest happenings on campus.

## Important points to be noted : 
* In commit the commits from **DESKTOP-23RLU4I\user** is Joel Varughese Thomas. there are some issues while pushing that we couldnt rectify.
* Our third member Mr. Chandu Hara Gopal, has actively participated in the initial phase like system Architecture and requirement engineering. However he couldnt join for other activities, so we couldnt implement all the requirment and functionality in coding, hence we have to reduce it.
* The entire coding is done through pair programming, hence both the students, Mr. Akhil and Mr. Joel has equal participation in every module. 
* A detailed video on working of software and a report has been uploaded with more details regarding the software.

## Requirement Specifications

### USER Requirements

1.	The software shall have the login feature for the user to provide security and privacy to the personal data.
2.	The software shall include distinct sections or separations within the user interface to clearly differentiate between various options like add events, view events, forum post, inquiries etc.
3.	The software shall allow the user to add their own events.
4.	The software shall give alerts or notifications when user responds to an event or a reply to an inquiry is received.
5.  The software shall facilitate a platform for students to post queries or concerns, with provision for other students to comment and engage in discussion.
6.  The software shall feature a dedicated functionality enabling students to submit inquiries requiring personal attention to the student representative, regarding educational concerns.
7. The software shall allow users to respond to events and to view the list of people responded.



### SYSTEM requirements

1.1.    The software shall provision create account feature for the new users(including student organisation) using their full name, enrollment id, email and password.

1.2.    The software shall provide login feature for known user accounts from successfully created details.

1.3.    The software shall have two account types: student and student representative, which is selected.

1.3.    The software shall provide a incorrect warning incase of incorrect student ID or incorrect password.

1.4.    The software shall have the logout feature.

2.1.    The software shall show 5 sections: View Profile, notification, Add/view Event, post/view open queries and inquiries.

2.2.    Each section shall be in differenct buttons. 

3.1.    The events shall have a event name, location, date, time and details.

4.1.    The software shall give in-app notification to host when someone responds to event with yes, no or may be.

4.2.    The software shall give notification when a student receives reply from their student representative.

4.3.    The notification should be cleared once it is read.

5.1.    The forum shall have fields to add title and to type the post.

5.2.    The software shall give option to comment and shall view all comments.

5.3.    If the comments contain any improper words, the software shall find it and give a warning about it and terminte the process.

6.1.    The submitted inquiries shall be catogorized based on thir nature, for instance examination, re-registration, studies, transcripts and documents, workshops, co-curricular activities, Sports etc.

7.1.    The software shall give an option to respond to the events like yes/no/maybe

7.2.    The software shall show response as drop down.


### Functional requirements

1.  The user shall be able to input the login details such as login id and password for the access to the software.

2.  The sofware shall allow the user to post on the forum or react to any information posted.

3.  Different tabs/sections of the GUI shall interact based on the selection of user.

4.  The address/location of the events or program shall be visible to everyone in the group.



### Non Functional Requirements

1.  The software shall be developed using Python programming concepts.

2.	The software shall utilize Python's GUI capabilities, specifically leveraging libraries such as Tkinter, to provide a user-friendly front-end interface.

3.  The software shall run in Windows OS.

4.  Only registered user shall login into the app.

5.  All the tabs are clearly visible to the user such that user don't need to find the hidden features in the software.

6.  The personal details of the users shall only be visible to oneself.

## System Architecture

![System Architecture](./arche.jpg)

## UML 

### Class Diagram

![Class](./UML/ClassDiagram1.jpg)

### Use Case Diagram

![Use case](./UML/Use_case_diagram.jpeg)

### State Diagram

![State Dia](./UML/State_diagram__2_.jpeg)

### Sequencial Diagram

#### Post Quries (forum Post)

![Seq post](./UML/Sequence_diagram_forum_post__3_.jpeg)

#### Add or view event

![Seq ADDe](./UML/Sequence_diagram_add_view_event.jpeg)

#### Notification

![Seq notification](./UML/Sequence_diagram_for_notification.jpeg)

### Activiy Diagram - Login

![act](./UML/Activity_diagram.JPG)




























