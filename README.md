# Contact Form API

This project implements a FastAPI-based API for handling contact form submissions. It receives form data, sends a notification email to the administrator, and optionally sends an auto-reply to the submitter.

## Features

- FastAPI-based RESTful API
- Form data validation using Pydantic
- Email notification for new form submissions
- CORS middleware for cross-origin requests
- Environment variable configuration using python-dotenv

## Prerequisites

- Python 3.7+
- pip

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MoAlkhateeb/contact-form-api.git
cd contact-form-api
```

1. Install the dependencies with pipenv:

```bash
pipenv install
```

1. Create a `.env` file in the project root and set the following environment variables:
```bash
GMAIL_ADDRESS=example@example.com
GMAIL_PASSWORD=yourpassword
```

Note: For security reasons, it's recommended to use an app password instead of your actual Gmail password.

## Usage

1. Start the server:

```bash
python main.py
```

2. The API will be available at `http://localhost:8000`.

3. To submit a form, send a POST request to the root endpoint (`/`) with the following form data:
- `name`: Name of the sender
- `email`: Email address of the sender
- `message`: Message content

## API Endpoints

- `POST /`: Submit a contact form

## Development

To run the server in development mode with auto-reloading:

```
uvicorn main:app --reload
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.