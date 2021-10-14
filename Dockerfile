FROM python:3
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY all_requirements.txt /code/
RUN pip install -r all_requirements.txt
COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]