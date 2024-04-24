FROM python:3.11-slim

RUN pip install --no-cache-dir fastapi uvicorn requests

WORKDIR /app

COPY . /app

# Expose the port
EXPOSE 8000

# Run the bot
CMD ["python", "bot_api.py"]