<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Redis_Logo.svg/1200px-Redis_Logo.svg.png" width= "400">
</p>

###  Instalación

Descargamos Redis desde su [página oficial.](https://redis.io/download) 

**Desde la PPA oficial de ubuntu**

Instalamos la última versión estable de Redis desde repositorio redislabs/redis.

    $ sudo add-apt-repository ppa:redislabs/redis
    $ sudo apt-get update 
    $ sudo ap-get install redis


Luego de instalar, iniciamos Redis:

    redis-server

Podemos comprobar si Redis funciona correctamente iniciando la interfaz de comunicación con la base de datos:

    redis-cli 

La respuesta en consola debería mostrar la dirección IP y el puerto en donde se ejecuta Redis, le enviamos un ping de comprobación:

    127.0.0.1:6379> ping
    PONG
    
Si obtenemos respuesta de Redis, hemos comprobado que se ha instalado correctamente. Podemos hacer también una comprobación de escritura de texto:

    127.0.0.1:6379> set test "hola"
    OK
    127.0.0.1:6379> get test
    "hola"


