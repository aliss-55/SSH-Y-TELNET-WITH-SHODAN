# 📋 INFORME DE ENTREGA - Auditoría SSH/Telnet con Shodan API

## 📌 Nombre del Estudiante:
**Alisson Tobar Ariza**

## 🎯 Asignatura:
Seguridad en Redes - Marzo 2025

## 👨‍🏫 Docente:
Andrés Felipe Gonzalez Coronado

---

## ✅ RÚBRICA DE EVALUACIÓN

| Criterio                            | Evidencia | Ponderación |
|------------------------------------|-----------|-------------|
| **Funcionalidad Básica**           | El script realiza búsqueda con Shodan API y valida servicios SSH y Telnet. IPs, usuarios y contraseñas se prueban desde listas externas. | 25% |
| **Funciones Avanzadas**            | Se implementó automatización masiva, logs de credenciales válidas (`valid_credentials.log`), manejo de errores y un resumen final (`resumen_final.log`). | 25% |
| **Código y Estructura**            | Código modular dividido en `main.py`, `utils/` y `validators/`. Incluye comentarios, buen manejo de errores y separación de funciones. | 15% |
| **Documentación (README)**         | Archivo `README.md` completo con instrucciones, ejemplos y estructura del proyecto. | 10% |
| **Manejo Ético y Responsable**     | Incluye advertencia clara en el `README.md` y en el encabezado de `main.py`. | 5% |
| **Claridad de Presentación**       | El proyecto incluye consola interactiva, salidas legibles y reportes automáticos. | 10% |
| **Uso de Herramientas de IA**      | Ver sección de prompts abajo. | 10% |

---

## ⚖️ Consideraciones Éticas y Legales

Esta herramienta se ha desarrollado exclusivamente con fines **educativos y éticos**. Se enfatiza que:

- **No se debe ejecutar en redes sin autorización.**
- Cualquier uso malicioso queda completamente bajo la responsabilidad del usuario.

---

## 🧠 Prompts Usados para Asistencia con IA

Se utilizó ChatGPT como asistente para guiar el desarrollo del proyecto. Los prompts más relevantes fueron:

"Explícame paso a paso cómo desarrollar una aplicación en Python para validar SSH y Telnet con Shodan."

"Hazme un script que genere un resumen final."

"Ayúdame a mejorar el README.md para entregarlo en GitHub."

"Explícame cómo cumplir con esta rúbrica punto por punto."

---

## 📈 Alcance y Limitaciones Técnicas

- Se implementó validación de puertos 22 y 23 (SSH y Telnet).
- Las IPs se obtienen dinámicamente desde la API de Shodan.
- Se requiere una conexión estable a internet y una API Key activa con créditos suficientes.
- Puede haber demoras o bloqueos si los servidores tienen firewalls, timeout o credenciales no válidas.

---

## 📌 Entregables Incluidos

- Código fuente (`main.py`, módulos, credenciales)
- Documentación (`README.md`)
- Logs generados automáticamente
- Este informe (`INFORME_DE_ENTREGA.md`)

---

## ✨ Recomendaciones Finales

Se recomienda probar en entornos controlados y manejar con responsabilidad los resultados obtenidos. Esta herramienta puede extenderse para incluir otros servicios inseguros o funcionalidades como escaneo de banners o gráficos de acceso.





