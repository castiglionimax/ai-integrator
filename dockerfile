# -------- base --------
    FROM python:3.12-slim AS base
    ENV PYTHONDONTWRITEBYTECODE=1 \
        PYTHONUNBUFFERED=1 \
        PIP_NO_CACHE_DIR=1
    WORKDIR /app
    RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*
    
    # -------- deps layer --------
    FROM base AS deps
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    
    # -------- dev --------
    FROM deps AS dev
    # en dev montamos el código como volumen; solo dejamos deps dentro de la imagen
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
    
    # -------- prod --------
    FROM deps AS prod
    COPY . .
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    