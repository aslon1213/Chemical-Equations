import os
import urllib.request

os.system("git clone https://github.com/aslon1213/Chemical-Equations")
os.system("cd Chemical-Equations")
os.system("python3 -m pip install -r Chemical-Equations/requirements.txt")
os.system("python3 Chemical-Equations/manage.py runserver")
