FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /donbot_translate_es_en

COPY ./donbot_translate_es_en.py /donbot_translate_es_en.py

CMD [ "python", "/donbot_translate_es_en.py" ]
