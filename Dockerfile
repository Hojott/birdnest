FROM python:3.10-alpine3.16
LABEL maintainer="Sakari Marttinen <sakkenino@gmail.com>"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ src

EXPOSE 5000
CMD python src/wsgi.py