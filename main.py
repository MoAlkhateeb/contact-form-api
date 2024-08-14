import os

import smtplib
from pydantic import EmailStr
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Environment variables
GMAIL_ADDRESS: str = os.getenv("GMAIL_ADDRESS", "")
GMAIL_PASSWORD: str = os.getenv("GMAIL_PASSWORD", "")

# CORS configuration
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/")
async def submit_form(
    name: str = Form(...), email: EmailStr = Form(...), message: str = Form(...)
) -> JSONResponse:
    """
    Handle form submission and send notification email.

    Args:
        name (str): Name of the sender.
        email (EmailStr): Email address of the sender.
        message (str): Message content.

    Returns:
        JSONResponse: Response indicating success or failure.
    """
    try:
        # Create the notification email
        msg = MIMEMultipart()
        msg["From"] = GMAIL_ADDRESS
        msg["To"] = GMAIL_ADDRESS
        msg["Subject"] = f"New Contact Form Submission from {name}"
        msg["Reply-To"] = email
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        msg.attach(MIMEText(body, "plain"))

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
            server.send_message(msg)

        return JSONResponse(
            content={"success": True, "message": "Email sent successfully"},
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(
            content={"success": False, "message": str(e)}, status_code=500
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
