FROM python:3.8-alpine

RUN mkdir /app && pip install requests TelegramBotInterface

COPY bot.py /app

WORKDIR /app

ENV TOKEN ''
ENV CHAT_ID ''
ENV RUN_TEST 'false'

ENTRYPOINT python3 bot.py $TOKEN $CHAT_ID $RUN_TEST
