# Track-Truck
Grupo 1- Api rest

Como usar nuestra API:

primero descarga este repositorio:

```textplain
git clone
```
Entramos:

```textplain
cd Track-Truck
```

Descarga el entorno virtual:

```textplain
uv venv .venv
```

Inicia el entorno virtual:

```textplain
source .venv/bin/activate
```

Descargamos las siguientes dependencias:
```textplain
uv pip install -r requirements.txt
```

Editamos el archivo .env y le retiramos la palabra .example

Descargamos requests:

```textplain
uv pip install requests
```

Y ahora estas listo para acceder a nuestra API:

```textplain
python manage.py runserver
```
