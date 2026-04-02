
# Coordination Spec

## Backend Tech Stack & DB Config

- FastAPI
- JWT authentication
- PostgreSQL database
- SQLAlchemy ORM

## Frontend Tech Stack

- Not specified

## API Contract

### Health Check
- **GET /health**:
  - **Request**: None
  - **Response**: `{"status": "ok"}`
  - **Status Code**: 200

### Authentication (to be implemented by backend-dev)
- Endpoints for token creation, refresh, and verification.

## Environment Variables and Ports

- **DATABASE_URL**: PostgreSQL connection string.
- **JWT_SECRET**: Secret key for JWT encoding and decoding.
- **PORT**: `8000` (backend)
