#!/bin/sh

export FLASK_APP=mlfields
export FLASK_ENV=development
export FLASK_DEBUG=1

flask init-db
flask run --host 0.0.0.0
