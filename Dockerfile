
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV PYTHONPATH=/code
EXPOSE 5000
CMD ["uvicorn", "app.main:app", "--no-server-header", "--host", "0.0.0.0", "--port", "5001"]
