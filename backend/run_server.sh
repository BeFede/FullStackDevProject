#!/bin/sh


while ! nc -z mysqldb 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 3
done

python3 manage.py migrate && python manage.py runserver 0.0.0.0:8000