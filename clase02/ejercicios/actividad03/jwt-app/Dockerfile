FROM python:3.10.17-slim

WORKDIR /app

ENV MONGO_URI=mongodb://host.docker.internal:27017
ENV JWT_ALGORITHM=RS256
ENV PRIVATE_PATH=C:\Users\jose_\master\IA0925\clase03\ejercicios\certificados\private.pem
ENV PUBLIC_PATH=clase03\ejercicios\certificados\public.pem

COPY ./jwt ./

RUN pip install -r requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]