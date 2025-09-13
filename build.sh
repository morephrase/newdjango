#!/bin/bash
# Install dependencies
pip install -r requirements.txt

# Run collectstatic so static files are available
python manage.py collectstatic --noinput
