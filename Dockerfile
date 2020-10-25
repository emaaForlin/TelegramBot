FROM python:3.8-alpine

RUN mkdir /app && pip install requests

COPY telegramapi.py /app
COPY bot.py /app

ENV TOKEN ''
ENV CHAT_ID ''

WORKDIR /app
ENTRYPOINT python3 bot.py $TOKEN $CHAT_ID
