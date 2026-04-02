
# Coordination Specification

This document outlines the technical specifications for the project.

## Backend

- **Tech Stack:** FastAPI, PostgreSQL, SQLAlchemy
- **Directory:** `backend/`
- **API Contract:**
  - **Health Check:**
    - Method: `GET`
    - Path: `/health`
    - Response: `{"status": "ok"}`
  - **JWT Authentication:**
    - **Get Token:**
      - Method: `POST`
      - Path: `/token`
      - Request Body: `{"username": "user", "password": "password"}`
      - Response: `{"access_token": "your-token", "token_type": "bearer"}`
    - **Protected Route Example:**
      - Method: `GET`
      - Path: `/users/me`
      - Response: `{"username": "user"}`
- **Database:**
  - **Type:** PostgreSQL
  - **Connection String:** To be managed by the backend agent.
- **Environment Variables:**
  - `DATABASE_URL`: The connection string for the PostgreSQL database.
  - `SECRET_KEY`: A secret key for JWT token generation.
- **Testing:** The agent should include unit and integration tests for the API.

