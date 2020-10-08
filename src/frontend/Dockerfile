FROM node:14

RUN apt-get update -qq && apt-get install -y yarn
RUN mkdir /app
WORKDIR /app

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["yarn", "start"]