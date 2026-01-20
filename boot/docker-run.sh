#!/bin/bash
. /opt/myenv/bin/activate
cd /code


RUN_PORT=${PORT:-8000}
RUN_HOST=${HOST:-0.0.0.0}
gunicorn \
    -k uvicorn.workers.UvicornWorker \
    -b $RUN_HOST:$RUN_PORT \
    --workers 4 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    main:app