# Proyecto de Automatización de Pruebas Web con Playwright

## Descripción

Este repositorio contiene un conjunto de pruebas automatizadas para el sitio web de Xtrim. Las pruebas están desarrolladas utilizando Python, Playwright y Pytest, siguiendo el patrón de diseño Page Object Model (POM). El objetivo principal es validar el correcto funcionamiento del formulario de contacto, incluyendo el envío con datos válidos, la validación de errores cuando se ingresan datos inválidos o vacíos, así como el manejo de modales y navegación dentro del sitio. A continuación, se detallan las instrucciones para ejecutar el proyecto en un entorno local.

El objetivo principal es validar:
- El envío correcto de formularios con datos válidos.
- Validaciones de errores con datos inválidos o vacíos.
- Manejo de modales y navegación dentro del sitio.

---

## Tecnologías utilizadas

- Python 3.x
- Playwright
- Pytest
- Faker (generación de datos dinámicos)

---

## 📋 Requisitos

Asegúrate de tener instalado:

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

---

## Instrucciones para Ejecutar el Proyecto

1. Clonar el repositorio:

- git clone https://github.com/mariajosesnchz/automatizacion-playwright-python.git
- cd automatizacion-playwright-python

2. Crear y activar entorno virtual:
- python -m venv venv
- venv\Scripts\activate   # Windows

3. Instalar dependencias:
- pip install -r requirements.txt

4. Instalar navegadores de Playwright:
- python -m playwright install

## Ejecución de pruebas
- pytest -s -v
## Reportes de ejecución
- Ejecuta el siguiente comando:
pytest --html=reports/report.html --self-contained-html
- El reporte se generará en la siguiente ruta:
 reports/report.html
## Estructura del Proyecto
- `pages/`
  - `home_page.py`: Acciones y validaciones de la página principal.
  - `contact_page.py`: Acciones y validaciones del formulario de contacto..
- `tests/`: Contiene los casos de prueba automatizados.
  - `home_page.py`: Pruebas relacionadas con el modal y navegación..
  - `test_contact_page.py`: Pruebas del formulario (válido, inválido, vacío, duplicado).
- `utils/`: Utilidades y configuración del proyecto.
  - `config.py`: Variables de entorno (BASE_URL, HEADLESS, TIMEOUT).
  - `data_reader.py`: Lectura de datos desde archivos (JSON u otros). 
  - `fake_data.py`: Generación de datos dinámicos con Faker.
- `conftest.py`: Configuración global de pytest (fixture del navegador, setup y teardown).
- `requirements.txt`: Lista de dependencias del proyecto.
- `README.md`: Documentación del proyecto e instrucciones de uso.
- `venv/`: Entorno virtual de Python (no se incluye en el repositorio).
- `reports/`: Reportes de ejecución de pruebas (ej. pytest-html).