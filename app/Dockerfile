FROM python:3.9.1

WORKDIR /app

EXPOSE 8000

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        supervisor \
    && apt-get clean \
    && rm -Rf /var/lib/apt/lists/*

COPY ./requirements.txt /tmp/
RUN pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt

COPY . /app

RUN ln -s /app/entrypoint.sh / \
    && ln -s /app/supervisor.conf /etc/supervisor/conf.d/ \
    && ln -s /app/gunicorn.py /etc/

ENTRYPOINT [ "/entrypoint.sh" ]
