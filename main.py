import os
import urllib.request

os.system("python3 -m pip install -r requirements.txt")
os.system("python3 manage.py runserver")
webUrl = urllib.request.urlopen("http://127.0.0.1:8000")
