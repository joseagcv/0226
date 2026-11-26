FROM python:3.9.6-slim

WORKDIR /my-app

ENV MONGO_URL=mongodb://host.docker.internal:27017

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]



