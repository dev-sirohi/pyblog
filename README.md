# Blog Platform

A blog platform backend built with FastAPI and PostgreSQL, featuring JWT cookie-based auth, rate limiting, and Firebase Storage for media. Content is written and stored as Markdown with image UUIDs referencing Firebase Storage assets.

## Stack

- **Backend:** FastAPI, SQLAlchemy (async), Alembic
- **Database:** PostgreSQL (asyncpg)
- **Media Storage:** Firebase Storage
- **Auth:** JWT via HTTP-only cookies
- **Rate Limiting:** SlowAPI

## Project Structure

```
├── src/
│   ├── dtos/
│   ├── models/
│   ├── routers/
│   │   └── v1/
│   ├── services/
│   └── main.py
├── pyblog_frontend/
├── alembic/
├── .env.example
├── Dockerfile
└── docker-compose.yml
```

## Setup

1. **Clone the repo**
   ```bash
   git clone <repo-url>
   cd <project>
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Fill in values
   ```

5. **Run migrations**
   ```bash
   alembic upgrade head
   ```

6. **Start server**
   ```bash
   uvicorn src.main:app --reload
   ```

## Environment Variables

```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
SECRET_KEY=your_secret_key
ALGORITHM=HS256
GOOGLE_APPLICATION_CREDENTIALS=./serviceAccountKey.json
```

## API

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/v1/auth/register` | No | Register |
| POST | `/api/v1/auth/login` | No | Login |
| POST | `/api/v1/auth/logout` | Yes | Logout |
| GET | `/api/v1/post/{id}` | No | Get post |
| POST | `/api/v1/post/` | Yes | Create post |
| PUT | `/api/v1/post/{id}` | Yes | Update post |
| DELETE | `/api/v1/post/{id}` | Yes | Delete post |
| POST | `/api/v1/post/{id}/like` | Yes | Like post |
| DELETE | `/api/v1/post/{id}/like` | Yes | Unlike post |
| GET | `/api/v1/feed` | No | Get feed |

## Media

Images are uploaded to Firebase Storage. The returned UUID is embedded in Markdown:

```md
![alt text](image_uuid)
```

The frontend resolves UUIDs to Firebase Storage URLs at render time.
