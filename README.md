# Fondeadora
Un acortador de URL es un servicio que crea alias cortos para URL. Genera un código abreviado para una URL y luego redirige al usuario a la URL cuando se accede a ese código.

 ### Requerimientos
 - Docker
 - Docker Compose
 

 ### Instalar Docker
 El primer paso es instalar la aplicación Docker de escritorio para su máquina local:
 - [Docker para Mac](https://docs.docker.com/docker-for-mac/install/)
 - [Docker para Windows](https://docs.docker.com/docker-for-windows/install/)
 - [Docker para Linux](https://docs.docker.com/engine/install/#server)

 Docker Compose es una herramienta adicional que se incluye automáticamente con las descargas de Docker para Mac y Windows. Sin embargo, si está en Linux, deberá agregarlo manualmente. Puede hacer esto ejecutando el comando sudo pip install docker-compose una vez completada la instalación de Docker.


### Instalacion.

Clonar el proyecto
```sh
git clone https://github.com/jdht1992/fondeadoratest.git          
```

Para crear la imagen ejecutas los siguientes comandos
```sh
cd fondeadoratest
docker-compose up --build
```

### Ejecutar proyecto.

Para ejecutar las migraciones, abrir otra terminal y entrar al contenedor y ejecutar los siguientes comandos.
```sh
docker-compose exec web bash 
python manage.py migrate
```

Para ejecutar los test se corre el comando.
```sh
pytest
```

## Rutas del proyecto
### Shortener

Uno acepta una URL a través de una solicitud POST y devuelve un código abreviado

endpoint
```sh
localhost:8000/shortener/api/v1/shortcode
```
payload
```sh
{
  "url": "https://www.youtube.com/watch?v=_pyYJCsCka0"
}
```
response
```sh
{
    "shortcode": "o9gf82"
}
```
El otro acepta un código abreviado a través de una solicitud GET y devuelve la URL original

endpoint
```sh
localhost:8000/shortener/api/v1/shortcode/<shortcode>/
```

response
```sh
{
    "url": "https://www.youtube.com/watch?v=PyNQi6zU80o"
}
```
