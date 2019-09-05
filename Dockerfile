FROM python:3.7.4-alpine3.10

WORKDIR /reddit-bot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "bot.py"]