FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

RUN cd shop

CMD ["python","manage.py","runserver", "0.0.0.0:8000"]