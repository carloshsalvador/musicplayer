# Use the official Python image from Docker Hub with the specified version
FROM python:3.11.9

# Set environment variable to ensure the Python output is sent straight to the terminal (unbuffered)
ENV PYTHONUNBUFFERED=1

# Install Rust and Cargo for compiling packages like cryptography and psycopg2 that require Rust
RUN apt-get update && apt-get install -y curl \
    && curl https://sh.rustup.rs -sSf | sh -s -- -y \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Ensure Rust and Cargo are available in the PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file into the /app directory
COPY requirements.txt requirements.txt

# Upgrade pip to the latest version and install Python dependencies from requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the rest of the application code into the /app directory
COPY . .

# Expose port 8000 for the application
EXPOSE 8000

# Define the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]