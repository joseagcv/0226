# Imagen Base, siempre partimos de alguna, en nuestro caso partiremos de la imagen ubuntu

FROM ubuntu


ARG WORKDIR

ENV USER user01
ENV FULL_WORKDIR /$USER/$WORKDIR

# Aquí definimos desde cuál directorio las siguientes acciones serán ejecutadas
WORKDIR $FULL_WORKDIR

# Con este comando copiamos todos los ficheros que necesitamos
# CUIDADO: Solo se pueden agregar ficheros y directorios que existan al mismo nivel que el Dockerfile!!!
COPY ./src ./

# Con el comando RUN podemos ejecutar cualquier comando Linux
RUN mv script2.sh script.sh 

# Se pueden poner varias lineas con && \
RUN echo "hola" && \
    echo "varias lineas"


# Podemos crear usuarios con este comando
RUN useradd -ms /bin/bash user01

# Cambiamos el usuario 
USER $USER

# EL ENTRYPOINT es el comando que ejecutará el contenedor, es el proceso principal y si este acaba
# el contenedor se apaga. ES MUY DIFICIL SOBRESCRIBIRLO!
ENTRYPOINT ["./script.sh"]

# Aquí podemos sobrescribir los argumentos del entrypoint. Si no existe el entrypoint, se arranca desde el CMD
CMD ["hola pontIA", "mas argumentos", "hola"]
