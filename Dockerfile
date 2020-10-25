FROM python:3.8-alpine

RUN mkdir /app && pip install requests

WORKDIR /tmp
RUN wget https://github.com/emaaForlin/TelegramBotAPI/archive/main.zip && unzip main.zip && mv ./TelegramBotAPI-main/telegramapi.py /app
RUN rm -rf /tmp/*

COPY bot.py /app
WORKDIR /app
ENV TOKEN ''
ENV CHAT_ID ''


ENTRYPOINT python3 bot.py $TOKEN $CHAT_ID
