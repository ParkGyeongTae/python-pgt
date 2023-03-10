FROM python:3.11.2

RUN pip install --upgrade pip

COPY ./requirements.txt /opt/requirements.txt

RUN pip install -r /opt/requirements.txt && \
    pip freeze > /opt/requirements-result.txt

COPY ./app /app

WORKDIR /app
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]