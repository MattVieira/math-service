# Math Service
This service is responsible for Math complex calcs

## Prerequisites
* [Docker](https://docs.docker.com/install/)

## Build the project
To build the project, you will need to do `make build`, after this you can run anothers commands on the project.

## Run the project
To run the project, you will need to do `make up`, after this the project will run in a container with the port exposed.
### Lint
To check the project lint messagens, you wil execute `make lint`, this command will show in the terminal all logs from pylint

### Tests
You have three options to run the tests
`make test`: In this option you will run all tests

## Postman Collections
There is a collection of postman with the requirements to be used with the application running.

## Next steps for Deploy
As the application generates a Docker image, it would create a pipeline in some CI service to:
* Perform all unit tests, styles and code coverage.
* Build the image and upload it to the ECR or DockerHub
* After that, do the Deploy on Amazon ECS.

## Matematical Solutions
The logic of the mathematical services was consulted on the internet, but the entire architecture and management of these services was entirely developed by me.

Prioritizing scalability, easy code maintenance and high-demand development styles.

## Built With
* [Python](www.python.org) - Program Language
* [Starlette](https://www.starlette.io) - Framework/Toolkit
* [Pytest](https://docs.pytest.org/en/latest) - Test Framework
* [Pylint](https://www.pylint.org/) - Lint Framework
* [Requests](https://requests.kennethreitz.org/en/master) - HTTP library
* [Uvicorn](https://www.uvicorn.org) - ASGI server
* [ScoutAPM](https://scoutapm.com/) - APM Agent
* [PipEnv](https://pypi.org/project/pipenv/) - Environment Manger
* [PyEnv](https://github.com/pyenv/pyenv) - Python Version Management
