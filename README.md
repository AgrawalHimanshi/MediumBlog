# Medium Blog
MediumBlog

to activate virtual environment

activate env_name

django-admin startproject projectname
cd projectname
django-admin startapp appname

python manage.py runserver

## for database
python manage.py makemigrations --- output->blog/migrations/0001_initial.py
// to see actual sql code before creating table in database using migrate
python manage.py sqlmigrate blog 0001

python manage.py migrate
