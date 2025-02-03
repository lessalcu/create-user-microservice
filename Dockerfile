# Use a Python base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which Flask will run
EXPOSE 5000

# Command to start the application
CMD ["python", "app.py"]