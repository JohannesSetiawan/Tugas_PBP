release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json'
release: sh -c 'python manage.py migrate && python manage.py loaddata data_watchlist.json'
web: gunicorn project_django.wsgi --log-file -
