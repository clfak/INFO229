<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Redis_Logo.svg/1200px-Redis_Logo.svg.png" width= "400">
</p>

### Contenidos

1. Introducción.
2. Instalación
3. Configuración 
4. Creación de entradas 
5. Fuentes


### 1. Introducción 
***
Redis (**R**emote **D**iccionary **S**erver), 


es gestor de base de datos no relacional de código abierto, 

###  2. Instalación
***

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

### 3. Configuración
***
Luego de instalarse, Redis mantiene la configuración por defecto. Podemos modificar la configuración, con el siguiente comando: 

    127.0.0.1:6379> config get *

El comando anterior nos mostrará una lista de elementos, estas parejas de elementos se descomponen en dos posiciones, por ejemplo:

    127.0.0.1:6379> config get dbfilename
    1) "dbfilename"
    2) "dump.rdb"

Al elemento *dbfilename*  le corresponde el valor *dump.rdb*, la llave corresponde al primer elemento para el valor de configuración correspondiente.

Podemos cambiar una entrada en el archivo de configuración usando el comando `set`. Por ejemplo, definimos una contraseña:

    127.0.0.1:6379> config set requirepass "password"
    OK

Una vez realizado esto, si solicitamos la contraseña con el comando `get`, se nos pedirá una autentificación, usando el comando `auth`, consultamos la entrada en el archivo de configuración anterior:

    127.0.0.1:6379> auth "password"
    OK
    127.0.0.1:6379> config get requirepass
    1) "requirepass"
    2) "password"

Redis almacena todos los datos en memoria principal. Si tenemos esto en cuenta, para lograr la persistencia de los datos, podemos almacenar una copia de la base de datos en el disco duro, que se ubicará en el archivo *dump.rdb*. Se puede crear una copia manualmente con el comando `save`.

    127.0.0.1:6379> save

También podemos programar la copia para que se realice de forma automática, por ejemplo, podemos asignarle dos parámetros, para que se cree una copia cada 60 segundos si ya se han producido 10 cambios en ese periodo de tiempo.

    127.0.0.1:6379> save 60 10 
 
La desventaja del comando `save` es que no se recomienda mientras el sistema esté en funcionamiento, pues impide que los clientes accedan a la base de datos. Para estos casos lo más recomendable es usar `bgsave`, que realiza el proceso en segundo plano.


### 4. Creación de entradas
***
 **Strings:** para la creación de cadenas de caracteres, usamos el comando `set`:

    127.0.0.1:6397> set foo "bar"
    127.0.0.1:6397> set value 1
    
  Solicitamos las entradas *foo* y *value* mediante el comando `get`:
  

    127.0.0.1:6379> get foo
    "bar"
    127.0.0.1:6379> get value
    "1"

Con el comando `del` borramos las entradas:

    127.0.0.1:6379> del foo
    (integer) 1
    127.0.0.1:6379> get foo
    (nil)
    
También podemos crear varias entradas en una misma fila,  usando la función `mset`:

    127.0.0.1:6379> mset foo1 "bar1" foo2 "bar2" foo3 "bar3"
    OK

Con `mget` solicitamos los valores de varios campos a la vez: 

    127.0.0.1:6379> mget foo1 foo2 foo3
    1) "bar1"
    2) "bar2"
    3) "bar3"


### 4.2 Listas

A diferencia de los ***sets*** que no tienen  un orden en particular, las ***listas*** están numeradas. En ellas podemos solicitar o borrar entradas.

Por ejemplo, podemos añadir elementos a la lista con el comando `lpush`:

    127.0.0.1:6379> lpush mylist foo 
    (integer) 1
    127.0.0.1:6379> lpush mylist bar
    (integer) 2

Con el comando `lrange`, indicamos que segmento de la lista debe mostrarse: 

    127.0.0.1:6379> lrange mylist 0 10
    1) "bar"
    2) "foo"

Usando `linsert`, añadimos un valor nuevo delante (*before*) de uno ya existente (también puede usarse *after*):

    127.0.0.1:6379> linsert mylist before "bar" "test"
    (integer) 3
    127.0.0.1:6379> lrange mylist 0 10
    1) "test"
    2) "bar"
    3) "foo"
    127.0.0.1:6379> 

Para eliminar de la lista entradas con valor específico usamos el comando `lrem`:

    127.0.0.1:6379> lrem mylist 0 foo
    (integer) 1
    127.0.0.1:6379> lrange mylist 0 10
    1) "test"
    2) "bar"
