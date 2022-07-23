# crash
otus final app project

### Install and run
```
cd path/to/project
pip install -r requirements.txt
mkdir -p test/CrashBest01
mkdir -p test/CrashBest10
mkdir -p test/CrashBest50
#fill folders with any images
python manage.py runserver
```
By deafault it starts on http://127.0.0.1:8000/

### Upload photos
```
in another session
python manage.py upload_file <count of files you want to upload>
```