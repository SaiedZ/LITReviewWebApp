# <div align="center">LITReviewWebApp</div>

<br>
<br>
<span><img src="https://img.shields.io/badge/DJANGO-4.0.1-brightgreen?style=for-the-badge&logo=django&logoColor=white">   <img src="https://img.shields.io/badge/Python-3.10.0-brightgreen?style=for-the-badge&logo=python&logoColor=white">   <img src="https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white">   <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"></span>
<br>
<br>


## 📖 What's it ?

This repository hosts a project to achieve during my training OpenClassRooms.com
This project was created on Django 4.0.1 using Python 3.10.0
The purpose of this progam is to manage an offline chess tournament.



## 💿 How to setup the application ?

1. First, you will need to download [the source code](https://github.com/SaiedZ/LITReviewWebApp.git) from GitHub.
2. Unzip the folder
3. Go to the unzipped folder using your terminal
4. Create your virtual environment with the following command (here I call it .env, but you can call it another way)
```bash
python -m venv .env
```
6. Activate the virtual environment with the following command
 
  * on Unix or Mac :
```shell
 source .env/bin/Activate
```
   * on Windows :
```bash
env\Scripts\activate.bat
```

7. Install the packages required to run the tool from the `requirements.txt` file
```bash
pip install -r requirements.txt
```
8. Now y can start the development server


For more information, refer to the python.org documentation :

[Virtual envirement tutorial](https://docs.python.org/3/tutorial/venv.html)


## ⚙️ Launch the development server

First of all, you need to be located in the **src forlder**
```bash
.
├── ./src
│   ├── ./src/LITReviewWebApp
│   ├── ./src/accounts
│   ├── ./src/db.sqlite3
│   ├── ./src/manage.py
│   ├── ./src/media
│   ├── ./src/requirements.txt
│   ├── ./src/templates
│   └── ./src/tickets
└── ./users.xlsx
```

To launch the development server locally, just use the `runserver` command from the `manage.py` file:

```
python manage.py runserver
``` 

Of course, you must first ensure that you have activated your virtual environment and that you are in the folder that contains the `manage.py` file.

Once the development server is launched, you can see your Django project's default home page at `127.0.0.1:8000` in a web browser.


## What is its use?




## Use flake8 html

In order to generate a flake8 report, run the following command :
```
flake8 --format=html --htmldir=flake-report --exclude=.env
```
Open the html file into the flake-report repertory to show the report.
