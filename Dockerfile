# Start from the official Python base image
FROM python:3.9

# Set the current working directory to /code
WORKDIR /code

# Move requirements file to the code directory
COPY ./requirements.txt /code/requirements.txt

# Install requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Move app file to the code directory
COPY ./app /code/app

# Set the command to run the uvicorn server
# Google Cloud listens on port 8080 by default
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

