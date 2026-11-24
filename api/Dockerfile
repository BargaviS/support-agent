FROM python:3.12-slim                  # start from a small Linux with Python 3.12
WORKDIR /app                           # everything below happens in /app inside the container
COPY requirements.txt .                # copy only the library list first
RUN pip install --no-cache-dir -r requirements.txt   # install the libraries
COPY . .                               # now copy your code
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]