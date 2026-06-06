FROM node:20-slim

RUN mkdir /app && chown node:node /app
WORKDIR /app

USER node

COPY --chown=node:node package*.json ./
RUN npm install

EXPOSE 5173

COPY --chown=node:node . .

CMD ["npm", "run", "dev"]