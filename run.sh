#!/bin/bash

# Where you want the log to be, "-" is stdout.
access_log="-"

# What you want gunicorn to bind to.
bind_host="127.0.0.1"
bind_port="8080"

# How many threads you want gunicorn to spawn.
workers="10"

# Daemonize gunicorn?
daemon="False"


/usr/local/bin/gunicorn --access-logfile "${access_log}" --bind "${bind_host}:${bind_port}"\
                        --workers "${workers}" main:app