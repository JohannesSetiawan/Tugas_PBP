release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json'
web: gunicorn aplikasi_tugas2.wsgi --log-file -
