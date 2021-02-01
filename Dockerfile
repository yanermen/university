FROM python:3.8
MAINTAINER Erik Abrahamyan
ENV PYTHONUNBUFFERED=1
ENV PROJECT_DIR /home/hello/Projects/university/
WORKDIR ${PROJECT_DIR}
COPY Pipfile Pipfile.lock ${PROJECT_DIR}
RUN python3 -m pip install pipenv
RUN pipenv install --system --deploy
COPY . /home/hello/Projects/university/
