FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /donbot_wikipedia_search

COPY ./donbot_wikipedia_search.py /donbot_wikipedia_search.py

CMD [ "python", "/donbot_wikipedia_search.py" ]
