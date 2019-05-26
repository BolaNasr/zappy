pip uninstall sqlparse
pip install sqlparse==0.2.4
python /code/zappy_pro/manage.py migrate --fake-initial
python /code/zappy_pro/manage.py runserver 0.0.0.0:8000