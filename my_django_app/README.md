# Django template
Basic workflows and notes for mostly static django websites.

<details>

## Table of contents

- Folder structure
- Workflow new route
- Workflow new model
- HTML

</details>

---
# Initial
- django_template/django_template contains settings.py
- all other directories are apps
- register app/urls.py in urls.py to access all routes from app
- register app in django_template/settings.py
- add app/urls.py and define routes

---
## Folder Structure  
{ project-name }  
+-- { project-name }  
|   +-- settings.py  
|   +-- urls.py  
+-- { app-name }  
|   +-- templates/{ app-name }  
|   +-- admin.py  
|   +-- models.py  
|   +-- urls.py  
|   +-- views.py  
+-- manage.py  

---
## Basic commands
create django project
```python
django-admin startproject { project-name }
```

create django app
```python
python manage.py startapp { app-name }
```

create admin account
```python
python manage.py createsuperuser
```

create model / database
```python
python manage.py makemigrations
python manage.py migrate
```

run app
```python
python manage.py runserver
```

---
## Routes
Routes control the urls. Routes can be parametrized with a str / int input or read the given url.  
Define index route as "".  
Variables are passed to html template from views.py

### Add routes
{ app-name }/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
```

{ project-name }/urls.py
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing_site/', include("landing_site.urls"))
]
```

---
## Models
Models are databases in django.  
Models must be registered in admin.py

---
## HTML
Create templates/{ app-name }/layout.html .  
Add static css files to app with:  
```html
{% load static %}
```


Create form:
```html
<form>
    <input type="text" name="task">
    <input type="submit">
</form>
```

Find url path:
```html
<a href="{% url 'add' %}">Add a New Task</a>
```


CSRF
```html
{% csrf_token %}
```

---




---
### Notes
routes:
/ -> hello, world!  
/alex -> hello, ALEX!  
