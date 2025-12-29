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

### 1. Standard Response Payload Structure
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

### 2. Comprehensive Logging System
I will have added a robust logging system that includes:
- **Request/Response Logging:** All API requests and responses logged with timestamps
- **Error Logging:** Detailed error logs with full stack traces for debugging
- **Performance Logging:** Track response times to identify performance bottlenecks
- **Audit Trail:** Complete logging of all book borrow/return operations for compliance and security

This logging infrastructure will be essential for debugging production issues, monitoring performance, and maintaining security audit trails.

### 3. Standard Error Response Handler
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

### 4. Caching Layer Implementation
I will have implemented a comprehensive caching strategy:
- **Response Caching:** Cache frequently accessed data like book lists and user information
- **Redis Integration:** Use Redis for distributed caching in production environments
- **Cache Invalidation:** Smart cache invalidation strategies when data is updated
- **TTL Management:** Appropriate time-to-live settings for different data types

This will significantly improve API response times, reduce server load, and enhance scalability for high-traffic scenarios.

### 5. Additional Production-Ready Features

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

#### DevOps & Deployment
- Docker containerization for consistent deployments
- Docker Compose setup for local development
- CI/CD pipeline for automated testing and deployment
- Environment-based configuration management
- Secure secrets management

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

### Installation
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run the Server
```bash
python manage.py runserver
```

### API Endpoints
- `POST /api/books/` - Create a book
- `POST /api/users/` - Register a user
- `POST /api/borrow/` - Borrow a book
- `GET /api/users/<user_id>/borrowed/` - Get user's borrowed books

