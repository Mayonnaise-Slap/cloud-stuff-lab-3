FROM python:3.11.3-alpine3.16

WORKDIR /app
COPY src/requirements.txt .
RUN python -m pip install -r requirements.txt

COPY ./src .
EXPOSE 3000

ENTRYPOINT [ "python", "app.py" ]