# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requeriments.txt

# Install playwright and then its dependencies (the browsers)
RUN pip install playwright
RUN playwright install
RUN playwright install-deps

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV STREAMLIT_SERVER_PORT=8501

# Run app.py when the container launches

CMD ["streamlit", "run", "app.py"]