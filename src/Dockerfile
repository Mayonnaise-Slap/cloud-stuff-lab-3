FROM python:3.11.3-alpine3.16

WORKDIR /app
COPY src/requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .
EXPOSE 3000

CMD [ "python", "src/app.py" ]