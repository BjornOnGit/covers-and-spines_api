# Covers And Spines API

## Table of Contents

- [Covers And Spines API](#covers-and-spines-api)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Installation](#installation)
  - [Technologies](#technologies)
  - [Usage](#usage)
  - [Integrations](#integrations)
  - [Contributions](#contributions)

## Description

The covers and spines API is an online bookstore API that allows a user to log in and log out, identify themselves as authors, upload books, review books and receive payments.
It was built using Django, Django Rest Framework, Docker, and is hosted on Heroku.

## Installation

To install the API, clone the repository and run the following command:

```bash
git clone https://github.com/BjornOnGit/covers-and-spines_api.git
```

## Technologies

Make sure you have the following installed:

- Python 3.8*
- Docker

Once you have the repository cloned and the required software installed, navigate to the root of the project and run the following command:

```bash
docker-compose -f docker-compose.yml build
docker compose up -d --build
```

These will build the docker image and run the API on your local machine.

To access the API, navigate to `http://localhost:8000/` in your browser.

## Usage

To use the API, all the endpoints are available on the API documentation page. You can access the API documentation by navigating to `https://documenter.getpostman.com/view/27448500/2sA3BgAais` in your browser. The API documentation provides a list of all the endpoints available and the required parameters for each endpoint.

## Integrations

The API is integrated with PayStack for payment processing. To use the payment processing feature, you will need to create a PayStack account and provide the API keys in the `.env` file.

## Contributions

To contribute to the project, fork the repository and create a pull request. Make sure to provide a detailed description of the changes you made and the reason for the changes. All contributions are welcome. I encourage frontend developers who have built online bookstore projects to use the API and provide feedback on how it can be improved.
PLEASE DO NOT PUSH TO THE MAIN BRANCH. Create a new branch and create a new pull request from that branch to the main.
