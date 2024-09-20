# Simple Personal Blog API with JWT Authentication
This Simple Personal Blog backend API is built using Django and Django Rest Framework (DRF) that powers a personal blogging platform. The API allows users to create, update, delete, and retrieve blog articles. Users can also filter articles based on tags or publication status. This API can be consumed by frontend applications like React, mobile apps, or other clients that need a blog feature.


**Features**
- **User Registration**: Users can register with their email, username, and password.
- **User Login**: Authenticated users can log in and receive access and refresh tokens.
- **JWT-based Authentication**: Protects routes using JWT tokens (access and refresh tokens).
- **Article Management**: Users can create, retrieve, update, and delete articles.
- **Token Blacklisting**: (Optional) Allows for revoking JWT tokens.
- **Swagger Documentation**: API documentation available via Swagger UI.


## What the Project Does:
1. Authentication- Allows users to register and authenticate via JWT tokens.Supports token refresh and (optionally) token blacklisting.
2. List Articles: Retrieve a list of all published/unpublished articles.
3. Filter Articles: Apply filters by tags and publication status.
4. Create New Articles: Authenticated users can create and publish new articles.
5. View a Single Article: Retrieve details of a specific article by its ID.
6. Update Articles: Authenticated users can update the content or metadata of existing articles by specifying the article ID.
7. Delete Articles: Authenticated users can delete an article by its ID.
8. Comment on articles
9. Share articles
10. Like articles

## What the Project Does Not Do:
1. No Frontend: This project is a backend API only. It does not include a frontend for interacting with the articles (e.g., no HTML views, no JavaScript).
2. This API does not handle OAuth2 or third-party login (e.g., Google, Facebook).
3. It does not encrypt the JWT token payload.

---

## Getting Started
**Prerequisites**
- Python 3.x
- Django 5.x
- Django Rest Framework 3.x

## Installation
1. Clone the repository
`git clone https://github.com/sarahwonago/SimplePersonalBlogAPI`
`cd simplepersonalblogAPI`

2. Create and activate a virtual environment
`python3 -m venv blog_env`
`source blog_env/bin/activate`

3. Install the dependencies
`pip install -r requirements.txt`

4. Apply database migrations
`python manage.py migrate`

5. Create a superuser
`python manage.py createsuperuser`

6. Run the development server 
`python manage.py runserver`

7. The API will be accessible at http://127.0.0.1:8000/api/


## API Endpoints

| Method | Endpoint                | Description                                          |
|--------|-------------------------|------------------------------------------------------|
| POST   | `/api/account/register/`           | Register a new user                       |
| POST   | `/api/account/login/`              | Login and get JWT tokens                  |
| POST   | `/api/account/token/refresh/`      | Refresh JWT access token                  |
| POST   | `/api/account/token/obtain/`      | Obtain JWT access/refresh token       |
| POST   | `/api/account/token/blacklist/`    | (Optional) Blacklist a JWT token          |
| GET    | `/api/blog/articles/`           | Retrieve a list of articles                       |
| GET    | `/api/blog/articles/<id>/`      | Retrieve a specific article by ID                 |
| POST   | `/api/blog/articles/`           | Create a new article (authenticated users)        |
| PUT    | `/api/blog/articles/<id>/`      | Update an article by ID (authenticated)           |
| DELETE | `/api/blog/articles/<id>/`      | Delete an article by ID (authenticated)           |
| GET    | `/api/schema/`             | Provides access to the OpenAPI schema             |
| GET    | `/api/docs/swagger/`       | Serves the Swagger UI interface                   |
| GET    | `/api/docs/redoc/`         | Serves the Redoc documentation interface          |



## Query Parameters
- published: Filter articles by their publication status (true/false).
Example: /api/articles/?published=true
- tags: Filter articles by specific tags.
Example: /api/articles/?tags=django

## Technology Stack
- **Backend**: Django, Django Rest Framework
- **Authentication**: JWT Authentication (via `djangorestframework-simplejwt`)
- **Documentation**: DRF Spectacular for OpenAPI (Swagger & Redoc)
- **Database**: SQLite (can be changed to PostgreSQL/MySQL for production)
- **Security Enhancements**: HTTPS, CORS, Token Blacklisting, Password Policies
- **Deployment**: 
- **Testing**: Can be tested using Postman or cURL


## Testing with Postman
1. Create an Article
To create a new article, send a POST request to /api/blog/articles/ with the following JSON payload:
```

{
    "title": "First Article",
    "tags": "#new",
    "body": "This is my First article"
}

```
Response:

```

{
  "id": "9f9f1f6c-cc57-437b-a9b5-6aca8d6aee87",
  "user": {
    "username": "zaza",
    "email": "zaza@gmail.com"
  },
  "title": "First Article",
  "tags": "#new",
  "body": "This is my First article"
}

```
2. Retrieve all Articles
To retrieve all articles, send a GET request to /api/blog/articles/ 

Response:

```

[
  {
    "id": "9f089128-eb64-4705-87ae-01f0217a9b71",
    "user": {
      "username": "zaza",
      "email": "zaza@gmail.com"
    },
    "title": "Second Article",
    "tags": "#new",
    "body": "This is my second article"
  },
  {
    "id": "156f4137-f9c5-4d45-8e4f-fca7a957dd61",
    "user": {
      "username": "zaza",
      "email": "zaza@gmail.com"
    },
    "title": "First Article",
    "tags": "#new",
    "body": "This is my first article"
  }
]

```

3. Update an Article
To update an existing article, send a PUT request to /api/articles/<id>/:

```

{
    "title": "Updated Title",
    "content": "This is the updated content.",
    "published": false,
    "tags": "drf,rest"
}


```

3. Delete an Article
To delete an article, send a DELETE request to /api/articles/<id>/.



4. **Register a User**: Send a POST request to /api/account/register/.
```

{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "TestPassword123!"
}



```

Response:
```

{
    "message": "User created successfully."
}

```

5. **Login**: Send a POST request to /api/account/login/ to get access and refresh tokens.
```

{
    "username": "testuser",
    "password": "TestPassword123!"
}



```

Response:
```

{
    "refresh": "your-refresh-token",
    "access": "your-access-token"
}

```

6. **Use JWT for Protected Routes**: Include the access token in the Authorization header for authenticated requests (Bearer <token>).
```

Authorization: Bearer <your-access-token>

```

## Future Enhancements
- Add User Roles: Yet to Implement different user roles like Admin, Author, and Reader with different permissions.
- Commenting System: Yet to Add functionality for readers to comment on articles.
- Image Uploads: Yet to Allow users to attach images to articles.
- Frontend: Yet to Build a user-friendly frontend using React, Vue, or any other framework.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
If you have any questions or feedback, feel free to reach out to me at ---