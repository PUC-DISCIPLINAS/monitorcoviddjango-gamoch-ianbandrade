#!/bin/sh
set -e

export APP_HOST=${APP_HOST:-app}
export APP_PORT=${APP_PORT:-8000}
export WEB_PORT=${WEB_PORT:-80}

exec /docker-entrypoint.sh "$@"
