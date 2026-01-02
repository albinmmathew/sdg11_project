# Smart City - SDG 11 Project

A Django-based web application focused on **Sustainable Cities and Communities (SDG 11)**. This platform empowers citizens to report local issues, track their resolution, and prioritize community needs through a voting system. It facilitates better communication between residents and city administrators to build safer, more resilient, and sustainable cities.

## Features

*   **User Authentication**: Secure registration, login, and logout functionality for citizens.
*   **Issue Reporting**: Users can report various community issues (e.g., waste management, road damage) with details like title, description, location, and category.
*   **Categorization**: Issues are organized by categories. Categories can be flagged as 'emergency' and include specific helpline numbers.
*   **Voting System**: Community members can upvote reported issues to highlight their importance and urgency to authorities.
*   **Admin Dashboard**: A dedicated interface for administrators to view all reported issues and update their status (Reported, In Progress, Resolved).
*   **Status Tracking**: Users can track the progress of the issues they reported or voted for.
*   **Ajax Integration**: Dynamic fetching of category information (such as emergency details) to enhance user experience.

## Tech Stack

*   **Backend**: Python, Django
*   **Database**: SQLite (Development), Support for others via Django ORM
*   **Frontend**: HTML, CSS, JavaScript, Django Templates
*   **Deployment**: Render (Configuration included)

## Installation & Setup

### Prerequisites

*   Python 3.8 or higher
*   pip (Python package manager)

### Local Development

1.  **Clone the repository**
    ```bash
    git clone <repository-url>
    cd sdg11_project
    ```

2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (Admin)**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server**
    ```bash
    python manage.py runserver
    ```

7.  **Access the application**
    *   Main Site: `http://127.0.0.1:8000/`
    *   Admin Panel: `http://127.0.0.1:8000/admin/`

## Usage

1.  **Register** for a new account using the signup page.
2.  **Login** to access the dashboard.
3.  **Report an Issue** by clicking the "Report Issue" button. Fill in the details and select a category.
4.  **View Issues** on the main feed. You can see issue status and details.
5.  **Upvote** issues that you believe need immediate attention.
6.  **Admins** can log in to the specific admin dashboard (via `/issues/admin/` or the Django admin panel) to manage issue statuses.

## Project Structure

*   `smart_city/`: Project configuration and variables.
*   `accounts/`: Handles user authentication (login, register).
*   `issues/`: Core functionality for reporting, listing, and managing issues.
*   `templates/`: HTML templates for the application.
