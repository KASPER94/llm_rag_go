FROM golang:1.21 AS builder

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY srcs/. .

RUN go build -o server main.go

FROM debian:bookworm-slim

WORKDIR /root/
COPY --from=builder /app/server .

EXPOSE 8080

CMD ["./server"]
