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
    
    
### 4.3 Sets

Los *sets* son colecciones de *strings*, estas colecciones no siguen un orden particular, en los que se garantiza que los elementos del mismo son **únicos y no pueden estar duplicados**. Podemos añadir un mismo elemento más de una vez, pero Redis garantiza que sólo existirá una vez, lo que nos permite poder añadir elementos sin tener que preocuparnos previamente de si ya existen o no.
Con el comando `sadd` se integran varios elementos en el *set*, esto si se introducen en el comando uno detrás de otro.

    127.0.0.1:6379> sadd myset "foo"
    (integer) 1
    127.0.0.1:6379> sadd myset "bar"
    (integer) 1

Utilizamos `smembers` y el nombre del *set* para visualizarlo:

    127.0.0.1:6379> smembers myset
    1) "foo"
    2) "bar"

Para buscar una entrada concreta usamos `sismeber`, y `srem`para eliminar entradas sueltas:

    127.0.0.1:6379> sismember myset "bar"
    (integer) 1
    127.0.0.1:6379>  srem myset "bar"
    (integer) 1
    127.0.0.1:6379> smembers myset
    1) "foo"

    
### 4.4 Hashes 
    
Un hash permite asociar a una clave una colección de pares *key-value*, habitualmente usado para representar objetos. 
Podemos usar por ejemplo `hset` para crea un *hash* con el nombre *user1* y tres campos. Con el comando `hget` solicitamos el valor de cada campo:

    127.0.0.1:6379> hset user1 name "juan" email "juan@example.com" password "Rsx83_af"
    (integer) 0
    127.0.0.1:6379> hget user1 name
    "juan"
    
Con `hgetall` mostramos todos los campos: 

    127.0.0.1:6379> hgetall user1
    1) "name"
    2) "juan"
    3) "email"
    4) "juan@example.com"
    5) "password"
    6) "Rsx83_af"

Para ver los valores(*values*) guardados en la tabla hash usamos el comando `hvals`, mientras que `hkeys` muestra las claves(*keys*) almacenadas en el hash:

    127.0.0.1:6379> hvals user1
    1) "juan"
    2) "juan@example.com"
    3) "Rsx83_af"
    127.0.0.1:6379> hkeys user1
    1) "name"
    2) "email"
    3) "password"

Borramos valores sueltos con `hdel`, y con `del` borramos el hash completo:

    127.0.0.1:6379> hdel user1 password
    (integer) 1
    127.0.0.1:6379> hgetall user1
    1) "name"
    2) "juan"
    3) "email"
    4) "juan@example.com"
    127.0.0.1:6379> del user1
    (integer) 1
    127.0.0.1:6379> hgetall user1 
    (empty array)

**NOTA** : con `flushall` se borran todas las entradas de la base de datos.
