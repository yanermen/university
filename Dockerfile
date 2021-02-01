FROM ubuntu
MAINTAINER Erik Abrahamyan <yanermen@gmail.com>
RUN apt-get update && apt-get install -y
RUN mkdir university
WORKDIR /university
COPY ./ ./
RUN apt-get install -y python3-pip
RUN apt-get install -y python3
RUN python3 -m pip install pipenv
RUN pipenv install --system --deploy
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
