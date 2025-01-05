echo "BUILD START"

# create a virtual environment named 'venv' if it doesn't already exist
python3.12 -m venv venv

# activate the virtual environment
source venv/bin/activate
pip install --upgrade setuptools
# install all deps in the venv
pip install -r requirements.txt
pip install django-cors-headers
npm install
# collect static files using the Python interpreter from venv
# Supprimez les anciens fichiers collectés
rm -rf staticfiles_build/static/
python manage.py collectstatic --noinput 

echo "BUILD END"

# [optional] Start the application here 
# python manage.py runserver
