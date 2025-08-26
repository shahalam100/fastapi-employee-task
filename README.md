# FastAPI Employee Task Management API

A **FastAPI-based backend project** for managing employees and their tasks.  
The project includes **authentication, user management, and task CRUD operations** with proper database integration.

---

## 🚀 Features
- User **Registration & Login** with JWT authentication
- Secure password hashing
- Role-based user management (basic)
- CRUD for **Tasks** (Create, Read, Update, Delete)
- Custom error handling for database integrity issues
- Middleware for:
  - **CORS** (cross-origin requests from frontend apps)
  - **Request timing** (monitor request performance)
- Modular project structure with routers
- Database integration with **SQLAlchemy**
- Auto-table creation (later upgradable to **Alembic migrations**)

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **FastAPI** – web framework
- **SQLAlchemy** – ORM for database models
- **SQLite** (default DB, can switch to PostgreSQL/MySQL)
- **JWT (OAuth2PasswordBearer)** – Authentication
- **Uvicorn** – ASGI server
- **Alembic** (planned) – Database migrations

---

## 📂 Project Structure
fastapi-employee-task/
│
├── app/
│   ├── __init__.py
│   ├── main.py  
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── deps.py
│   ├── middleware.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── users.py
│   │   └── tasks.py
│── .gitignore
│── README.md




---

## ⚡ Quick Start

### 1️⃣ Clone the repository
```bash
git clone https://github.com/shahalam100/fastapi-employee-task.git
cd fastapi-employee-task

2️⃣ Create virtual environment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

---

3️⃣ Install dependencies

pip install -r requirements.txt

---

4️⃣ Run the project

uvicorn app.main:app --reload

---

5️⃣ Open API docs

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

---

🔑 Authentication

Register a new user → /auth/register

Login with credentials → /auth/login

Use the returned access_token (JWT) to call protected APIs like /users/me and /tasks.

---

📌 Example APIs
Register User

POST /auth/register
{
  "email": "user@example.com",
  "full_name": "User",
  "password": "password123"
}


---

Login User

POST /auth/login
form-data:
  username: user@example.com
  password: password123


Response:

{
  "access_token": "jwt_token_here",
  "token_type": "bearer"
}


---

Create Task

POST /tasks
Authorization: Bearer <access_token>
{
  "title": "Complete Assignment",
  "description": "Finish the FastAPI project",
  "done": false
}

---

👨‍💻 Author

Shah Alam
📧 Email: shahalam834054@gmail.com

💻 GitHub: https://github.com/shahalam100

---

⭐ Future Enhancements

Role-based access control (Admin, User)

Database migrations using Alembic

Docker support

Full UI integration with React/Next.js

Unit & integration tests (Pytest)

---


---

👉 Steps for you:  
1. Create a file named `README.md` in your project root.  
2. Paste the above content.  
3. Commit & push:  
   ```bash
   git add README.md
   git commit -m "Add README file with project details"
   git push origin main

Thanks!

