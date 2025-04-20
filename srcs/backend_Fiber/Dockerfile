FROM golang:latest AS builder

WORKDIR /app

# # COPY srcs/go.mod srcs/go.sum ./
COPY srcs/backend_Fiber/* .
# RUN go mod init feedme
# RUN go mod tidy
# RUN go mod download

# RUN go get -u github.com/cosmtrek/air
RUN go install github.com/air-verse/air@latest


# RUN go build -o server .

# FROM debian:bookworm-slim

# WORKDIR /root/
# COPY --from=builder /app/server .

# EXPOSE 8080

# CMD ["./server", "air"]

EXPOSE 8080

CMD [ "air", "-c", ".air.toml" ]
