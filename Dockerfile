FROM python:3
ARG django_key
ARG env
ENV PYTHONUNBUFFERED=1
ENV DJANGO_KEY=$django_key
ENV ENV = $env

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN echo DJANGO_KEY
COPY . /code/
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]