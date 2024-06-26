﻿# blogging-application

# blogging-application

Welcome to our blogging application repository! This project is a backend implementation written in Django Python, designed to facilitate a comprehensive blogging experience. Users can create accounts, authenticate themselves with a JWT (JSON Web Token), and then seamlessly interact with the platform to write and manage blogs, comment on posts, and search for specific content.

## Features

- **User Authentication**: Utilizes a robust authentication system powered by Django, generating JWT tokens for secure user access.
- **Blog Management**: Users can create, edit, and delete their blogs.
- **Comments**: Enables users to engage with blog posts by commenting on them.
- **Search Functionality**: Allows users to search for specific content based on keywords within comments.
- **Technologies Used**: Django, Simple JWT (JSON Web Token), Django REST Framework, Serializer.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/iaryangoyal/blogging-application.git
```

2. Navigate to the project directory:

```bash
cd blogging-application
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Access the application in your web browser at `http://localhost:8000`.

## Usage

- **User Authentication**: Upon registration, users receive a JWT token for accessing the application's features.
- **Creating a Blog**: Logged-in users can create new blog posts.
- **Editing Blogs**: Users can edit their own blog posts.
- **Commenting**: Users can comment on blog posts.
- **Searching**: Users can search for specific content based on keywords within comments.

## Contributors

- [Aryan Goyal](https://github.com/iaryangoyal)
