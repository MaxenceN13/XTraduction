FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get -y upgrade

RUN useradd --create-home appuser

USER appuser

RUN pip install -U pip

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY config.py .
COPY translateDeeplAPI.py .
COPY twitterengine.py .

CMD [ "python", "./main.py" ]