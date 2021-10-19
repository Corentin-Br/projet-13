FROM python:3.8
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt
COPY . /code/


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]