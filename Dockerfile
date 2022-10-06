FROM python:3.8-alpine
WORKDIR /app
COPY requirements.txt .

RUN pip install -U pip

RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "tests/test_homepage.py", "-n 3"]
