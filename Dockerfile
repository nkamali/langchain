FROM python:3.8

# Install dependencies
RUN pip install openai langchain

# Copy all scripts to the container
COPY ./scripts /scripts

# Set work directory
WORKDIR /scripts

# By default, list available scripts (you can change this)
CMD ["ls"]
