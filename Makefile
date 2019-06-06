run:
	py manage.py runserver 0.0.0.0:8888

mig:
	py manage.py migrate

mk-mig:
	py manage.py makemigrations

sh-mig:
	py manage.py showmigrations

create-su:
	py manage.py createsuperuser

get-req:
	pip freeze > requirements.txt