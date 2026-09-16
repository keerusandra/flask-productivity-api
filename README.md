# Flask Productivity API

A backend REST API for a productivity application built with Flask. The application provides user authentication with JWTs and allows authenticated users to create and manage their own notes.

## Features

* User registration
* User login
* JWT authentication
* Protected API endpoints
* Password hashing with Flask-Bcrypt
* Create notes
* View notes
* Update notes
* Delete notes
* User ownership and access control
* Pagination for notes
* SQLite database
* Flask-Migrate database migrations
* RESTful API endpoints
* Deployment with Gunicorn and Render

## Technologies

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Flask-JWT-Extended
* Flask-Bcrypt
* SQLite
* Gunicorn
* Render

## Project Structure

```text
flask-productivity-api/
├── README.md
├── requirements.txt
├── Pipfile
└── server/
    ├── app.py
    ├── extensions.py
    ├── models.py
    └── migrations/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/keerusandra/flask-productivity-api.git
```

Navigate into the project directory:

```bash
cd flask-productivity-api
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application Locally

Navigate to the server directory:

```bash
cd server
```

Run the Flask application:

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## Authentication

The API uses JSON Web Tokens (JWT) to protect authenticated endpoints.

After successfully logging in, the API returns an access token.

Include the token in requests to protected endpoints using the following Authorization header:

```text
Authorization: Bearer <access_token>
```

## API Endpoints

### Home

**GET** `/`

Returns the API status.

### Register

**POST** `/register`

Creates a new user.

Example request:

```json
{
    "username": "testuser",
    "password": "password123"
}
```

### Login

**POST** `/login`

Authenticates a user and returns a JWT access token.

Example request:

```json
{
    "username": "testuser",
    "password": "password123"
}
```

### Check Authentication

**GET** `/check_session`

Returns information about the currently authenticated user.

Requires a valid JWT.

### Get Notes

**GET** `/notes`

Returns notes belonging to the authenticated user.

Pagination is supported using:

```text
/notes?page=1&per_page=5
```

### Create Note

**POST** `/notes`

Creates a new note for the authenticated user.

Example request:

```json
{
    "title": "My Note",
    "content": "This is my productivity note."
}
```

### Update Note

**PATCH** `/notes/<id>`

Updates a note belonging to the authenticated user.

Example request:

```json
{
    "title": "Updated Note",
    "content": "Updated note content."
}
```

### Delete Note

**DELETE** `/notes/<id>`

Deletes a note belonging to the authenticated user.

## Authorization and Ownership

Notes are associated with the user who created them.

Authenticated users can only view, update, or delete their own notes. Attempts to access another user's note return a `404` response.

## Pagination

The notes endpoint supports pagination.

Example:

```text
GET /notes?page=1&per_page=5
```

The response includes:

* Current page
* Items per page
* Total number of notes
* Total number of pages

## Database

The application uses SQLite for data storage.

Database migrations are managed using Flask-Migrate.

## Deployment

The application has been deployed remotely using Render.

**Live API:**

https://flask-productivity-api-4.onrender.com

The root endpoint should return:

```json
{
    "message": "Flask Productivity API is running"
}
```

## Production Server

The deployed application uses Gunicorn as the WSGI server.

Render uses the following start command:

```bash
gunicorn --chdir server app:app
```

## Requirements

Project dependencies are listed in:

```text
requirements.txt
```

Install them with:

```bash
pip install -r requirements.txt
```

## Testing

API endpoints can be tested using Postman.

Authentication-protected endpoints require the JWT access token returned from the login endpoint.

## Author

Flask Productivity API project developed as part of a Flask backend development lab assignment.