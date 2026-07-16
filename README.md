# student-management-api



A REST API built using **FastAPI** and **SQLAlchemy** for managing student records. This project demonstrates backend development concepts including API creation, database integration, CRUD operations, and request validation.

## 🚀 Features

* Create student records
* Retrieve all students
* Retrieve student by ID
* Update student details
* Delete student records
* Interactive API documentation using Swagger UI
* SQLite database integration
* Data validation using Pydantic

## 🛠️ Tech Stack

* **Python**
* **FastAPI** - Web framework for building REST APIs
* **SQLAlchemy** - ORM for database operations
* **Pydantic** - Data validation
* **SQLite** - Database
* **Uvicorn** - ASGI server

## 📂 Project Structure

```
student-management-api/
│
├── main.py          # FastAPI application and API routes
├── database.py      # Database connection configuration
├── models.py        # SQLAlchemy database models
├── schemas.py       # Pydantic request/response schemas
├── crud.py          # Database CRUD operations
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student-management-api.git
```

### 2. Navigate into the project folder

```bash
cd student-management-api
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

## 📖 API Documentation

FastAPI automatically provides interactive documentation:

Swagger UI:

```
http://127.0.0.1:8000/docs
```

## 🔗 API Endpoints

| Method | Endpoint                 | Description          |
| ------ | ------------------------ | -------------------- |
| POST   | `/students`              | Create a new student |
| GET    | `/students`              | Get all students     |
| GET    | `/students/{student_id}` | Get student by ID    |
| PUT    | `/students/{student_id}` | Update student       |
| DELETE | `/students/{student_id}` | Delete student       |

## 📌 Example Request

### Create Student

```json
{
  "name": "Satish",
  "age": 22,
  "course": "FastAPI"
}
```

### Response

```json
{
  "id": 1,
  "name": "Satish",
  "age": 22,
  "course": "FastAPI"
}
```

## 🎯 Learning Outcomes

Through this project, I learned:

* Building REST APIs with FastAPI
* Working with databases using SQLAlchemy
* Designing CRUD operations
* API testing using Swagger UI
* Structuring a Python backend application

## 👨‍💻 Author

Ayyaluri Satish Kumar Reddy

GitHub: https://github.com/satish-ayyaluri
