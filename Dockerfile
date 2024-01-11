FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY . .

RUN python manage.py collectstatic --no-input

EXPOSE 8000
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8000", "decisionassistant.wsgi:application"]