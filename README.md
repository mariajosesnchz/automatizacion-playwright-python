# Automatización de Pruebas con Playwright y Python

Este proyecto automatiza la prueba del formulario de contacto y modales en la web de ejemplo "https://www.xtrim.com.ec/", usando **Playwright** y **Python** con una estructura de Page Object Model (POM).

## Tecnologías utilizadas
- Python 3.11+
- Playwright
- Pytest
- Faker (para datos aleatorios)
- Docker (opcional)
- Git / GitHub

## Estructura del proyecto
project/
├── pages/
│ ├── base_page.py
│ ├── home_page.py
│ └── contact_page.py
├── tests/
│ ├── test_home.py
│ └── test_contact.py
├── utils/
│ ├── config.py
│ ├── data_reader.py
│ └── fake_data.py
├── requirements.txt
├── README.md
└── docker-compose.yml