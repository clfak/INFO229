FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1404448791367-1417413815399-FarzLf2c4TsTyla4t4vtBWcy"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /donbot_slack_writer

COPY ./donbot_slack_writer.py /donbot_slack_writer.py
COPY ./donbot_slack_writer.py /donbot_slack_writer.py

CMD [ "python", "/donbot_slack_writer.py" ]