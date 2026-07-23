# --- Stage 1: build das dependências ---
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# --- Stage 2: imagem final, mais leve ---
FROM python:3.12-slim

# Cria um utilizador não-root (boa prática de segurança)
RUN useradd --create-home appuser
WORKDIR /app

# Copia só as dependências já instaladas do stage anterior
COPY --from=builder /root/.local /home/appuser/.local

# Copia o código da app
COPY app/ ./app/

# Garante que os binários instalados em --user são encontrados
ENV PATH=/home/appuser/.local/bin:$PATH

# Muda para o utilizador não-root
USER appuser

EXPOSE 5000

CMD ["python", "app/main.py"]