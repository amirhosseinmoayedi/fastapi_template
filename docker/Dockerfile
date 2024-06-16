# Stage 1: Build
FROM python:3.12.3-slim-bullseye AS build

# Set environment variables to ensure poetry installs to the right location
ENV PIP_DEFAULT_TIMEOUT=1000
# Allow statements and log messages to immediately appear
ENV PYTHONUNBUFFERED=1
# prevents python creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

ENV POETRY_VERSION=1.7.1
# make poetry install to this location
ENV POETRY_HOME="/opt/poetry"
# make poetry create the virtual environment in the project's root it gets named `.venv`
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# Add Poetry to PATH
ENV PATH="$POETRY_HOME/bin:$PATH"


# Set the working directory in the container
WORKDIR /usr/src/app

# Copy dependencies
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION" \
    && poetry install --only main --without dev --no-root --no-ansi --no-interaction

# Stage 2: Runtime
FROM python:3.12.3-slim-bullseye AS runtime

RUN apt-get update

# Set environment variables
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# Add Poetry to PATH
ENV PATH="$POETRY_HOME/bin:$PATH"


# Set the working directory
WORKDIR /usr/src/app

# Copy the virtual environment from the build stage
COPY --from=build /usr/src/app/.venv /usr/src/app/.venv

# Copy the application code from the build stage
COPY . /usr/src/app

# Run the application
CMD ["poetry", "run", "python", "main.py"]
