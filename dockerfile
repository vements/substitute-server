FROM python:3.12.0-alpine3.18

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./subserver /app/subserver
ENV PYTHONPATH "${PYTHONPATH}:/app"

ENTRYPOINT ["python", "-m", "subserver"]
