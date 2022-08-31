# Travel 2 Ireland 

<img src="media/image.png" widht="100%">

### Install all Libraries neededed 

**Install all libraries and create a virtual environment to proced**
*Install virtualenv to create a virtual environment*
~~~ shell
pip install virtualenv
~~~
*Create a virtual environment*
~~~ shell
python -m venv venv
~~~
*Activate virtual environment*
~~~ shell
venv/scripts/activate
~~~
*Install all libraries nedded*
~~~ shell
pip install -r requirements.txt
~~~

**Migrate the database(Create database)**
~~~ shell
python manage.py migrate
~~~

**Save changes created in models.py**
~~~ shell
python manage.py makemigrations
~~~
- Afterchanges,run the migration" python manage.py migrate "


**Create an admin user in django**
~~~ shell
python manage.py createsuperuser
~~~

**Run django application**
~~~ shell
127.0.0.1:8080
~~~

**Admin Page**
~~~ shell
127.0.0.1:8080/admin
~~~
- then just log into the system with created user