FROM alpine:latest
RUN apk add --no-cache python3
COPY ./helloworld.py /app/helloworld.py
WORKDIR /app
CMD ["python3", "/app/helloworld.py"]