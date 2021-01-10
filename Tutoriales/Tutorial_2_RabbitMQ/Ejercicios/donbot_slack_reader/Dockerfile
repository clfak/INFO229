FROM python:3.6.3


ENV SLACK_TOKEN="xoxb-1404448791367-1417413815399-FarzLf2c4TsTyla4t4vtBWcy"

ENV SLACK_SIGNING_SECRET="87c7636c515213b1f2ad4271fc971eb7"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /donbot_slack_reader

COPY ./donbot_slack_reader.py /donbot_slack_reader.py

CMD [ "python", "/donbot_slack_reader.py" ]
