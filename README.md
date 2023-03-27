<p align="center">
  <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" width="200" alt="Python Logo" />
</p>


# Bk_service


1. Clonar proyecto
2. Ubicar el archivo ```Local .py``` en la siguiente carpeta:
```
../bk_service_py/config/settings/local.py
```
3. Cambiar el valor ```true``` por ```false``` en la siguiente linea:
```
DEBUG = False
```
4. Abrir el proyecto en ```Visual Studio Code``` y en la terminal integrada correr el siguiente comando:
```
export COMPOSE_FILE=local.yml
```
```NOTA:```
Puedes verificar que la variable de entorno se ha establecido correctamente ejecutando el comando:
```
echo $COMPOSE_FILE
```
5. Genera la imagen ejecutando el comando:
```
docker-compose build
```
6. En Docker Desktop podras verificar que se crea el contenedor:

```bk_service_py```

podras darle play para poner a funcionar el contenedor