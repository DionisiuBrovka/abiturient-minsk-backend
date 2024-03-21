FROM python:3.11.4-slim-buster


# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt

# copy project
COPY ./ .

# make migrations
#docker-compose exec api python manage.py migrate --noinput
ENTRYPOINT [ "sh", "-c", "/start.sh" ]