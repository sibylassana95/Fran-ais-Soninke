echo "BUILD START"
# Clear pip cache
pip cache purge

pip install --upgrade setuptools

# install all deps in the venv
pip install -r requirements.txt
python3.9 manage.py makemigrations
python3.9 manage.py migrate
python3.9 manage.py collectstatic --noinput

echo "BUILD END"

# [optional] Start the application here 
# python manage.py runserver