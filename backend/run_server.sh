#!/bin/sh

# This scritp check if mysql server is running.
# If it's not, wait 3 seconds and retry
# If the mysql server is up, then run migrations and run django server 
while ! nc -z mysqldb 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 3
done

python3 manage.py migrate && python manage.py runserver 0.0.0.0:8000