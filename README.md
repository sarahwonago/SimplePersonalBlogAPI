# Simple Personal Blog API
This Simple Personal Blog backend API is built using Django and Django Rest Framework (DRF) that powers a personal blogging platform. The API allows users to create, update, delete, and retrieve blog articles. Users can also filter articles based on tags or publication status. This API can be consumed by frontend applications like React, mobile apps, or other clients that need a blog feature.

**Features**
## What the Project Does:
1. Authentication: The project includes user authentication using JWT authentication.
2. List Articles: Retrieve a list of all published/unpublished articles.
3. Filter Articles: Apply filters by tags and publication status.
4. Create New Articles: Authenticated users can create and publish new articles.
5. View a Single Article: Retrieve details of a specific article by its ID.
6. Update Articles: Authenticated users can update the content or metadata of existing articles by specifying the article ID.
7. Delete Articles: Authenticated users can delete an article by its ID.

## What the Project Does Not Do:
1. No Frontend: This project is a backend API only. It does not include a frontend for interacting with the articles (e.g., no HTML views, no JavaScript).

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

5. Run the development server 
`python manage.py runserver`

6. The API will be accessible at http://127.0.0.1:8000/api/


## API Endpoints
| Method | Endpoint | Description |
| ----------- | ----------- || ----------- |
| GET	| /api/articles/	| Retrieve a list of articles |
| GET	| /api/articles/<id>/	| Retrieve a specific article by ID |
| POST	| /api/articles/	| Create a new article (authenticated users) |
| PUT	| /api/articles/<id>/	| Update an article by ID (authenticated) |
| DELETE | /api/articles/<id>/	| Delete an article by ID (authenticated) |
| GET   | /api/schema/ | Provides access to the OpenAPI schema |
| GET   | /api/docs/swagger/ | Serves the Swagger UI interface |
| GET   | /api/docs/redoc | Serves the Redoc documentation interface |


## Query Parameters
- published: Filter articles by their publication status (true/false).
Example: /api/articles/?published=true
- tags: Filter articles by specific tags.
Example: /api/articles/?tags=django

## Technology Stack
- Backend Framework: Django (5.x)
- API Framework: Django Rest Framework (3.x)
- Database: SQLite (default, but can be replaced with PostgreSQL or MySQL)
- Authentication: (DRF’s simpleJWT  Token Authentication )
- Deployment: 
- Testing: Can be tested using Postman or cURL

## How to Use
1. Create an Article
To create a new article, send a POST request to /api/articles/ with the following JSON payload:
```

{
    "title": "New Article",
    "content": "This is the content of the new article.",
    "published": true,
    "tags": "django,api"
}

```

2. Update an Article
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