# Comandos esenciales de Docker

## 1. Gestión de imágenes

Las imágenes son plantillas inmutables a partir de las cuales se crean los contenedores.

### Listar imágenes locales
    docker images

### Descargar imagenes en local
    docker pull <imagen>:<tag>

### Listar imágenes locales
    docker images

### Eliminar imagen en local
    docker rmi <imagen>

### Construir imagen en local
    docker build -t <nombre_imagen>:<tag> .


## 2. Gestión de contenedores

### Ejecutar un contenedor en base a una imagen.
    docker run <imagen> 

    Este comando ejecuta un contenedor desde la terminal, quedandose está "bloqueada" y mostrando la salida de lo que pasa dentro del contenedor.

### Ejecutar en segundo plano
    docker run -d <imagen> 

    Con la opción '-d' luego del run, indicamos que la imagen debe ejecutarse en segundo plano, dejando la terminal disponible.

### Listar contenedores en ejecución

    docker ps
        ó
    docker ps -a

    El primero nos muestra las contenedores ACTUALMENTE en estado Running, es decir, arrancados y vivos. Con la opción '-a' hacemos que aparezcan todos, incluso los que ya han parado o están en pausa.

    Este comando saca una tabla con las siguientes cabeceras:

    CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES


### Listar logs del contenedor.

    docker logs <CONTAINER ID>

    Al ejecutar un contenedor en segundo plano, perdemos el acceso inmediato en la consola de los logs dentro del contenedor. Los logs son fundamenteales para la tarea de depurar errores o simplemente verificar el correcto funcionamiento. Con el comando anterior, podemos listar los logs de un contenedor, pero necesitamos su id anteriormente listado.

    Si queremos evitar tener que contar los logs por el id, le podemos poner un nombre al contenedor con el parametro 'name':

    docker run -d --name "minombre" <imagen> 

    Esto permite hacer:

    docker logs minombre.

    IMPORTANTE: El nombre debe ser único entre todos los contenedores arrancados o parados.

### Exponer los puertos del contenedor.

    Todo lo que ejecutemos en un contenedor, está aislado en su propio entorno, es decir, no tengo acceso a sus puertos facilmente, nisiquiera desde la máquina anfitrión (el host). Si quiero exponer un puerto TCP a mi máquina anfitrión, el comando es:

    docker run -p <Puerto del Host>:<Puerto dentro del contenedor> <imagen>

    Ejemplo: Si tenemos una app de fastAPI expuesta en el puerto 8080 y queremos tener acceso a nuesta aplicación utilizando el mismo número de puerto del host:

    docker run -p 8080:8080 <imagen>

### Borrar un contenedor

    docker rm <id_o_nombre>

    A veces es importante borrarlos, como por ejemplo cuando existe ya otro contenedor con el mismo nombre o por simplemente liberar memoria.

## 3. Interacción con contenedores

    docker exec -it <contenedor> /bin/bash

    Este comando sirve para conectarnos dentro del contenedor. Es interesante porque así podemos mirar el sistema de fichero, los procesos arrancados e incluso hacer un curl a nuestra aplicación internamente. 

### Inspeccionar un contenedor

    docker inspect <contenedor>

    Con este comando podemos ver cual fue el punto de entrada (ENTRYPOINT o CMD) del contenedor, que variables de entorno tiene y más cosas...

## 4. Otros

### CURLS

    GET:

        Básico:
        
        curl https://api.ejemplo.com/users

        Con cabeceras:

        curl -H "Accept: application/json" \
        https://api.ejemplo.com/users

        Con cabecera de autorizacion:

        curl -H "Authorization: Bearer TOKEN" \
        -H "Accept: application/json" \
        https://api.ejemplo.com/users

    POST:

        Con header y body:

        curl -X POST https://api.ejemplo.com/users \
        -H "Content-Type: application/json" \
        -d '{
            "name": "Juan",
            "email": "juan@example.com"
            }'

    PUT:

        curl -X PUT https://api.ejemplo.com/users/1 \
        -H "Content-Type: application/json" \
        -d '{
            "name": "Juan Actualizado",
            "email": "juan.updated@example.com"
            }'

    DELETE: 

        curl -X DELETE https://api.ejemplo.com/users/1 \
        -H "Authorization: Bearer TOKEN"
