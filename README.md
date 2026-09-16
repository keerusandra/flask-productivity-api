# Flask Productivity API

## Overview

A backend REST API built with Flask for a productivity application. The API provides user authentication and allows authenticated users to manage their own productivity notes.

## Features

* User registration
* User login
* JWT authentication
* Protected API routes
* Create productivity notes
* View productivity notes
* Update productivity notes
* Delete productivity notes
* User ownership and access control
* Pagination for notes
* Database persistence
* Database migrations

## Technologies

* Python 3.8.10
* Flask
* Flask-SQLAlchemy
* Flask-JWT-Extended
* SQLite
* Alembic / Flask-Migrate
* Pytest
* Postman

## API Endpoints

### Authentication

| Method | Endpoint    | Description              |
| ------ | ----------- | ------------------------ |
| POST   | `/register` | Register a new user      |
| POST   | `/login`    | Log in and receive a JWT |

### Notes

| Method | Endpoint      | Description                             |
| ------ | ------------- | --------------------------------------- |
| GET    | `/notes`      | Retrieve the authenticated user's notes |
| POST   | `/notes`      | Create a new note                       |
| GET    | `/notes/<id>` | Retrieve a specific note                |
| PATCH  | `/notes/<id>` | Update a note                           |
| DELETE | `/notes/<id>` | Delete a note                           |

## Authentication

Protected endpoints require a JWT access token.

In Postman, select:

**Authorization → Bearer Token**

and provide the token returned by the login endpoint.

## Example Note

```json
{
  "title": "Finish Flask Lab",
  "content": "Complete API testing and documentation."
}
```

## Pagination

The notes endpoint supports pagination using query parameters such as:

```text
/notes?page=1&per_page=2
```

## Testing

Run the automated tests with:

```bash
pytest
```

## Running the Application

Start the Flask development server using the project's configured Flask entry point.

The API is available locally at:

```text
http://127.0.0.1:5000
```

## Project Purpose

This project demonstrates authentication, authorization, CRUD operations, database relationships, ownership controls, pagination, and REST API development using Flask.
