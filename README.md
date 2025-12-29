# Library API - Assessment Question

## Python Coding Task — Build a Simple Library API

You have 50 minutes to build a simple Library API where users can borrow books.
Please use a Python backend framework — such as Flask, FastAPI, or Django.
(You must use Python — not Node.js or another language.)

### 1. Add a Book
**Endpoint:** POST /books
**Input (JSON):**
```json
{ "title": "Book Title", "author": "Book Author" }
```

**Output:** The created book object with an auto-generated id.

### 2. Register a User
**Endpoint:** POST /users
**Input (JSON):**
```json
{ "name": "Alice" }
```

**Output:** The created user object with an auto-generated id.

### 3. Borrow a Book
**Endpoint:** POST /borrow
**Input (JSON):**
```json
{ "userId": 1, "bookId": 2 }
```

**Rules:**
- A book can only be borrowed if it's not already borrowed.
- **Output:** A confirmation message like:
```json
{"message": "Book borrowed successfully"}
```

### 4. List Borrowed Books by User
**Endpoint:** GET /users/:id/borrowed
**Output:** A list of all books borrowed by that user.

## What We're Looking For
- Clear, correct implementation of the above rules.
- Code that runs without errors.
- Simple, readable structure.
- Ability to explain your decisions.

## Notes
- Use in-memory storage (e.g., Python lists or dictionaries).
- No database setup required.

If you finish early, you can add extras like:
- Returning a book
- Input validation and error messages
- Preventing invalid user/book IDs

---

## What I Will Have Done Better in a Production-Level Application

Beyond the basic requirements, here are the key improvements I will have implemented to make this a production-ready application:

### 1. Serializers for Input Validation and Fast Error Detection
I will have implemented Django REST Framework serializers to validate all input data before processing, catching errors early and providing clear, structured error messages. This approach validates data at the API boundary, preventing invalid data from reaching business logic.

**Example Serializer Implementation:**

```python
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(
        required=True,
        max_length=200,
        error_messages={
            'required': 'Title is required',
            'max_length': 'Title cannot exceed 200 characters'
        }
    )
    author = serializers.CharField(
        required=True,
        max_length=100,
        error_messages={
            'required': 'Author is required',
            'max_length': 'Author name cannot exceed 100 characters'
        }
    )

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(
        required=True,
        min_length=2,
        max_length=100,
        error_messages={
            'required': 'Name is required',
            'min_length': 'Name must be at least 2 characters',
            'max_length': 'Name cannot exceed 100 characters'
        }
    )

class BorrowBookSerializer(serializers.Serializer):
    userId = serializers.IntegerField(
        required=True,
        min_value=1,
        error_messages={
            'required': 'userId is required',
            'invalid': 'userId must be a valid integer',
            'min_value': 'userId must be a positive number'
        }
    )
    bookId = serializers.IntegerField(
        required=True,
        min_value=1,
        error_messages={
            'required': 'bookId is required',
            'invalid': 'bookId must be a valid integer',
            'min_value': 'bookId must be a positive number'
        }
    )
```

**Example Usage in Views:**

```python
class BookCreateView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({
                'success': False,
                'error': {
                    'message': 'Validation failed',
                    'code': 'VALIDATION_ERROR',
                    'details': serializer.errors
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Data is guaranteed to be valid here
        validated_data = serializer.validated_data
        # ... create book logic
```

**Benefits:**
- **Fast Error Detection:** Invalid data is caught immediately at the API boundary before any processing
- **Structured Error Messages:** Clear, field-specific error messages help frontend developers fix issues quickly
- **Type Safety:** Automatic type conversion and validation (e.g., string to integer)
- **Reusable Validation Logic:** Serializers can be reused across different views
- **Better Developer Experience:** Consistent validation patterns throughout the application
- **Security:** Prevents malformed data from reaching business logic, reducing potential security vulnerabilities

### 2. Standard Response Payload Structure
I will have implemented a consistent response structure across all endpoints to ensure better frontend integration and developer experience. All successful responses will follow this format:
```json
{
  "success": true,
  "message": "Operation completed successfully",
  "data": {
    // Response data here
  }
}
```

This standardization makes it easier for frontend developers to handle responses consistently, improves error handling, and provides a better API contract.

### 3. Comprehensive Logging System
I will have added a robust logging system that includes:
- **Request/Response Logging:** All API requests and responses logged with timestamps
- **Error Logging:** Detailed error logs with full stack traces for debugging
- **Performance Logging:** Track response times to identify performance bottlenecks
- **Audit Trail:** Complete logging of all book borrow/return operations for compliance and security

This logging infrastructure will be essential for debugging production issues, monitoring performance, and maintaining security audit trails.

### 4. Standard Error Response Handler
I will have created a custom exception handler that ensures all errors return a consistent structure:
```json
{
  "success": false,
  "error": {
    "message": "Error message here",
    "code": "ERROR_CODE",
    "details": null,
    "status_code": 400
  }
}
```

This provides consistent error handling across all endpoints, making it easier for frontend applications to handle errors uniformly and improving the overall developer experience.

### 5. Caching Layer Implementation
I will have implemented a comprehensive caching strategy:
- **Response Caching:** Cache frequently accessed data like book lists and user information
- **Redis Integration:** Use Redis for distributed caching in production environments
- **Cache Invalidation:** Smart cache invalidation strategies when data is updated
- **TTL Management:** Appropriate time-to-live settings for different data types

This will significantly improve API response times, reduce server load, and enhance scalability for high-traffic scenarios.

### 6. Additional Production-Ready Features

#### Input Validation & Sanitization
- Comprehensive request data validation using Django serializers
- Protection against SQL injection attacks
- XSS (Cross-Site Scripting) protection
- Input sanitization for all user inputs

#### Security Enhancements
- Proper CORS configuration for cross-origin requests
- Rate limiting to prevent API abuse
- JWT-based authentication and authorization
- API key management system
- Request throttling to protect against DDoS attacks

#### Database Integration
- Migration from in-memory storage to PostgreSQL for production
- Database migrations for schema management
- Connection pooling for better performance
- Query optimization and indexing

#### API Documentation
- OpenAPI/Swagger documentation for all endpoints
- Interactive API explorer for testing
- Detailed endpoint descriptions with examples
- Complete request/response schema documentation

#### Comprehensive Testing
- Unit tests covering all endpoints and business logic
- Integration tests for end-to-end workflows
- Test coverage reports to ensure code quality
- Automated testing integrated into CI/CD pipeline

#### Monitoring & Observability
- Health check endpoints for service monitoring
- Metrics collection using Prometheus
- Distributed tracing for request tracking
- Error tracking integration with Sentry

#### Performance Optimization
- Database query optimization with proper indexing
- Pagination for list endpoints to handle large datasets
- Async task processing using Celery for background jobs
- Background job processing for long-running operations

#### Code Quality Standards
- Type hints throughout the codebase for better IDE support
- Code formatting using Black
- Linting with Flake8/Pylint
- Pre-commit hooks to enforce code quality

#### Docker Containerization
I will have implemented Docker containerization to ensure consistent deployments across all environments. This includes:
- **Dockerfile:** Optimized multi-stage build for production-ready images
- **Docker Compose:** Complete development environment setup with all services
- **Container Orchestration:** Easy scaling and deployment management
- **Environment Isolation:** Consistent runtime environment regardless of host system
- **Dependency Management:** All dependencies bundled in the container

**Example Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

**Example docker-compose.yml:**
```yaml
version: '3.8'

services:
  backend:
    build: .
    container_name: django_backend
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DEBUG=1
    command: python manage.py runserver 0.0.0.0:8000
```

**Benefits:**
- Consistent development and production environments
- Easy onboarding for new developers
- Simplified deployment process
- Isolation from host system dependencies
- Reproducible builds across different machines

#### DevOps & Deployment
- CI/CD pipeline for automated testing and deployment
- Environment-based configuration management
- Secure secrets management
- Automated backup and recovery procedures

#### Enhanced API Features
- Return book functionality
- Real-time book availability status
- Complete user borrowing history
- Advanced search and filtering capabilities
- Pagination and sorting for all list endpoints

These enhancements will transform the basic assessment implementation into a robust, scalable, and production-ready application that can handle real-world usage scenarios.

---

## Project Structure
```
backend/
├── config/           # Django project configuration
├── library/          # Library app with views, models, serializers
├── manage.py
├── requirements.txt
└── README.md
```

## Getting Started

### Option 1: Using Docker (Recommended)

#### Prerequisites
- Docker installed on your system
- Docker Compose installed (usually comes with Docker Desktop)

#### Run with Docker Compose
```bash
cd backend
docker-compose up --build
```

The API will be available at `http://localhost:8000`

#### Run in Detached Mode
```bash
docker-compose up -d --build
```

#### Stop the Container
```bash
docker-compose down
```

#### View Logs
```bash
docker-compose logs -f
```

#### Rebuild After Changes
```bash
docker-compose up --build
```

### Option 2: Local Installation

#### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

#### Installation
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Run the Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

### API Endpoints
- `POST /api/books/` - Create a book
- `POST /api/users/` - Register a user
- `POST /api/borrow/` - Borrow a book
- `GET /api/users/<user_id>/borrowed/` - Get user's borrowed books

