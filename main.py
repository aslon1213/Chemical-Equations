import os
import platform

os.system("git clone https://github.com/aslon1213/Chemical-Equations")
os.system("cd Chemical-Equations")
# get system os type
if platform.system() == "Windows":
    os.system("python -m pip install pipenv")
    os.system("python -m pipenv shell")
    os.system("python -m pip install -r requirements.txt")
    os.system("python manage.py runserver")
elif platform.system() == "Linux":
    os.system("python3 -m pip install pipenv")
    os.system("python3 -m pipenv shell")
    os.system("python3 -m pip install -r requirements.txt")
    os.system("python3 manage.py runserver")
elif platform.system() == "Darwin":
    os.system("python3 -m pip install pipenv")
    os.system("python3 -m pipenv shell")
    os.system("python3 -m pip install -r requirements.txt")
else:
    print("Your system is not supported")
    exit(0)
