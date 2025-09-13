#!/bin/bash
echo "BUILD START"
pip install -r requirements.txt

# collect static files into staticfiles_build
python3 manage.py collectstatic --noinput --clear

# list collected files for debugging
echo "STATIC FILES COLLECTED:"
find staticfiles_build -type f

echo "BUILD END"