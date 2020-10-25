FROM python:3.8-alpine

RUN mkdir /app

COPY telegramapi.py /app
COPY bot.py /app

RUN pip install requests

ENV TOKEN ''
ENV CHAT_ID ''

WORKDIR /app
ENTRYPOINT python3 bot.py $TOKEN $CHAT_ID
