# Comandos esenciales de Docker pt 2

## 1. Redes

Los tipos de redes más importantes para nosotros son:

    * Bridge: Crea una red "puente" con el sistema operativo. Utiliza NAT para conexiones fuera del contenedor, es decir, usa al host como intermediario.
    * Host: Comparte la misma red del ordenador. OJO: En windows (hyper-v) y en MacOS hay una máquina virtual de por medio, por lo que realmente comparte red con la máquina virtual intermedia, no el host en si.
    * none: contenedor totalmente aislado.

### Listar networks
    docker network ls


## 2. Gestión de volumenes


### Bind Mounts

    Se puede montar un volumen desde una carpeta que quieras en tu sistema operativo:

    docker run -d -v <direccion absoluta o relativa>:<lugar de montaje dentro del contenedor> <Imagen>

    Por ejemplo:

    docker run -d -v $(pwd)/vol:/app/data --name micont nginx

    Es importante poner rutas ABSOLUTAS del lado del host, ya que docker de lo contrario se puede liar un poco.

### Volumenes gestionados

    Una opción sencilla es usar volumenes gestionados por docker. Se crean de la siguiente manera:

    docker volume create <nombre>

    luego, para montarlo:

    docker run -d --name micont -v <nombre>:<ruta dentro del contenedor> <imagen>
