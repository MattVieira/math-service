FROM python:3.9
LABEL maintainer="Mateus Vieira <asakbjj@gmail.com>"
ENV PYTHONPATH /app
ENV SCOUT_MONITOR True
ENV SCOUT_NAME 'Math Service'
ENV SCOUT_KEY '[OBN3A86viRERBM6ptvXx]'
WORKDIR /app
COPY Pipfile ./
RUN pip install pipenv
RUN pipenv install --skip-lock --system
COPY . .
#ENTRYPOINT gunicorn -w 4 --bind 0.0.0.0 -k uvicorn.workers.UvicornWorker --log-level debug server:app
ENTRYPOINT python server.py
