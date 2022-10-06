FROM python:3.8-alpine
WORKDIR /app
COPY requirements.txt .

RUN pip install -U pip

RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "tests/test_homepage.py", "-n 3"]
CMD ['cp environment.properties ./allure/environment.properties']
CMD ['cp category.json ./allure/category.json']
CMD ['allure serve allure']