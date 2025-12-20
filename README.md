  

---

# ResumeMatch Scoring API

This is a backend project built using Django and Django REST Framework.  
The goal of this project is to simulate a real job application system where users can upload resumes, apply for jobs, and receive a similarity score between their resume and the job description.

This project is backend-focused. There is no frontend UI.

---

## What this project does

- User registration and login using JWT authentication
- Resume upload (PDF)
- Background resume parsing using Celery
- Job creation and management (admin controlled)
- Job application tracking
- Resume vs Job Description similarity scoring
- API documentation using Swagger

---

## Tech stack used

- Python
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- Celery for background tasks
- Redis as message broker
- SQLite (local development)
- PostgreSQL (production)
- Swagger (drf-yasg)

---

## Project structure

core/
├── __init__.py  
├── asgi.py  
├── celery.py  
├── settings.py  
├── urls.py  
├── wsgi.py  

accounts/
├── admin.py  
├── apps.py  
├── managers.py  
├── models.py  
├── serializers.py  
├── urls.py  
├── views.py  

resumes/
├── admin.py  
├── apps.py  
├── models.py  
├── serializers.py  
├── tasks.py  
├── urls.py  
├── views.py  

jobs/
├── admin.py  
├── apps.py  
├── models.py  
├── serializers.py  
├── urls.py  
├── views.py  

applications/
├── admin.py  
├── apps.py  
├── models.py  
├── serializers.py  
├── tasks.py  
├── urls.py  
├── utils.py  
├── views.py  

media/  
requirements.txt  
manage.py  

---

## Authentication

Authentication is handled using JWT.

After login, the client receives:
- Access token
- Refresh token

All protected endpoints require the access token in the request header:

```
Authorization: Bearer <access_token>
```
---
## Resume upload and processing
- User uploads a resume in PDF format
- File is saved immediately
- Resume text extraction runs in the background using Celery
- Parsed text is stored in the database

This asynchronous approach prevents blocking API requests.
---
## Job application flow
1. User uploads a resume
2. User applies for a job
3. Resume text is compared with the job description
4. A similarity score is calculated and stored
5. Application status is saved

Similarity scores vary depending on the resume content and job description.
---
## Background tasks (Celery)

Celery is used for:
- Resume parsing
- Application-related background tasks

Redis is used as the message broker.
---
## API documentation
Swagger UI is available at:
```
/swagger/
```
Swagger supports:
- JWT authorization
- File upload testing
- API request and response inspection

Swagger is used for API documentation and testing.
---
## Environment variables

All sensitive values are stored in environment variables and are not committed to GitHub.
```
DJANGO_SECRET_KEY
DEBUG
DJANGO_ALLOWED_HOSTS
CELERY_BROKER_URL
EMAIL_HOST
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
```
The `.env` file is excluded using `.gitignore`.
---
## Local setup
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Start Redis:
```
redis-server
```
Start Celery worker:
```
celery -A core worker -l info
```
---
## Deployment
- Environment variables are configured on the hosting platform (Render)
- SQLite is replaced with PostgreSQL in production
```

 
