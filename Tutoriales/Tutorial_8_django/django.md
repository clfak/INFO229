<p align="center">
<img src = "img/django.png" width="400">
</p>


# Tutorial 8: Django


### Contenido:

1. ¿Qué es Django?
2. ¿Por qué usar Django?
3. Instalación 
4. Creación de proyectos
5. Servidor de desarrollo

6. Referencias



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

* **proyecto1:** El directorio raíz externo **proyecto1/** solo es un contenedor de nuestro proyecto(El nombre no es relevante para Django).

* **manage.py:**  Una utilidad de la línea de comandos que le permite interactuar con este proyecto *Django* de diferentes formas.

* **proyecto1/__init__.py:** archivo vacío que le indica a *Python* que este directorio debería ser considerado como un paquete *Python*.

* **proyecto1/settings.py:** Ajustes/configuración para este proyecto Django (para más información ver [Django Settings](https://docs.djangoproject.com/es/3.1/topics/settings/)).


* **proyecto1/urls.py:** declaraciones URL para este proyecto *Django*; una «tabla de contenidos» nuestro sitio basado en *Django* (más información [URL dispatcher](https://docs.djangoproject.com/es/3.1/topics/http/urls/)).

* **proyecto1/asgi.py:** punto de entrada para servidores web compatibles con ASGI.

* **proyecto1/wsgi.py**: Un punto de entrada para que los servidores web compatibles con WSGI.

**** 
### Servidor de desarrollo
Django viene con un servidor ligero(escrito en *python*) para realizar pruebas, no es recomendado usarlo para proyectos grandes pues no admite peticiones simultaneas, y cargas de trabajo pesadas.

Ejecutando  el siguiente comando iniciamos el servidor de desarrollo:

`$ python manage.py runserver`

Con esto ya tenemos el servidor funcionando, podemos comprobarlo visitando la dirección `http://127.0.0.1:8000/` y debería mostrar lo siguiente: 



<p align="center">
<img src = "img/img1.png" width="600">
</p>



***
### Referencias: 

* django project [[1](https://www.djangoproject.com/)].












