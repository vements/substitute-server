FROM python:alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./subserver /app/subserver
ENV PYTHONPATH "${PYTHONPATH}:/app"

ENTRYPOINT ["python", "-m", "subserver"]
