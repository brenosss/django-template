# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set environment variables for Poetry
ENV POETRY_VERSION=1.7.0 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies for Poetry and Django
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libpq-dev

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy the Poetry files (pyproject.toml and poetry.lock)
COPY pyproject.toml poetry.lock /app/

# Install the dependencies using Poetry
RUN poetry lock && poetry install

# Copy the rest of the project files into the container
COPY . /app/