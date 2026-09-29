# FastAPI PostgreSQL Quiz Application

A robust backend REST API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL** for managing a quiz application featuring questions and multiple-choice answers.

## 🚀 Tech Stack
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Database:** [PostgreSQL](https://www.postgresql.org/)
* **Data Validation:** [Pydantic](https://docs.pydantic.dev/)
* **Server:** [Uvicorn](https://www.uvicorn.org/)

---

## 📁 Project Structure

fastapi-postgresql/

├── .env                  # Environment variables 
(Database URL)

├── .gitignore            # Ignored files (venv, 
pycache, .env)

├── database.py           # Database connection & session setup

├── main.py               # FastAPI app initialization & route handlers

├── models.py             # SQLAlchemy database models (Tables)

├── schemas.py            # Pydantic models (Data validation & serialization)

├── crud.py               # Database queries (Create, Read operations)

└── README.md             # Project documentation

## ⚙️ Getting Started & Installation
To run this project locally, follow these steps:

   ### 1. Clone the Repository
    git clone <your-repository-url>
    cd fastapi-postgresql

   ### 2. Create and Activate a Virtual Environment
##### Create virtual environment:
    python -m venv .venv

##### Activate it (Windows PowerShell):
    .venv\Scripts\Activate.ps1

##### Activate it (Mac / Linux / Git Bash):
    source .venv/bin/activate

   ### 3. Install Dependencies
    pip install fastapi uvicorn sqlalchemy psycopg python-dotenv

   ### 4. Configure Environment Variables
   ##### Create a .env file in the root directory and add your PostgreSQL connection string:

    DATABASE_URL=postgresql://postgres:your_password@localhost:5432/QuizApplication

   ### 5. Run the Application
    Start the development server using Uvicorn:

    uvicorn main:app --reload

📖 API Documentation
Once the server is running, you can explore and test the endpoints directly through your browser using FastAPI's built-in interactive documentation:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc UI: http://127.0.0.1:8000/redoc