FROM python:3.9

RUN adduser --system --group --no-create-home hjkl

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./app /app/

USER hjkl
#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
