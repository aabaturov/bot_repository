FROM python
COPY bot.py /app/
COPY config.py /app/
COPY sendings.py /app/
COPY menu.py /app/
COPY api.py /app/
COPY audio /app/audio
COPY data /app/data
#COPY high_school.jpg /app/data
#COPY hobby.jpg /app/data
#COPY greetings.jpg /app/data
#COPY stickers /app/stickers
RUN pip install pyTelegramBotAPI
WORKDIR /app/
CMD ["python3","bot.py"]
