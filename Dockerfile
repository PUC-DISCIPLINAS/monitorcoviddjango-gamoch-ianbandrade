FROM python:3.9.0-slim

RUN pip install -qU pip

ENV USER django

ENV HOME /home/${USER}

ENV WORKDIR ${HOME}/workspace

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

ENV PATH ${PATH}:${HOME}/.local/bin

RUN useradd -ms /bin/bash ${USER}

USER ${USER}

RUN mkdir -p ${WORKDIR}/static

WORKDIR ${WORKDIR}

COPY --chown=${USER}:${USER} requirements.txt .

RUN pip install --no-cache-dir -qr requirements.txt

COPY --chown=${USER}:${USER} . .

RUN chmod +x ./docker/entrypoint.sh

ENTRYPOINT ["./docker/entrypoint.sh"]

CMD [ "${ENVIRONMENT:-development}" != "development" ] \
    && gunicorn app.wsgi -w ${APP_WORKERS:-2} -b 0.0.0.0:${APP_PORT:-8000} \
    || python manage.py runserver
