FROM node:14.17.5-alpine

WORKDIR /app
COPY . .
RUN npm install

ENTRYPOINT ["node","app.js"]
EXPOSE 3000