# Use the official lightweight Python image.
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
