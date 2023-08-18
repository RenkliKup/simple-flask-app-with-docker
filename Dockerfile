# Use an official Python runtime as the base image
FROM python:slim
# Set the working directory in the container
EXPOSE 5000/tcp
WORKDIR /app
ADD ./model ./model
ADD main.py main.py
# Copy the requirements file into the container
COPY requirements.txt .
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Define the command to run your Flask app
CMD ["python", "main.py"]