# Start from a small Linux image that already has Python 3.12
FROM python:3.12-slim

# Everything below runs inside /app in the container
WORKDIR /app

# Copy only the library list first, so Docker can cache the install step
COPY requirements.txt .

# Install the libraries
RUN pip install --no-cache-dir -r requirements.txt

# Now copy your code
COPY . .

# Start the API server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]