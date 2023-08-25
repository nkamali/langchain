# LangChain (LLMs and Generative AI)

I've created multiple scripts using LangChain that you can run within the docker container.

## Prerequisites

Docker

## Get Started

Clone the repository:

```
git clone git@github.com:nkamali/langchain.git
cd langchain
```

## To install and run the service with Docker:

I assume you already have Docker Desktop running on your machine. If not, install that first.

This will download the docker image and install everything within a docker container.

`docker-compose up --build`

`docker-compose run gen_ai python /scripts/predict_message.py --text "What would be a good company name for a company that makes colorful socks?"`

## Project Structure

The project's structure is as follows:

```
├── README.md
├── scripts
|   └──predict_message.py
├── docker-compose.yml
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Built With

FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Contact

Navid Kamali - navidkamali@gmail.com

Project Link: https://github.com/nkamali/langchain
