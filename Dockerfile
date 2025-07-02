# ✅ 1. Base image
FROM python:3.11

# ✅ 2. Working directory inside container
WORKDIR /app

# ✅ 3. Copy files from host to container
COPY . .

# ✅ 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ 5. Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
