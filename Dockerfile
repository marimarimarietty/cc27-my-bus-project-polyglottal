# download image of python
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src

# install poetry by using pip
RUN pip install poetry

# copy the file of poetry if exists
COPY pyproject.toml* poetry.lock* ./

# install library by poetry if pyproject.toml already exists
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install; fi

# run server uvicorn
ENTRYPOINT ["uvicorn"]
CMD uvicorn api.main:app --host 0.0.0.0 --port $PORT
