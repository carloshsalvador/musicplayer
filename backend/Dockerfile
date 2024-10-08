# official Python image from Docker Hub with the specified version
FROM python:3.11.9

# environment variable to ensure the Python output is sent straight to the terminal (unbuffered)
ENV PYTHONUNBUFFERED=1

# installation of tools in the containers usefull for other tools and requirements aferwards, such as
# curl for downloading the packages installer (e.g., Rust),
# Rust and Cargo for compiling packages like cryptography and psycopg2 that require Rust,
# iputils-ping for debugging purposes
# postgresql-client for running database migrations
# obs: such tools are useful also later on containers bash for debugging purposes
RUN apt-get update && apt-get install -y curl \
    && curl https://sh.rustup.rs -sSf | sh -s -- -y \
    && apt-get install -y iputils-ping postgresql-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# to ensure Rust and Cargo are available in the PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# setting the working directory in the container to /app
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