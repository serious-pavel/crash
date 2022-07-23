# crash
Otus final app project

### Install requirements
```
cd path/to/project
pip install -r requirements.txt
mkdir -p test/CrashBest01
mkdir -p test/CrashBest10
mkdir -p test/CrashBest50
# fill folders with any images
mv crash/.env.example crash/.env
# edit crash/.env with your settings
python manage.py migrate
```
### Upload photos
```
# Necessary step for site work. It must be one or more photos for main page correct work
python manage.py upload_file <count of files you want to upload>
```
### Start app
```
python manage.py runserver
```
By deafault it starts on http://127.0.0.1:8000/