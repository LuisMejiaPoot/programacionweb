"# web" 
"# programacionweb" 
python -m venv nameenv
myenv\Scripts\activate.bat
python -m pip install Django
pip install pymysql
python manage.py makemigrations appname
python manage.py migrate appname

python manage.py startapp appname