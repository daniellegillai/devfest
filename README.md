HealthHub: a software development that makes health data more engaging. Project created by Terry Kim, Jacob Hahn, Ivanna Brigido Torres, and Danielle Gillai for DevFest 2025 at Columbia University.

**HealthHub**

**Overview**

HealthHub is an interactive web application designed to make health data more engaging and accessible for users. Our goal is to transform the way individuals interact with their personal health information by incorporating an intuitive and visually engaging interface. Through personalized avatars, interactive body maps, and categorized health data storage, HealthHub encourages users to regularly check in on their well-being in a fun and meaningful way.

**Features**

* User-Friendly Interface: A homepage featuring buttons for new and returning users.

* Personalized Avatars: New users can select a Bitmoji-style avatar from eight diverse options to represent themselves.

* Health Data Hub: Users interact with an avatar on the hub.html page, where body-part-specific buttons (heart, limbs, head) allow them to view and update their health data.

* Categorized Health Records: Three specialized pages—Dental, Optical, and Medications—where users can upload relevant health data. The user can interact with the images that correspond to their medical event.

* Secure Data Storage: Health information is stored securely using MongoDB in the backend.

**Technology Stack**

* Frontend: HTML, CSS, JavaScript

* Backend: Python, MongoDB

* Development Environment: Visual Studio Code

**Project Structure**

* index.html – Homepage with options for new and returning users.

* signup.html – New user registration and avatar selection.

* hub.html – Main user dashboard featuring interactive avatar and body-part-based health data access.

* dental.html – Dental health records page.

* optical.html – Optical health records page.

* medications.html – Medications and prescriptions page.

* main.py – Python-based backend to handle data storage with MongoDB.

* styles/ scripts/ and /images – images, scripts, and styles for accessible and aesthetic interface.



**Future Enhancements**

* Implement user authentication for secure access: 2FA

* Expand avatar selection for even greater diversity. Implement the Snap Kit API so users can upload their own bitmoji from their phone

* Introduce AI-powered health insights and recommendations.

* Mobile-friendly design for accessibility on all devices.

* More secure ways to protect sensitive health data

**Contributing**

We welcome contributions! If you'd like to improve HealthHub, please fork the repository and submit a pull request.
