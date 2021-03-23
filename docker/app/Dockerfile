FROM python:3.7.7

COPY Pipfile /Pipfile
COPY Pipfile.lock /Pipfile.lock

COPY app /app

RUN pip install pipenv && pipenv sync --system

EXPOSE 80

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]
