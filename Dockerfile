FROM python:3.10-slim

ENV APP_ENV=.venv

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api:user_api", "--host", "0.0.0.0", "--port", "8000"]