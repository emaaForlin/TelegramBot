FROM python:3.8-alpine

RUN mkdir /app && pip install requests TelegramBotInterface

COPY bot.py /app

WORKDIR /app

ENV TOKEN ''
ENV CHAT_ID ''

ENTRYPOINT python3 bot.py $TOKEN $CHAT_ID
