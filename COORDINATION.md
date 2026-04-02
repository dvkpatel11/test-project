
# Coordination Specification

This document outlines the technical specifications for the project, serving as the single source of truth for all agents.

## Backend

- **Tech Stack:** FastAPI, Python
- **Database:** PostgreSQL with SQLAlchemy
- **Authentication:** JWT (JSON Web Tokens)

### Database Configuration

- **Connection String:** `postgresql://user:password@localhost/db`
- **Tables:**
    - `users`:
        - `id` (Integer, Primary Key)
        - `username` (String, Unique)
        - `hashed_password` (String)

## Frontend

- **Tech Stack:** To be determined by the frontend agent.

## API Contract

### Authentication

- **POST** `/token`
    - **Request Body:** `username`, `password`
    - **Response Body:** `access_token`, `token_type`

### Health Check

- **GET** `/health`
    - **Response Body:** `{"status": "ok"}`
