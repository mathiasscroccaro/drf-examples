FROM python:3.10-slim

RUN mkdir /project

COPY . /project/

WORKDIR /project

RUN pip install -r requirements.txt

CMD ["gunicorn", "app.wsgi", "--bind", "0.0.0.0:8000"]