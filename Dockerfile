FROM python:3.11.0

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY api.py /code/api.py
COPY production_guard.py /code/production_guard.py
COPY ./src /code/src
COPY .env /code/.env

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]












