#!/bin/sh
gunicorn --bind 0.0.0.0:5000 --workers 2 app:app &
nginx -g 'daemon off;'