FROM debian:bookworm

RUN apt-get update && \
    apt-get install -y curl git python3 python3-pip && \
    curl -fsSL https://ollama.com/install.sh | sh

ENV PATH="/root/.ollama/bin:${PATH}"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

COPY . .

CMD ["sh", "-c", "OLLAMA_HOST=0.0.0.0 ollama serve & sleep 5 && ollama pull gemma:2b && tail -f /dev/null"]

# RUN ollama pull mistral

# CMD ["sh", "-c", "ollama serve & sleep 3 && tail -f /dev/null"]
