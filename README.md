# Book Review API

A simple RESTful API for managing book reviews. Built with FastAPI, SQLAlchemy, and SQLite.

---

## 📚 Project Overview
This project is a backend API that allows users to add, view, update, and delete reviews for books. It is useful for any book review website or app that needs a backend to manage reviews.

---

## 🚀 Features
- Add new book reviews
- View all reviews or reviews for a specific book
- Update existing reviews
- Delete reviews
- Data validation for all requests
- Interactive API documentation (Swagger UI)

---

## 🛠️ Tech Stack
- **Python 3**
- **FastAPI** (for building APIs)
- **SQLAlchemy** (for ORM/database)
- **SQLite** (as the database)
- **Pydantic** (for data validation)

---

## 📁 Project Structure
```
book-review-api/
│
├── app/
│   ├── crud.py        # CRUD operations
│   ├── database.py    # Database connection
│   ├── models.py      # Database models
│   ├── routes.py      # API endpoints
│   └── schemas.py     # Data schemas
│
├── main.py            # FastAPI app entry point
├── requirements.txt   # Python dependencies
├── Dockerfile         # (Optional) Docker setup
├── reviews.db         # SQLite database file
└── README.md          # Project documentation
```

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd book-review-api
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API server:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API docs:**
   Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📝 Example API Endpoints

- **Get all reviews:**
  - `GET /reviews`
- **Add a new review:**
  - `POST /reviews`
- **Get a review by ID:**
  - `GET /reviews/{review_id}`
- **Update a review:**
  - `PUT /reviews/{review_id}`
- **Delete a review:**
  - `DELETE /reviews/{review_id}`

---

## 🙋‍♀️ Author
- **Yashi**
- B.Tech CSE Student

---

## 📢 Notes
- This project is for learning and demonstration purposes.
- You can extend it by adding authentication, user management, or more features as needed.## 🧪 Postman Collection
## Postman Collection
-This Postman collection allows you to quickly test and explore all the API endpoints provided by the Book Review API.
 [Download Postman Collection](Book Review api.postman_collection.json)
