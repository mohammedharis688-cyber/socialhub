# SocialHub

## Overview

SocialHub is a multi-platform social media management backend application developed using FastAPI and PostgreSQL. The goal of the project is to allow users to create content once and publish it across multiple social media platforms from a single interface.

The current version supports user authentication, media uploads, post management, platform connections, and publishing to Telegram and Discord. The architecture is designed to be scalable so that additional platforms such as LinkedIn, Facebook, Instagram, and X can be integrated without major code changes.

---

## Features

### User Management

* User Registration
* User Login
* JWT Authentication
* Protected API Endpoints
* Current User Information Endpoint

### Post Management

* Create Posts
* View User Posts
* Store Draft Posts
* Associate Media with Posts

### Media Management

* Upload Documents
* Upload Images
* Store Media Metadata
* Attach Multiple Media Files to a Post

### Social Platform Integration

* Telegram Integration
* Discord Integration
* Connect Platforms
* View Connected Platforms
* Publish to Individual Platforms
* Publish to All Connected Platforms

### Architecture Features

* Provider-Based Design
* Scalable Multi-Platform Publishing
* Environment Variable Configuration
* Service Layer Separation
* Router-Based API Structure

---

## Technology Stack

### Backend

* FastAPI
* Python 3

### Database

* PostgreSQL
* SQLAlchemy ORM

### Authentication

* JWT (JSON Web Tokens)
* Passlib (Bcrypt)

### Integrations

* Telegram Bot API
* Discord Webhooks

### Development Tools

* Git
* GitHub
* Swagger UI

---

## Project Structure

```text
app/
│
├── routers/
│   ├── users.py
│   ├── posts.py
│   └── social_accounts.py
│
├── services/
│   ├── telegram_service.py
│   └── discord_service.py
│
├── providers/
│   ├── telegram.py
│   ├── discord.py
│   └── provider_registry.py
│
├── auth.py
├── config.py
├── database.py
├── models.py
├── schemas.py
└── main.py
```

---

## Database Entities

### User

Stores user account information.

### Post

Stores post content and publishing status.

### Media

Stores uploaded files and images.

### SocialAccount

Stores connected social media platforms.

### PostMedia

Junction table used to maintain many-to-many relationships between posts and media.

---

## API Endpoints

### User APIs

```text
POST   /users/register
POST   /users/login
GET    /users/me
```

### Post APIs

```text
POST   /posts/
GET    /posts/
POST   /posts/upload
POST   /posts/{post_id}/publish/{platform}
POST   /posts/{post_id}/publish-all
```

### Social Account APIs

```text
POST   /social/connect/{platform}
GET    /social/accounts
```

---

## Current Workflow

```text
User Login
    ↓
Create Post
    ↓
Upload Media
    ↓
Attach Media to Post
    ↓
Connect Platforms
    ↓
Publish Post
    ↓
Telegram / Discord
```

---

## Future Enhancements

* LinkedIn OAuth Integration
* Facebook Integration
* Instagram Integration
* X (Twitter) Integration
* Scheduled Publishing
* Cloud Storage (S3 / MinIO)
* AI Content Generation
* Frontend Dashboard
* Analytics and Reporting
* Multi-User Workspace Support

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file and configure:

```env
DATABASE_URL=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
DISCORD_WEBHOOK_URL=
```

### Run Application

```bash
uvicorn app.main:app --reload
```

### Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## Current Project Status

Version: 1.0 (Development Phase)

Completed:

* Authentication System
* Media Upload System
* Telegram Integration
* Discord Integration
* Social Account Management
* Multi-Platform Publishing

In Progress:

* LinkedIn OAuth Integration
* Additional Social Media Providers
