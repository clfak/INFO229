<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Redis_Logo.svg/1200px-Redis_Logo.svg.png" width= "400">
</p>


# Tutorial # 7: Redis
Este tutorial es introductorio  a *redis*, y está inspirado en [redis-tutorial-paso-a-paso](https://www.ionos.es/digitalguide/hosting/cuestiones-tecnicas/redis-tutorial-paso-a-paso/) de ionos.es, además de la documentación oficial de [redis](https://redis.io/documentation).

### Contenidos

1. **Introducción**

	**1.1** ¿Qué es ***Redis***?

	**1.2** Ventajas

	**1.3** ¿Cuándo usar ***Redis***?

2. **Instalación**
3. **Configuración** 
4. **Creación de entradas**

	**4.1** Strings 
	
	**4.2** Listas 

	**4.3** Sets

	**4.4** Hashes

5. **Otras funciones**



### 1. Introducción 
***
### 1.1 ¿Qué es *Redis*?

Redis (**R**emote **D**iccionary **S**erver), 
es un  gestor de base de datos no relacional de código abierto. *Redis* almacena estructuras de datos *key-value* en memoria. Entre los casos de uso principales de Redis se encuentran el almacenamiento en caché, la administración de sesiones, pub/sub y las clasificaciones. 

Redis es una opción popular para aplicaciones web, móviles, de juegos, de tecnología publicitaria y de IoT (Internet of things) que requieren mejor desempeño. 


### 1.2 Ventajas 

* **Desempeño**

	A diferencia de la mayoría de los  DBMS que almacenan los datos en el disco duro o en SSD, *Redis* los almacena en la memoria principal del servidor. Esto hace que eviten retrasos al  eliminar la necesidad de acceder a discos y pueden acceder a los datos con algoritmos más sencillos que utilizan menos instrucciones de la CPU.

* **Estructuras de datos en memoria**

	En *Redis* pueden almacenarse claves que se correspondan con diversos tipos de datos. El tipo fundamental de datos son las *cadenas*, que pueden estar compuestas de texto o datos binarios. Además de admitir listas de cadenas en el ordene en que se hayan agregado, cadenas sin ordenar, hashes, HyperLogLogs, y prácticamente cualquier tipo de dato.

* **Compatibilidad con lenguajes de Programación**

	Los desarrolladores de *Redis* tienen más de cien clientes de código abierto. Entre los cuales encontramos lenguajes como *Java*, *Python*, *PHP*, *C*, *C++*, *C#*, *JavaScript*, *Node.js*, *Ruby*, *R*, *Go*, entre otros.  

### 1.3 ¿Cuándo usar Redis?

Situaciones o casos en donde usar *Redis* es conveniente:

* **Almacenamiento en caché**
	
	*Redis*, situado "delante" de otra base de datos, crea una caché en memoria de alto rendimiento que reduce la latencia de acceso, incrementa el desempeño y alivia la carga de la base de datos relacional o NoSQL. 


* **Colas**

	La estructura de datos de listas de *Redis* facilita la implementación de una cola ligera y persistente. Las listas ofrecen operaciones atómicas, así como capacidades de bloqueo, por lo que resultan aptas para una variedad de aplicaciones que requieren un agente de mensajes fiable o una lista circular. 


* **Chat y mensajería**


	*Redis* es compatible con el estándar PUB/SUB con la correspondencia de patrones, esto le permite abastecer salas de chat de alto desempeño, transmisiones de comentarios en tiempo real e intercomunicación en los servidores. También puede utilizar PUB/SUB para activar acciones a partir de eventos publicados. 

* **Clasificaciones en tiempo real**

	Con la estructura de datos de conjuntos clasificados de *Redis*, los elementos se guardan en una lista ordenados por sus puntuaciones. Esto facilita la creación de clasificaciones dinámicas con el fin de mostrar quién va ganando en un juego o publicar los mensajes más populares, o cualquier otra aplicación en la que desee mostrar quién va liderando. 
 

###  2. Instalación
***

Descargamos *Redis* desde su [página oficial.](https://redis.io/download) 

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

### 4.1 Strings: 
Los strings son tipos de datos básicos para las bases de datos *key-value*. En *redis* los strings son una secuencia de bytes, que permite almacenar cualquier tipo de dato.

Para la creación de cadenas de caracteres, usamos el comando `set`:

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


Los strings pueden usarse para almacenar y recuperar información como sesiones de usuario, carritos de la compra, contadores, caché de HTML, caché de consultas a BBDD o llamadas a un API, y en general objetos serializados en XML, JSON o cualquier otro formato.


### 4.2 Listas

Las listas permiten almacenar secuencias de strings en el orden en el que fueron insertadas. En *redis* las listas están optimizadas para que añadir un elemento al inicio o al final de la lista.

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

Los *sets* son colecciones de *strings*, estas colecciones no siguen un orden particular, en los que se garantiza que los elementos del mismo son **únicos y no pueden estar duplicados**.
 
Por ejemplo podemos añadir un mismo elemento veinte veces, pero *redis* garantiza que sólo existirá una vez, lo que nos permite poder añadir elementos sin tener que preocuparnos previamente de si ya existen o no.

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

Las tablas hash permite almacenar cualquier entidad con sus atributos asociados (como una especie de tabla o diccionario), de forma que podamos recuperar únicamente el atributo de interés en cada momento. Una particularidad de *redis* es que se caracteriza por almacenar los hashes de forma bastante eficiente, lo que permite sacarle provecho a la memoria disponible.

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



 ### 5 Alternativas 
 ***
 Con *Redis* además de crear entradas en una base de datos, podemos asignar propiedades a los datos. *Redis* es capaz de interpretar valores numéricos y puede llevar a cabo operaciones de incremento/decremento de manera atómica sobre los mismos. 
 Por ejemplo, podemos implementar los comandos de incremento(`incr`) y decremento(`decr`):
 

    127.0.0.1:6379> set foo 1
    OK
    127.0.0.1:6379> get foo
    "1"
    127.0.0.1:6379> incr foo
    (integer) 2
    127.0.0.1:6379> incr foo
    (integer) 3
    127.0.0.1:6379> get foo
    "3"
    127.0.0.1:6379> decr foo
    (integer) 2
    127.0.0.1:6379> get foo
    "2"
   
   Las funciones anteriores pueden ser útiles para reducir o incrementar valores en una unidad.Esto nos permite utilizarlo para generar identificadores únicos desde múltiples clientes, o en general para casos de uso en los que se requieran contadores, como contabilizar votos de usuarios, visualizaciones de productos, cantidades compradas de un artículo, visitas a una página, etc.



Si se quiere introducir valores en la base de datos que solo permanezcan un cierto tiempo en ella, podemos usar la  función `expire`, este comando necesita una indicación de tiempo ( en segundos), con `ttl` (*time to live*) mostramos el tiempo restante de la entrada, cuando el tiempo es negativo la entrada ya ha desaparecido.  

    127.0.0.1:6379> set foo "bar"
    OK
    127.0.0.1:6379> expire foo 40
    (integer) 1
    127.0.0.1:6379> ttl foo
    (integer) 33
    127.0.0.1:6379> ttl foo
    (integer) 19
    127.0.0.1:6379> ttl foo
    (integer) 3
    127.0.0.1:6379> ttl foo
    (integer) -2
    127.0.0.1:6379> get foo
    (nil)

Con `setex` podemos asignar un TTL a una entrada de la base de datos desde su creación.

    127.0.0.1:6379> setex foo 40 "bar"
    OK

Una vez se ha creado la entrada, usando el comando `append` ampliamos la entrada añadiendo otro valor al ya existente. Si la entrada no existe, `append`  realiza la misma acción  que la función `set`:

    127.0.0.1:6379> set foo "hello"
    OK
    127.0.0.1:6379> append foo " word"
    (integer) 10
    127.0.0.1:6379> get foo
    "hello word"
    127.0.0.1:6379> set bar 5
    OK
    127.0.0.1:6379> append bar 10
    (integer) 3
    127.0.0.1:6379> get bar
    "510"


También podemos renombrar las entradas usando el comando `rename`:

    127.0.0.1:6379> set foo 4
    OK
    127.0.0.1:6379> rename foo bar
    OK
    127.0.0.1:6379> get foo
    (nil)
    127.0.0.1:6379> get bar
    "4"




