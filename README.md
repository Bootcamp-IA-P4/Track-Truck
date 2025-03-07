# Track-Truck 🚚

## ¿Qué es Track Truck?

API REST que conecta empresas con conductores para facilitar el transporte de mercancías.
Permite a las empresas publicar rutas y a los conductores encontrar oportunidades de transporte.

### 🌟 Características
✅ Registro y autenticación de usuarios (empresas y conductores).  
✅ Publicación y gestión de rutas de transporte.  
✅ Asignación de rutas a conductores.  
✅ Documentación interactiva con Swagger. 

---

## 🛠️ Tecnologías Utilizadas

- **Backend:** Django REST Framework (DRF) + Python  
- **Base de Datos:** PostgreSQL  
- **Frontend:** HTML + CSS (básico)  
- **Entorno Virtual:** `.env` para configuración segura  

---

## 🚀 Instalación y Configuración

### 1️⃣ Clonar el repositorio

```textplain
git clone
```
### 2️⃣ Entramos:

```textplain
cd Track-Truck
```

### 3️⃣ Descarga el entorno virtual:
⚠️ linux/mac
```textplain
uv venv .venv
```

### 4️⃣ Inicia el entorno virtual:

```textplain
source .venv/bin/activate
```

### 5️⃣ Descarga las siguientes dependencias:
```textplain
uv pip install -r requirements.txt
```

### 6️⃣ Edita el archivo .env y retira la palabra .example

Descargamos requests:

```textplain
uv pip install requests
```
### 7️⃣ Ejecuta las migraciones:

```texplain
python manage.py migrate
```

### 8️⃣ Accede a nuestra API:

```textplain
python manage.py runserver
```
