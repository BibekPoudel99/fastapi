# FastAPI Blog API

> A RESTful backend API built with FastAPI for managing users, posts, authentication, and voting.

## Highlights

- Built with **FastAPI** for fast, modern API development.
- Uses **PostgreSQL** and **SQLAlchemy** for persistent data storage and ORM-based database access.
- Secured with **JWT authentication** and password hashing using **bcrypt**.
- Managed with **Alembic** for database migrations.
- Container-friendly with **Docker** and **Docker Compose**.

## Tech Stack

- **Backend:** FastAPI, Python, Uvicorn
- **Database:** PostgreSQL, SQLAlchemy
- **Validation:** Pydantic
- **Security:** JWT, Passlib, bcrypt
- **Migrations:** Alembic
- **Deployment:** Docker, Docker Compose

## Features

- User registration and login
- JWT-based authentication
- Create, read, update, and delete posts
- Vote system for posts
- Request validation with Pydantic
- Database modeling with SQLAlchemy
- Database migrations with Alembic
- CORS support for frontend integration

## What I Learned

This project helped me build practical knowledge in:

- Designing REST APIs with FastAPI
- Structuring a backend project with routers, schemas, models, and utilities
- Connecting Python applications to PostgreSQL with SQLAlchemy
- Building relational database models and working with ORM relationships
- Securing endpoints with JWT authentication
- Hashing and verifying passwords with bcrypt
- Running database migrations with Alembic
- Validating request data and shaping API responses with Pydantic
- Using Docker for consistent development and deployment

## Project Structure

- `app/main.py` - application entry point
- `app/model.py` - database models
- `app/schemas.py` - request and response schemas
- `app/database.py` - database session and engine setup
- `app/oauth2.py` - JWT authentication helpers
- `app/utils.py` - password hashing utilities
- `app/routers/` - API route handlers for auth, users, posts, and votes

## Getting Started

### Prerequisites

- Python 3.13+
- PostgreSQL
- `pip`

### Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your environment variables in a `.env` file:

```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=your_password
DATABASE_NAME=fastapi
DATABASE_USERNAME=postgres
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at http://127.0.0.1:8000

### Using Docker

```bash
docker-compose up --build
```

## API Overview

- `POST /users/` - register a new user
- `POST /login` - authenticate and receive a JWT token
- `GET /posts/` - list posts
- `POST /posts/` - create a post
- `GET /posts/{id}` - get a single post
- `PUT /posts/{id}` - update a post
- `DELETE /posts/{id}` - delete a post
- `POST /vote/` - vote on a post

## License

This project is for learning and portfolio purposes.