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
- **Frontend:** HTML + CSS  
- **Entorno Virtual:** `.env` para configuración segura  

---

## 🚀 Instalación y Configuración

### 1️⃣ Clonar el repositorio y entrar

```textplain
git clone https://github.com/Bootcamp-IA-P4/Track-Truck.git
cd Track-Truck
```

### 2️⃣ Descarga el entorno virtual:
⚠️ linux/mac
```textplain
python3 -m venv .venv
```
⚠️ windows
```texrplain
python -m venv .venv
```

### 3️⃣ Inicia el entorno virtual:
⚠️ linux/mac
```textplain
source .venv/bin/activate
```
⚠️ windows
```textplain
.venv\Scripts\activate
```

### 4️⃣ Descarga las siguientes dependencias:
```textplain
uv pip install -r requirements.txt
```
### 5️⃣ Configura variables de entorno
En el archivo .env en la raíz configura las siguiente variables:

```textplain
SECRET_KEY="tu_clave_secreta"
DEBUG=True
DATABASE_URL="postgres://usuario:contraseña@localhost:5432/nombre_db"
```
### 6️⃣ Accede a nuestra API:

```textplain
python manage.py runserver
```
> [!IMPORTANT]
> La API estará disponible en http://127.0.0.1:8000/

## 📌 Uso de la API
---
## 🔹 Autenticación
---
### Registro de usuario
Endpoint: POST /api/auth/register/

Ejemplo de request:
```json
{
    "username": "empresa1",
    "password": "123456",
    "tipo_usuario": "empresa"
}
```
### Inicio de sesión
Endpoint: POST /api/auth/login/

Ejemplo de request:
```json
{
    "username": "empresa1",
    "password": "123456"
}
```
---
## 🔹 Gestión de Empresas
---
### Obtener todas las empresas
Obtiene una lista de todas las empresas registradas.

Endpoint: GET /companies/

Ejemplo de respuesta (`200 OK`)
```json
[
    {
        "id": 1,
        "name": "Empresa XYZ",
        "email": "contacto@xyz.com",
        "phone": "+123456789",
        "user_id": 101
    },
    {
        "id": 2,
        "name": "Empresa ABC",
        "email": "info@abc.com",
        "phone": "+987654321",
        "user_id": 102
    }
]
```
---
### Crear una empresa
Crea una nueva empresa en el sistema.

POST /companies/create/

Parámetros requeridos (JSON)
```json
{
    "user_id": 101,
    "name": "Empresa XYZ",
    "email": "contacto@xyz.com",
    "phone": "+123456789"
}
```

Ejemplo de respuesta (`201 Created`)
```json
{
    "id": 1,
    "user_id": 101,
    "name": "Empresa XYZ",
    "email": "contacto@xyz.com",
    "phone": "+123456789"
}
```
Ejemplo de posibles errores (400 Bad Request si falta el campo user_id)
```json
{
    "error": "user_id is required"
}
```
---
### Obtener detalles de una empresa
Obtiene los detalles de una empresa específica.

GET /companies/{id}/detail/

Ejemplo de respuesta (`200 OK`)
```json
{
    "id": 1,
    "user_id": 101,
    "name": "Empresa XYZ",
    "email": "contacto@xyz.com",
    "phone": "+123456789"
}
```
Ejemplo de posibles errores (`404 Not Found`) si la empresa no existe:
```json
{
    "detail": "Not found."
}
```
---
### Actualizar una empresa
 Actualiza todos los datos de una empresa.
 
 PUT /companies/{id}/update/

Parámetros requeridos (JSON)
```json
{
    "name": "Empresa Actualizada",
    "email": "nuevo@email.com",
    "phone": "+000000000",
    "address": "Calle 123",
    "user_id": 101
}
```

 Ejemplo de respuesta (`200 OK`)
 ```json
{
    "id": 1,
    "user_id": 101,
    "name": "Empresa Actualizada",
    "email": "nuevo@email.com",
    "phone": "+000000000",
    "address": "Calle 123"
}
```
---
### Actualización parcial de una empresa
Permite actualizar solo algunos campos de la empresa.

PATCH /companies/{id}/update/

Ejemplo de petición (JSON)
```json
{
    "phone": "+111111111"
}
```

Ejemplo de respuesta (`200 OK`)
```json
{
    "id": 1,
    "user_id": 101,
    "name": "Empresa XYZ",
    "email": "contacto@xyz.com",
    "phone": "+111111111"
}
```
---
### Eliminar una empresa
Elimina una empresa del sistema.

DELETE /companies/{id}/delete/

Ejemplo de respuesta (`204 No Content`)

(No retorna contenido)

Posibles errores:

`404 Not Found` si la empresa no existe.

---

## Vistas HTML (Interfaz Web)
1. Crear una empresa desde formulario
URL: /companies/create/form/{user_id}/
Muestra un formulario para registrar una empresa.

* Si la empresa se crea correctamente, redirige a home.
* En caso de error, recarga la página con un mensaje de error.

2. Dashboard de una empresa
URL: /companies/{id}/cp-dashboard/
Muestra los detalles de una empresa y una lista de sus envíos.

3. Actualizar empresa desde formulario
URL: /companies/{id}/cp-update/
Formulario para actualizar los datos de una empresa.

* Si la actualización es exitosa, redirige al dashboard de la empresa.
* Si hay un error, muestra un mensaje en la página.

>[!NOTE]
> * Se utiliza logging para registrar eventos (creación, actualización, eliminación, etc.).
>
> * Se manejan fechas en formato YYYY-MM-DD HH:MM.
>
> * La API usa requests para realizar llamadas internas a otros servicios.

### 🔹 Gestión de Rutas
Crear una nueva ruta
Endpoint: POST /api/rutas/

Ejemplo de request:
```json
{
    "empresa": 1,
    "camionero": 2,
    "origen": "Madrid",
    "destino": "Galicia",
    "fecha_envio": "2024-03-10",
    "estado": "pendiente"
}
```

## 🤝 Contribución  

¡Las contribuciones son bienvenidas! Para contribuir:  

1. Haz un fork del repositorio.  
2. Crea una nueva rama:  
   ```sh
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz commit:
  ```sh
git commit -m "Añadir nueva funcionalidad"
```

4. Envía un pull request 🚀.
---
## 📜 Licencia
Este proyecto está bajo la licencia MIT. Puedes ver más detalles en el archivo LICENSE
---
# 🚀 ¡Gracias por usar Track-Truck! Si tienes preguntas, crea un issue en el repositorio o contáctanos.
