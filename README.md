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
