FROM python:3
ENV PYTHONUNBUFFERED=1
ENV django_key=$django_key
ENV debug=$debug
ENV allowed_hosts=$allowed_hosts

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]