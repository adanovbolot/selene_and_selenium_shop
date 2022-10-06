FROM python:3.8-alpine

LABEL "channel"="solveme"
LABEL "creator"="solme community"


WORKDIR ./usr/lessons

COPY . .

RUN pip install -U pip && pip install -r requirements.txt


CMD pytest -s -v tests/test_homepage.py

