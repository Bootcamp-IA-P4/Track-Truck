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

### 🔹 Autenticación
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
### 🔹 Gestión de Empresas
---
### Obtener todas las empresas
Endpoint: GET /api/empresas/

Ejemplo de respuesta:
```json
[
    {
        "id": 1,
        "nombre": "Empresa Logística S.A.",
        "direccion": "Madrid, España",
        "telefono": "+34 600 123 456"
    }
]
```
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
