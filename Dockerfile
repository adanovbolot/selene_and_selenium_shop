FROM python:3.8-alpine

WORKDIR ./usr/lessons

VOLUME /allure

COPY requirements.txt .

RUN pip install -U pip && pip install -r requirements.txt

COPY . .

CMD pytest -s -v tests/test_homepage.py -n 4
