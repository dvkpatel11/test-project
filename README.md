# my-app2

This is the main README for my-app2. 

## Project Overview

This project is a FastAPI REST API with JWT authentication, a PostgreSQL database, and a health check endpoint. 

## Quickstart

1.  Clone the repository
2.  `cp .env.example .env`
3.  `make up`

## Architecture

```
+-----------------+      +-----------------+      +-----------------+
|     Frontend    |----->|     Backend     |----->|   PostgreSQL    |
| (React/Vue/etc) |      |    (FastAPI)    |      |    (Database)   |
+-----------------+      +-----------------+      +-----------------+
                                  |
                                  |
                                  v
                            +-----------------+
                            |      Redis      |
                            |     (Cache)     |
                            +-----------------+
```

## Backend

See the [backend README](../backend/README.md) for more information.

## Frontend

See the [frontend README](../frontend/README.md) for more information.
