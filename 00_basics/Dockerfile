FROM python:3.13-slim

WORKDIR /app

COPY game_search/web/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY game_search ./game_search

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "game_search.web.app:app"]
