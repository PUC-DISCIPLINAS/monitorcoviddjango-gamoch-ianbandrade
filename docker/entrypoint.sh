#!/bin/bash
set -e

HOST=${DATABASE_HOST}
PORT=${DATABASE_PORT:-5432}

if [[ -z "${HOST}" ]]; then
  echo -e "\nDATABASE_HOST is required\n"
  exec bash
else
  echo "Waiting for PostgreSQL"

  until &>/dev/null </dev/tcp/${HOST}/${PORT}; do
    sleep .1
  done

  python manage.py migrate &>/dev/null
  python manage.py collectstatic --noinput &>/dev/null

  exec "$@"
fi
