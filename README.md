# <div align="center">LITReviewWebApp</div>

<br>
<br>
<span><img src="https://img.shields.io/badge/DJANGO-4.0.1-brightgreen?style=for-the-badge&logo=django&logoColor=white">   <img src="https://img.shields.io/badge/Python-3.10.0-brightgreen?style=for-the-badge&logo=python&logoColor=white">   <img src="https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white">   <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">   <img src="https://img.shields.io/badge/Bootstrap-4.6-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"></span>
<br>
<br>


## 📖 What's it ?

This repository hosts a project to achieve during my training OpenClassRooms.com
This project was created on Django 4.0.1 using Python 3.10.0
**Note that it is an MVP (minimum viable product)**

The application has two main use cases:

* People who ask for reviews of a particular book or article;
* People who are looking for interesting articles and books to read, based on the reviews of others.

The registration and login features have been implemented to use this MVP.

When a user logs into the system, their feed is the first page they see.

He can see the tickets and reviews of all the users he follows.

Users see their own tickets and reviews, as well as reviews in response to their own tickets – even if the user who responded isn't one of the people they follow.

User can also manage his subscriptions to other users and see those who are subscribed to him.



## 💿 How to setup the application ?

1. First, you will need to download [the source code](https://github.com/SaiedZ/LITReviewWebApp.git) from GitHub.
2. Unzip the folder
3. Go to the unzipped folder using your terminal
4. You can also clone the repo without dowloading the folder. In this case, don't follow the steps above and just: use these commands:
```bash
git clone https://github.com/SaiedZ/LITReviewWebApp.git
cd 4425126-testing-python-django
```
5. Create your virtual environment with the following command (here I call it .env, but you can call it another way)
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


## Some screenshots


### login
<hr>

![image](https://user-images.githubusercontent.com/90851774/151717963-f549289a-ffb4-4b12-9044-ebc0c41da925.png)

### Signup
<hr>

![image](https://user-images.githubusercontent.com/90851774/151717987-98f03524-31c5-4db3-a015-fa5258c8005a.png)

### Home page (feed)
<hr>

![image](https://user-images.githubusercontent.com/90851774/151718036-795d1f91-8443-49cd-9209-37a28422ff75.png)

### Subscriptions (relation between users)
<hr>

![image](https://user-images.githubusercontent.com/90851774/151718109-74eac4bf-8e6d-4444-ac2b-7405fb084afc.png)



