venv) mac@MacdeMacBook-Pro chatter % curl -X POST http://127.0.0.1:5000/auth/signup \
-H "Content-Type: application/json" \
-d '{"username": "newuser", "email": "new@example.com", "password": "secret"}'

{
  "email": "new@example.com",
  "id": 6,
  "username": "newuser"
}

(venv) mac@MacdeMacBook-Pro chatter % curl -X POST http://127.0.0.1:5000/auth/login \
-H "Content-Type: application/json" \
-d '{"email":"new@example.com","password":"secret"}'

{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc1ODgyODU2NCwianRpIjoiOTAwYjU1MjUtYTc5Mi00YTg4LWIzMjktMjM4MGQ5MjkzM2EyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6NiwibmJmIjoxNzU4ODI4NTY0LCJjc3JmIjoiZGI0Y2RhMDktNDFhZi00Y2MyLWI0MjgtMDYzZjdjNzllYWFkIiwiZXhwIjoxNzU4ODI5NDY0fQ.ZfIFNRGsuwRfC4eeKYofv-Cho_XHhbjHEIMHxIbyYgI",
  "message": "Login successful",
  "user": {
    "email": "new@example.com",
    "id": 6,
    "username": "newuser"
  }
}