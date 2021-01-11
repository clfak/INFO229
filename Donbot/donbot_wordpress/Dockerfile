FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /donbot_wordpress

COPY ./donbot_wordpress.py /donbot_wordpress.py

CMD [ "python", "/donbot_wordpress.py" ]
