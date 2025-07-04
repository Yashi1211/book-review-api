# Book Review API

A simple, AI-powered RESTful API for managing book reviews. Built with FastAPI, SQLAlchemy, and SQLite. Now deployed live on Render!

---

## 📚 Project Overview
This project is a backend API that allows users to add, view, update, and delete reviews for books. It also uses AI to analyze the sentiment of each review (positive, negative, or neutral). The API is cloud-deployed and publicly accessible.

---

## 🚀 Features
- Add new book reviews
- View all reviews or reviews for a specific book
- Update existing reviews
- Delete reviews
- **AI-powered sentiment analysis** for every review
- Data validation for all requests
- Interactive API documentation (Swagger UI)
- **Cloud deployment** (Render)

---

## 🛠️ Tech Stack
- **Python 3**
- **FastAPI** (for building APIs)
- **SQLAlchemy** (for ORM/database)
- **SQLite** (as the database)
- **Pydantic** (for data validation)
- **TextBlob & NLTK** (for sentiment analysis)
- **Docker** (for deployment)

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
│   ├── schemas.py     # Data schemas
│   └── ai_service.py  # AI sentiment analysis logic
│
├── main.py            # FastAPI app entry point
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker setup for deployment
├── reviews.db         # SQLite database file (local only)
├── README.md          # Project documentation
└── Book Review api.postman_collection.json # Postman collection
```

---

## ⚙️ Setup Instructions (Local)

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd book-review-api
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On Mac/Linux
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

## ☁️ Cloud Deployment (Render)

This project is deployed live on Render cloud platform.

- **Live Demo:** [Book Review API on Render](https://revuebot.onrender.com/docs)

**How to deploy on Render:**
1. Push your project to GitHub.
2. Create a free account on [Render.com](https://render.com/).
3. Create a new Web Service, connect your GitHub repo, and let Render auto-detect your Dockerfile.
4. Make sure your Dockerfile has this line:
   ```Dockerfile
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```
5. Deploy and get your public URL!

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

Each review response includes:
- `sentiment_score` (float)
- `sentiment_label` (Positive/Negative/Neutral)
- `sentiment_insight` (short AI-generated summary)

---

## 🧪 Postman Collection

You can use this Postman collection to easily test all the API endpoints of this project.

- [Download Postman Collection](Book%20Review%20api.postman_collection.json)

---

## 🙋‍♀️ Author
- **Yashi**
- B.Tech CSE Student

---

## 📢 Notes
- This project is for learning and demonstration purposes.
- You can extend it by adding authentication, user management, or more features as needed.
- SQLite is used for demo; for production, use a cloud database.
- AI sentiment analysis uses TextBlob (basic, but easy to use for learning).

---

**Deployed on Render 🚀**
