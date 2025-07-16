# Django To-Do App

This is a To-Do list web application build with the Django framework. Users can use this to manage personal tasks using CRUD functions. This app features user authentication as well as an email reminder system.

## Features

**User Authentication:**

- User registration
- Login and Logout

**Task Management:**

- Create: Add new tasks with a title, description(optional), due date, priority, and completion status.
- Read: View a list of all tasks including overdue tasks
- Update: Options to edit existing tasks
- Delete: Remove tasks after being sent to custom confirmation page

**Overdue Task Tracking:** Using a custom Django manager, tasks that are overdue are displayed prominently.

**Email Reminders:** Automated email reminders using Django signals are used to notify users for tasks an hour before due.

## Tech Stack

- Backend: Python, Django
- Database: Default SQLite
- Frontend: HTML, CSS

## Setup

1. Clone Repo

- git clone

2. Create Venv

- python3 -m venv .venv
- source. venv/bin/activate

3. Install Dependencies

- pip install Django

4. Run Database migrations

- python manage.py migrate

5. Create Superuser

- python manage.py createsuperuser

6. Run Dev Server

- python manage.py runserver

## Usage

1. Open browser via development server link
2. Home Screen:

- Login/Register
- You can log in using the superuser, or you can register. Choose your path via the Home screen

3. Creating/Managing Tasks:

- After login/registration you will be sent to the task list
- Create tasks, Edit tasks, and even delete tasks
- To test overdue tasks, create a task with a past due date and they will appear in their own list
- To test email reminders when creating or editing a task set it with a due date within the next hour. The reminder email will be printed to your terminal for easier testing.
