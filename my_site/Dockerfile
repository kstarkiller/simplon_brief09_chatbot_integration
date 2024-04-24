FROM python:3.11-slim

WORKDIR /app

COPY . /app

# Expose the port
EXPOSE 5000

# Run the bot
CMD ["python", "-m", "http.server", "5000"]