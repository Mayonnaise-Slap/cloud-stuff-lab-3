FROM ubuntu:20.04

RUN apt-get -y update
RUN apt-get -y install nginx

WORKDIR /app
COPY . .
RUN npm install

ENTRYPOINT ["node","app.js"]
EXPOSE 3000
