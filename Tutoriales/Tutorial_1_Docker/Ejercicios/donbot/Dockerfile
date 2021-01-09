FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV SLACK_TOKEN="xoxb-xxxxxxxxxxxxxx-xxxxxxxxxxxxx-xxxxxxxxXxXxxxxxxxxXXxx"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /donbot

COPY ./donbot.py /donbot.py
COPY ./donbot_app.py /donbot_app.py

CMD [ "python", "/donbot_app.py" ]
