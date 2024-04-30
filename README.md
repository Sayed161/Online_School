# Online School Platform - Backend

Welcome to the backend of the Online School Platform! This Django project serves as the backbone for the Online School platform, providing robust backend functionalities to support user registration, course management, and more. Below is an overview of the backend architecture and functionalities implemented in this project:

## Setup and Installation:
To set up the backend of the Online School platform locally, follow these steps:
1. Clone this repository to your local machine.
2. Navigate to the `backend` directory.
3. Create a virtual environment and activate it.
4. Install the required dependencies using `pip install -r requirements.txt`.
5. Configure the database settings in the `settings.py` file.
6. Run the database migrations using `python manage.py migrate`.
7. Start the Django development server using `python manage.py runserver`.
8. Access the backend APIs via the provided URL.

## Project Structure:
- **apps/**: Contains Django apps for different modules such as user authentication, courses, and departments.
- **templates/**: Stores HTML templates for rendering dynamic content.
- **static/**: Houses static files such as CSS, JavaScript, and images.
- **media/**: Stores user-uploaded files such as course materials and profile pictures.
- **tests/**: Includes unit tests for testing backend functionalities.
- **utils/**: Contains utility functions used across the project.

## API Endpoints:
- **/register/**: Handles user authentication and registration.
- **/login/**: Handles user authentication and login.
- **/course/**: Manages CRUD operations for courses.
- **/lesson/**: Manages courses lessons.
- **/student/**: Manages Students.
- **/category/**: Provides endpoints for managing categories.
- **/review/**: Allows to review about the courses.
- **/enroll/**: Handles course enrollment and student progress tracking.

## Technologies Used:
- **Django**: A high-level Python web framework for rapid development and clean, pragmatic design.
- **Django Rest Framework (DRF)**: A 
