echo "BUILD START"
# Clear pip cache
pip cache purge
# create a virtual environment named 'venv' if it doesn't already exist
python3.9 -m venv venv
# activate the virtual environment
source venv/bin/activate
pip install --upgrade setuptools

# install all deps in the venv
pip install psycopg2-binary
pip install -r requirements.txt
python3.9 manage.py makemigrations
python3.9 manage.py migrate
python3.9 manage.py collectstatic --noinput

echo "BUILD END"

# [optional] Start the application here 
# python manage.py runserver