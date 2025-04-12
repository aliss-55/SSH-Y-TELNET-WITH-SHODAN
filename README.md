# 🔐 Auditoría de Credenciales SSH/Telnet con Shodan API

Este proyecto permite realizar una auditoría automatizada de dispositivos en Latinoamérica que tengan expuestos servicios SSH (puerto 22) y Telnet (puerto 23), utilizando la API de Shodan y validando credenciales con listas configurables.

> ⚠️ **Uso exclusivo con fines académicos y éticos. No ejecutar sobre redes o dispositivos sin autorización expresa.**

---

## 🎯 Objetivos

- Utilizar la API de Shodan para descubrir servicios expuestos.
- Probar credenciales por SSH (usando `paramiko`) y Telnet (usando `telnetlib`).
- Automatizar el proceso de validación con Python.
- Generar logs y reportes de accesos exitosos.
- Gestionar errores comunes y uso responsable de la API.

### 📦 Dependencias

Instala las librerías necesarias con:

```bash
pip install shodan paramiko

## 🧪 Ejecución Paso a Paso

### 🔧 Paso 1: Preparar el entorno

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/proyecto-auditoria.git
   cd proyecto-auditoria
   ```

2. Instala las dependencias:
   ```bash
   pip install shodan paramiko
   ```

---

### 🗝️ Paso 2: Obtener tu API Key de Shodan

1. Ve a [shodan.io](https://www.shodan.io/)
2. Crea una cuenta gratuita o inicia sesión.
3. Copia tu API Key desde el perfil.
4. Pégala cuando el script la solicite.

---

### 📁 Paso 3: Configurar credenciales

Edita los archivos dentro de `credentials/`:

**users.txt**
```
admin
root
user
```

**passwords.txt**
```
1234
admin
toor
```

---

### ▶️ Paso 4: Ejecutar el script

```bash
python main.py
```

- Ingresa tu API Key.
- Selecciona el país de Latinoamérica desde el menú.
- El sistema buscará IPs expuestas y validará automáticamente por **SSH y Telnet**.

---
