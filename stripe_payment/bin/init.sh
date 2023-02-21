#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata stripe_payment_fixture.json