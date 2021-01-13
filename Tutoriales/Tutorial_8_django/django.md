<p align="center">
<img src = "img/django.png" width="400">
</p>


# Tutorial 8: Django


### Contenido:

1. ¿Qué es Django?
2. ¿Por qué usar Django?
3. Instalación 
4. Creación de proyectos

4. Referencias



### 1. ¿Qué es Django?


***Django*** es un framework web de código abierto escrito en *Python*. El objetivo de *Django* es facilitar la creación de sitios web complejos, poniéndole énfasis en el re-uso, la conectividad y expansibilidad de componentes.
******
### 2. ¿Por qué usar django?

* **Rapidez:**
Con *django* podemos construir buenas aplicaciones en poco tiempo, especialmente si se tenemos una *startup* y tenemos prisa por terminar nuestro proyecto, además de reducir costes.

* **Seguridad:** 
Django implementa de por si algunas medidas de seguridad, como por ejemplo, para que no haya SQL Injectionm, Cross site request forgery(CSRF) o no Clickjacking por JavaScript.

* **Escalabilidad:**

Este framework nos permite pasar desde un aplicación pequeña a aplicación enorme que sea modular y que funcione rápido y que además sea estable.

* **Versatilidad** 
Django comenzó siendo un Framework para almacenar noticias de sitios de prensa, blogs, pero hoy en día ha ganado mucha popularidad y puede usarse en webs de cualquier propósito. Entre las webs destacadas que usan *django* encontramos National Geografic, Instagram, Pinterest, Mozila Foundation, entre otras.


****

 ### 3. Instalación

Descarga en la página oficial de [django](https://www.djangoproject.com/download/) .

**Opción 1:** 

Instalamos la versión oficial, usando pip:

`pip install Django==3.1.5`

**Opción 2:**

Desde el repositorio git podemos descargar la versión de desarrollo:

`git clone https://github.com/django/django.git`


****

### Creación de proyectos

Creamos un directorio local donde se encontrará nuestro proyecto:

`$ mkdir djangoproyect`

`$ cd djangoproyect`

Luego ejecutamos el siguiente comando que creará un directorio llamado proyecto1 en el directorio actual:

`$ django-admin startproject proyecto1`

El comando `startproeyct` crea los siguientes archivos:

````````
proyecto1/
    manage.py
    proyecto1/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py

````````

***
### Referencias: 

* django project [[1](https://www.djangoproject.com/)].












