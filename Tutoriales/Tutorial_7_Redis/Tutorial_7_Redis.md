<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Redis_Logo.svg/1200px-Redis_Logo.svg.png" width= "400">
</p>

###  Instalación

Descargamos Redis desde su [página oficial.](https://redis.io/download) 

**Desde la PPA oficial de ubuntu**

Instalamos la última versión estable de Redis desde su repositorio redislabs/redis, añadimos el repositorio a la apt, acualizamos e instalamos: 

    $ sudo add-apt-repository ppa:redislabs/redis
    $ sudo apt-get update 
    $ sudo ap-get install redis
