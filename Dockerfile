FROM python:3.9-alpine
LABEL authors="pratikbhadane"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ=Asia/Kolkata
ENV PATH="/root/.local/bin:$PATH"

RUN apk add --no-cache curl ca-certificates
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /app

COPY requirements.txt .
RUN uv pip install --system -r requirements.txt

COPY . .

EXPOSE 8000
