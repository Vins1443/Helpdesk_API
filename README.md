# 🚀 Helpdesk Ticketing API  

## 📌 Overview  
A simple REST API for managing helpdesk tickets using **FastAPI** and **SQLite**. Supports **CRUD operations** (Create, Read, Update, Delete).  

---
## 🛠 Installation  

1️⃣ **Clone the Repository**  
```cmd
git clone https://github.com/Vins1443/Helpdesk_API.git
cd helpdesk-api
```

2️⃣ **Create & Activate Virtual Environment (Optional but Recommended)**  
```cmd
python -m venv venv
venv\Scripts\activate  (Windows)
```

3️⃣ **Install Dependencies**  
```cmd
pip install -r requirements.txt
```

---

## ▶️ Running the API  

1️⃣ **Start the FastAPI Server**  
```cmd
uvicorn main:app --reload
```
2️⃣ **Open API Docs**  
Visit: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**  

---

## 🧪 Running Tests  

1️⃣ **Run Pytest**  
```cmd
pytest -s -v
```

---

## 📂 Folder Structure  
```
helpdesk-api/
│── app/
│   ├── __init__.py
│   ├── main.py         # API endpoints
│   ├── database.py     # Database connection
│   ├── models.py       # ORM models
│   ├── crud.py         # CRUD operations
│── tests/
│   ├── __init__.py
│   ├── test_main.py    # Unit tests
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
