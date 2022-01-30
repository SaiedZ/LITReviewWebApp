# <div align="center">LITReviewWebApp</div>

<br>
<br>
<span><img src="https://img.shields.io/badge/DJANGO-4.0.1-brightgreen?style=for-the-badge&logo=django&logoColor=white">   <img src="https://img.shields.io/badge/Python-3.10.0-brightgreen?style=for-the-badge&logo=python&logoColor=white">   <img src="https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white">   <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"></span>
<br>
<br>

## 💿 Installer Django



## 📖 Créer un projet Django


## How to setup the application ?

1. First, you will need to download [the source code](https://github.com/SaiedZ/application_centre_d_echec) from GitHub.
2. Unzip the folder
3. Go to the unzipped folder using your terminal
4. Create your virtual environment with the following command (here I call it .env, but you can call it another way)
```bash
python -m venv .env
```
6. Activate the virtual environment with the following command
    * on Unix or Mac :
```bash
source env / bin / Activate
```
    * On Windows
```bash
env\Scripts\activate.bat
```
7. Install the packages required to run the tool from the `requirements.txt` file
```bash
pip install -r requirements.txt
```
8. Execute the `main.py` file


For more information, refer to the python.org documentation :

[Virtual envirement tutorial](https://docs.python.org/3/tutorial/venv.html)

## ⚙️ Launch the development server

To launch the development server locally, just use the `runserver` command from the `manage.py` file:

```
python manage.py runserver
``` 

Of course, you must first ensure that you have activated your virtual environment and that you are in the folder that contains the `manage.py` file.

Once the development server is launched, you can see your Django project's default home page at `127.0.0.1:8000` in a web browser.


## What's it ?

This repository hosts a project to achieve during my training OpenClassRooms.com
This script was created on Python 3.9.5
The purpose of this progam is to manage an offline chess tournament.

## What is its use?

Create tournaments
Continue ongoing tournaments
Add players
Generate reports

This program use tinyDB and create a db.json file at the root and the Swiss Algorithm to create pairs.

You can't delete players and tournaments,


## Use flake8 html

In order to generate a flake8 report, run the following command :
```
flake8 --format=html --htmldir=flake-report --exclude=.env
```
Open the html file into the flake-report repertory to show the report.
