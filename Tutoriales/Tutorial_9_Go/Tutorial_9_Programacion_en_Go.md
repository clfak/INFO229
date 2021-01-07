<p align="center">
<img src = "img/gopher_head-1462551971634.png" width="400">
</p>

# PROGRAMACIÓN EN  GO
	
## ¿Qué es go?

Go es un lenguaje de programación de código abierto que facilita la construcción de software de manera simple, segura y eficiente.

    agregar mas cosas acá 

### 1. Instalación 

Las distribuciones de Go están disponibles para Linux, macOS, Windows, podrá descargarlo en el siguiente [link](https://golang.org/dl/), también podrá encontrar las instrucciones de instalación [aquí](https://golang.org/doc/install).


### Instalación en Linux 

Una vez descargamos el archivo, abrimos una terminal, ubicamos la carpeta donde se descargó el archivo .tar y lo extraemos en la ruta /usr/local:

    $ sudo tar -C /usr/local -xzf gox.xx.x.linux-xxx.tar.gz

Agregamos /usr/local/go/bin a la variable de entorno PATH. 
Podemos hacerlo añadiendo la siguiente linea en $HOME/.profile(solo para un usuario= o /etc/profile (para todos los usuarios):

    export PATH=$PATH:/usr/local/go/bin

Verificamos que la instalación se haya realizado correctamente ejecutando el siguiente comando: 

    $ go version

### Ejemplos en Go
**Ejemplo 1:** ***Hello World***

En un editor de texto de preferencia, creamos un archivo helloworld.go, y escribimos el siguiente código: 

    package main 
    import "fmt"
    func main(){
	    fmt.Println("Hello World")
    }
Desglosando el código anterior: 

 - Declarar un `main` package (en todos los archivos go  debemos declarar el paquete al que pertenecen usando la sentencia ***package***, esto es una forma de agrupar funciones).
 - Importar el [packege fmt](https://golang.org/pkg/fmt/), el cual contiene funciones para el formato de texto, incluyendo la función `Println` que nos permite realizar una impresión en consola.

Para ejecutar el código: 

    go run helloworld.go

 

#### Fuentes  y referencias:
+ https://medium.com/@golang_es/instalaci%C3%B3n-de-go-golang-6fd5d7b9eb48


  
  

  
  

