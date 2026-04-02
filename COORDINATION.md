# COORDINATION.md

This document outlines the coordination spec for the `my-app1` project.

## Backend Tech Stack

*   **Language:** Python
*   **Framework:** FastAPI
*   **Authentication:** JWT
*   **Database:** PostgreSQL
*   **ORM:** SQLAlchemy

## Database Configuration

*   **Host:** `localhost`
*   **Port:** `5432`
*   **Username:** `user`
*   **Password:** `password`
*   **Database Name:** `app`

## API Contract

### Endpoints

*   **Health Check:**
    *   **Method:** `GET`
    *   **Path:** `/health`
    *   **Response:**
        *   **Status Code:** 200 OK
        *   **Body:** `{"status": "ok"}`

*   **Authentication:**
    *   **Login:**
        *   **Method:** `POST`
        *   **Path:** `/login`
        *   **Request Body:** `{"username": "user", "password": "password"}`
        *   **Response:**
            *   **Status Code:** 200 OK
            *   **Body:** `{"access_token": "your_jwt_token"}`
    *   **Signup:**
        *   **Method:** `POST`
        *   **Path:** `/signup`
        *   **Request Body:** `{"username": "user", "password": "password"}`
        *   **Response:**
            *   **Status Code:** 201 Created
            *   **Body:** `{"message": "User created successfully"}`

## Environment Variables

*   `DATABASE_URL`: The connection string for the PostgreSQL database.
*   `SECRET_KEY`: The secret key for JWT token encoding and decoding.
