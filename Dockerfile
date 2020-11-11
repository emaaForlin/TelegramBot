FROM python:3.8-alpine

<<<<<<< HEAD
RUN mkdir /app && pip install requests

WORKDIR /tmp
RUN wget https://github.com/emaaForlin/TelegramBotAPI/archive/main.zip && unzip main.zip && mv ./TelegramBotAPI-main/telegramapi.py /app && rm -rf /tmp/*
=======
RUN mkdir /app && pip install TelegramBotInterface
>>>>>>> test

COPY bot.py /app
WORKDIR /app
ENV TOKEN ''
ENV CHAT_ID ''

ENTRYPOINT python3 bot.py $TOKEN $CHAT_ID
