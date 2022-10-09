FROM python:3.8-alpine

LABEL "channel"="solveme"
LABEL "creator"="solme community"

WORKDIR ./usr/lessons

VOLUME /allure

COPY requirements.txt .

RUN pip install -U pip && pip install -r requirements.txt

COPY . .

CMD pytest -s -v tests/test_homepage.py --alluredir=allure && allure serve allure -n 4

