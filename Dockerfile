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

# run main task
CMD ["gunicorn"  , "backend.wsgi:application", "--bind", "0.0.0.0:8000"]