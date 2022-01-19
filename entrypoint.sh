#!/bin/bash

python3 settings/manage.py collectstatic --no-input
python3 settings/manage.py runserver