FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

# Upgrade pip, setuptools, and wheel first
RUN pip install --upgrade pip setuptools wheel

# Then install your requirements
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "railway_server.py"]
