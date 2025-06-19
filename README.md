# SXC Network Community Backend

This is the backend service for the SXC Network Community platform, built with Django. It provides APIs and services to support community features such as user management, posts, comments, and more.

## Features

- User authentication and authorization
- CRUD operations for posts and comments
- Community management
- RESTful API design
- Secure and scalable architecture

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) (v3.8+)
- [pip](https://pip.pypa.io/)
- [virtualenv](https://virtualenv.pypa.io/) (recommended)
- [PostgreSQL](https://www.postgresql.org/) or your preferred database

### Installation

```bash
git clone https://github.com/Rajchal/sxc-network-community-backend.git
cd sxc-network-community-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configuration

Copy `.env.example` to `.env` and update the environment variables as needed.

### Running the Server

```bash
python manage.py migrate
python manage.py runserver
```

The server will start on `http://localhost:8000` by default.

## API Documentation

See [API_DOCS.md](API_DOCS.md) for detailed API endpoints and usage.

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.