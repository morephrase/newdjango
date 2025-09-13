#!/bin/bash
echo "BUILD START"
pip install -r requirements.txt

# collect static files into staticfiles_build/static
python3 manage.py collectstatic --noinput --clear

echo "BUILD END"
