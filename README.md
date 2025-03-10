# Track-Truck 🚚
<details>
  <summary>¿Que voy a encontrarme?</summary>
  <ol>
    <li>
      <a href="#¿Qué-es-Track-Truck?">¿Qué es Track Truck?</a>
      <ul>
        <li><a href="#Características"> Características</a></li>
      </ul>
    </li>
    <li><a href="#Tecnologías-Utilizadas">Tecnologías Utilizadas</a></li>
    <li><a href="#Instalación-y-Configuración">Instalación y Configuración</a></li>
    <li>
        <a href="#Uso-de-la-API">Uso de la API</a>
    <ul>
        <li><a href="#Autenticación">Autenticación</a></li>
        <li><a href="#Gestión-de-Empresas">Gestión de Empresas</a></li>
         <li><a href="#Gestión-de-Conductores">Gestión de Conductores</a></li>
        <li><a href="#Gestión-de-Envíos">Gestión de Envíos</a></li>
      </ul>
    </li>
     <li><a href="#Contribución">Contribución</a></li>
  </ol>
</details>


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
- **Frontend:** HTML + CSS + Bootstrap 
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
> La API estará disponible en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📌 Uso de la API
---
> [!NOTE]
> Si quieres ver esto de forma más visual visita:
>
> Swagger UI: http://localhost:8000/docs/
> 
> ![docs](https://github.com/Bootcamp-IA-P4/Track-Truck/blob/docs/readme/static/images/docs-swagger-_1_.gif)
> 
> Redoc UI: http://localhost:8000/redoc/
> 
>  ![redoc](https://github.com/Bootcamp-IA-P4/Track-Truck/blob/docs/readme/static/images/redoc-swagger-_1_.gif)


## 🔹 Autenticación
---
### Registro de usuario
Permite a los usuarios registrarse en la plataforma.

Endpoint: POST /users/signin/

Parámetros requeridos (Formulario o JSON)
```json
{
    "username": "usuario123",
    "password1": "ContraseñaSegura123",
    "password2": "ContraseñaSegura123",
    "email": "usuario@example.com",
    "user_type": "company"  // Opciones: "company" o "driver"
}
```

> [!NOTE]
> Flujo de redirección:
> 
> * Si el usuario se registra como empresa → Redirige a companies:create_company_form
>  
> * Si el usuario se registra como conductor → Redirige a drivers:create_driver_form


Ejemplo de respuesta (`200 OK`) ✔️
```json
{
    "message": "Usuario registrado correctamente",
    "redirect": "/companies/create/"
}

```
Ejemplo de posibles errores:

(`400 Bad Request`) si las contraseñas no coinciden o faltan datos. ❌

> [!IMPORTANT]
> (`400 Bad Request`) si se registra un usuario con el mismo email/username,  un driver con el mismo truck plate, una empresa con el mismo nombre.
> Estas validaciones son personalizadas

---
### Inicio de sesión
Permite a los usuarios iniciar sesión con sus credenciales.

Endpoint: POST /api/auth/login/

Parámetros requeridos (Formulario o JSON):
```json
{
    "email": "usuario123@user.com",
    "password": "ContraseñaSegura123"
}
```

Ejemplo de respuesta (200 OK). ✔️
```json
{
    "message": "Inicio de sesión exitoso",
    "redirect": "/home"
}

```

> Ejemplo de posibles errores ❌ :
> > `401 Unauthorized` si las credenciales son incorrectas.
> > 
> > `400 Bad Request` si faltan datos.
---
### Cierre de sesión
Cierra la sesión del usuario y lo redirige a la página de inicio de sesión.

Endpoint: GET /users/logout/

Ejemplo de respuesta (`302 Redirect`)

(Redirige a [/users/login/](/users/login/))

---

> [!NOTE]
>
> Se utilizan formularios personalizados:
> 
> * CustomUserCreationForm para el registro.
> 
> * CustomAuthenticationForm para el inicio de sesión.
> 
> Se usa auth_login y auth_logout de Django para manejar sesiones.
> 
> Se redirige a diferentes vistas según el tipo de usuario registrado.

---

## 🔹 Gestión de Empresas
---
### Obtener todas las empresas
Obtiene una lista de todas las empresas registradas.

Endpoint: GET /companies/

Ejemplo de respuesta (`200 OK`). ✔️
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

Endpoint: POST /companies/create/

Parámetros requeridos (JSON)
```json
{
    "user_id": 101,
    "name": "Empresa XYZ",
    "email": "contacto@xyz.com",
    "phone": "+123456789"
}
```

Ejemplo de respuesta (`201 Created`). ✔️
```json
{
    "id": 1,
    "user_id": 101,
    "name": "Empresa XYZ",
    "email": "contacto@xyz.com",
    "phone": "+123456789"
}
```
Ejemplo de posibles errores (`400 Bad Request`) si falta el campo user_id. ❌
```json
{
    "error": "user_id is required"
}
```
---
### Obtener detalles de una empresa
Obtiene los detalles de una empresa específica.

Endpoint: GET /companies/{id}/detail/

Ejemplo de respuesta (`200 OK`) ✔️
```json
{
    "id": 1,
    "user_id": 101,
    "name": "Empresa XYZ",
    "email": "contacto@xyz.com",
    "phone": "+123456789"
}
```
Ejemplo de posibles errores (`404 Not Found`) si la empresa no existe. ❌
```json
{
    "detail": "Not found."
}
```
---
### Actualizar una empresa
 Actualiza todos los datos de una empresa.
 
 Endpoint: PUT /companies/{id}/update/

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

 Ejemplo de respuesta (`200 OK`) ✔️
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

Endpoint: PATCH /companies/{id}/update/

Ejemplo de petición (JSON)
```json
{
    "phone": "+111111111"
}
```

Ejemplo de respuesta (`200 OK`) ✔️
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

Endpoint: DELETE /companies/{id}/delete/

Ejemplo de respuesta (`204 No Content`) ✔️

(No retorna contenido)

Posibles errores:

`404 Not Found` si la empresa no existe. ❌

---

## Vistas HTML (Interfaz Web)
1. Crear una empresa desde formulario
URL: [create_companies_form/<int:user_id>/](create_companies_form/<int:user_id>/)
Muestra un formulario para registrar una empresa.

* Si la empresa se crea correctamente, redirige a home.
* En caso de error, recarga la página con un mensaje de error.

2. Dashboard de una empresa
URL: [/companies/{id}/cp-dashboard/](/companies/{id}/cp-dashboard/)
Muestra los detalles de una empresa y una lista de sus envíos.

3. Actualizar empresa desde formulario
URL: [/companies/{id}/cp-update/](/companies/{id}/cp-update/)
Formulario para actualizar los datos de una empresa.

* Si la actualización es exitosa, redirige al dashboard de la empresa.
* Si hay un error, muestra un mensaje en la página.

>[!NOTE]
> * Se utiliza logging para registrar eventos (creación, actualización, eliminación, etc.).
>
> * Se manejan fechas en formato YYYY-MM-DD HH:MM.
>
> * La API usa requests para realizar llamadas internas a otros servicios.

--- 
## 🔹Gestión de Conductores
---

### Obtener todos los conductores
Obtiene una lista de todos los conductores registrados.

Endpoint: GET /drivers/

Ejemplo de respuesta (`200 OK`). ✔️
```json
[
    {
        "id": 1,
        "name": "Juan Pérez",
        "truck_plate": "XYZ123",
        "phone": "+123456789",
        "user": 101
    },
    {
        "id": 2,
        "name": "Ana López",
        "truck_plate": "ABC987",
        "phone": "+987654321",
        "user": 102
    }
]
```
---

### Crear un nuevo conductor
Registra un nuevo conductor en el sistema.

Endpoint: POST /drivers/create/

Parámetros requeridos (JSON):
```json
{
    "user": 101,
    "name": "Juan Pérez",
    "truck_plate": "XYZ123",
    "phone": "+123456789"
}
```
Ejemplo de respuesta (`201 Created`)
```json
{
    "id": 1,
    "user": 101,
    "name": "Juan Pérez",
    "truck_plate": "XYZ123",
    "phone": "+123456789"
}
```
Posibles errores ❌:

`400 Bad Request` si los datos son incorrectos.

---

### Obtener detalles de un conductor
Obtiene la información de un conductor específico.

Endpoint: GET /drivers/{id}/detail/

Ejemplo de respuesta (`200 OK`). ✔️
```json
{
    "id": 1,
    "user": 101,
    "name": "Juan Pérez",
    "truck_plate": "XYZ123",
    "phone": "+123456789"
}
```
Posibles errores `404 Not Found` si el conductor no existe. ❌
```json
{
    "detail": "Not found."
}
```
---

### Actualizar un conductor
 Modifica todos los datos de un conductor.

 Endpoint: PUT /drivers/{id}/update/

 Parámetros requeridos (JSON):
 ```json
{
    "name": "Juan Pérez",
    "truck_plate": "XYZ789",
    "phone": "+000000000",
    "user": 101
}
```

Ejemplo de respuesta (`200 OK`) ✔️
```json
{
    "id": 1,
    "user": 101,
    "name": "Juan Pérez",
    "truck_plate": "XYZ789",
    "phone": "+000000000"
}
```

---

### Eliminar un conductor
Borra un conductor del sistema.

Endpoint: DELETE /drivers/{id}/delete/

Ejemplo de respuesta (`204 No Content`)

(No retorna contenido)

Posibles errores `404 Not Found` si el conductor no existe. ❌

---

### Vistas HTML (Interfaz Web)
1. Crear un conductor desde formulario
URL: [create_driver_form/<int:user_id>/](create_driver_form/<int:user_id>/)
Muestra un formulario para registrar un conductor.

* Si el conductor se crea correctamente, redirige a home.
* En caso de error, recarga la página con un mensaje de error.
  
2. Dashboard de un conductor
URL: [/drivers/{id}/dr-dashboard/](/drivers/{id}/dr-dashboard/)
Muestra los detalles de un conductor y una lista de sus envíos.

3. Actualizar conductor desde formulario
URL: [/drivers/{id}/dr-update/](/drivers/{id}/dr-update/)
Formulario para actualizar los datos de un conductor.

* Si la actualización es exitosa, redirige al dashboard del conductor.
* Si hay un error, muestra un mensaje en la página.

> [!NOTE]
> * Se utiliza requests para hacer llamadas a la API desde las vistas HTML.
>   
> * Se manejan fechas en formato YYYY-MM-DD HH:MM.
>   
> * La API devuelve errores detallados en caso de problemas con las solicitudes.

## 🔹Gestión de Envíos
---

### Crear un envío
Crea un nuevo envío con los datos proporcionados.

Endpoint: POST /shipments/create/

Parámetros requeridos (JSON):
```json
{
   "company_id": 1,
    "driver_id": null,
    "origin": "Madrid",
    "destination": "Barcelona",
    "status": "pending"
}
```

Ejemplo de respuesta (`200 OK`). ✔️
```json
{
    "id": 10,
    "company_id": 1,
    "driver_id": null,
    "origin": "Madrid",
    "destination": "Barcelona",
    "status": "pending",
    "created_at": "2024-06-01T12:00:00Z"
}
```

Posibles errores:
`400 Bad Request` si los datos son inválidos o faltan parámetros requeridos. ❌

---

### Obtener la lista de envíos
Devuelve una lista de todos los envíos.

Endpoint: GET /shipments/list/

Ejemplo de respuesta (`200 OK`). ✔️
```json
[
    {
        "id": 1,
        "company_id": 2,
        "driver_id": 5,
        "origin": "Sevilla",
        "destination": "Valencia",
        "status": "in_progress"
    },
    {
        "id": 2,
        "company_id": 3,
        "driver_id": null,
        "origin": "Madrid",
        "destination": "Bilbao",
        "status": "pending"
    }
]
```
Posibles errores: `400 Bad Request` en caso de fallo inesperado en la consulta. ❌

---

### Obtener envíos de una empresa
Devuelve los envíos pertenecientes a una empresa específica.

Endpoint: GET /shipments/company/{id}/

Parámetros de la URL:

`company_id`: ID de la empresa.

Ejemplo de respuesta (200 OK). ✔️
```json
[
    {
        "id": 5,
        "company_id": 3,
        "driver_id": 7,
        "origin": "Barcelona",
        "destination": "Madrid",
        "status": "completed"
    }
]
```

Posibles errores: ❌

* `404 Not Found` si la empresa no tiene envíos.
* `400 Bad Request` en caso de error interno.
---

### Obtener envíos asignados a un conductor
Devuelve los envíos asignados a un conductor.

Endpoint: GET /shipments/driver/{id}/

Parámetros de la URL:

`driver_id`: ID del conductor.

Ejemplo de respuesta (`200 OK`). ✔️
```json
[
    {
        "id": 6,
        "company_id": 1,
        "driver_id": 2,
        "origin": "Zaragoza",
        "destination": "Málaga",
        "status": "in_progress"
    }
]
```

Posibles errores: ❌

* `404 Not Found` si el conductor no tiene envíos asignados.
* `400 Bad Request` en caso de error interno.

---

### Actualizar un envío
Actualiza la información de un envío existente.

Endpoint: PUT /shipments/update/

Parámetros requeridos (JSON):
```json
{
    "id": 10,
    "status": "completed",
    "finished_at": "2025-03-11T20:00:00Z"
}
```

Ejemplo de respuesta (`200 OK`). ✔️
```json
{
    "id": 10,
    "company_id": 1,
    "driver_id": 2,
    "status": "completed",
    "created_at": "2025-03-10T12:00:00Z",
    "finished_at": "2025-03-11T20:00:00Z",
    "origin": "Ciudad A",
    "destination": "Ciudad B"
}
```

Posibles errores: `400 Bad Request` si los datos son inválidos o falta el ID del envío. ❌

---

### Obtener envíos sin conductor asignado
Devuelve los envíos que aún no tienen un conductor asignado.

Endpoint: GET /shipments/without-driver/

Ejemplo de respuesta (`200 ok`) ✔️
```json
[
    {
        "id": 3,
        "company_id": 4,
        "driver_id": null,
        "origin": "Valencia",
        "destination": "Madrid",
        "status": "pending"
    }
]
```
---

### Asignar un conductor a un envío
Permite a un conductor tomar un envío disponible.

Endpoint: POST /shipments/assign-driver/{shipment_id}/

Ejemplo de respuesta:
```json
{
    "message": "Driver assigned successfully"
}
```

### Actualizar un envío
Actualiza los detalles de un envío.

Endpoint: PUT /shipments/update/

Ejemplo de solicitud:
```json
{
    "id": 3,
    "status": "completed"
}
```

Ejemplo de respuesta:
```json
{
    "id": 3,
    "company_id": 4,
    "driver_id": 2,
    "origin": "Valencia",
    "destination": "Madrid",
    "status": "completed"
}
```
---

### Eliminar un envío
Elimina un envío si aún no tiene un conductor asignado.

Endpoint: DELETE /shipments/delete/{id}/

Ejemplo de respuesta (`200 OK`)
```json
{
    "message": "Shipment deleted"
}
```
Posibles errores: `400 Bad Request` si ocurre un error durante la eliminación. ❌

---

> [!NOTE]
> * Los datos se manejan a través del serializador ShipmentSerializer.
>   
> * Se implementan métodos HTTP estándar: POST (crear), GET (consultar), PUT (actualizar) y DELETE (eliminar).

---

## 🤝 Contribución  

¡Las contribuciones son bienvenidas! Para contribuir:  

1. Haz un fork del repositorio.
   
3. Crea una nueva rama:
    
   ```sh
   git checkout -b feature/nueva-funcionalidad
   ```
   
4. Realiza tus cambios y haz commit:
   
  ```sh
git commit -m "Añadir nueva funcionalidad"
```

4. Envía un pull request 🚀.
   
---
## 🚀 ¡Gracias por usar Track-Truck! Si tienes preguntas, crea un issue en el repositorio o contáctanos.
