# 📌 Playwright - Proyecto de Automatización de Pruebas


## 🔧 Instalación de Herramientas


### 1️⃣ Instalar Python (si no está instalado)
Descargar e instalar Python desde [python.org](https://www.python.org/downloads/).
Asegúrate de agregar Python al `PATH` durante la instalación.

### 2️⃣ Crear un entorno virtual (opcional pero recomendado)

python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate    # En Windows


### 3️⃣ Instalar Playwright y dependencias

pip install pytest playwright
playwright install

# navegador
playwright install chromium

# extensión pytest
pip install pytest-playwright



---

## 📂 Estructura del Proyecto

```bash
.
├── tests/
│   ├── test_cpl_localizador.py  # Archivo con los casos de prueba
│   ├── helpers.py  # Funciones auxiliares
│   ├── login.py  # Función de login
│   └── config.py  # Configuración de variables
├── reports/
│   ├── test_report.html  # Reporte de ejecución
│   ├── screenshots/  # Carpeta para capturas de pantalla
│   └── videos/  # Carpeta para grabaciones
├── database/
│   └── test_results.db  # Base de datos SQLite para guardar resultados
├── README.md
└── requirements.txt  # Dependencias del proyecto
```

---

## ⚙️ Configuración de Playwright

Si deseas configurar navegadores específicos o personalizar la ejecución, puedes modificar el archivo `config.py`:

```python
# config.py
DNI_BUSQUEDA = "12345678"
DENOMINACION_BUSQUEDA = "Empresa XYZ"
```

---

## ▶️ Ejecución de Pruebas

### 1️⃣ Ejecutar un caso con Chromium (headed + slowmo)

pytest --slowmo 500 --headed tests/test_cpl_localizador.py::test_limpiar_campos


### 2️⃣ Ejecutar un caso sin Chromium (headless)

pytest tests/test_cpl_localizador.py::test_filtro_tipo

---

## 📸 Captura de Imágenes y Videos

### 1️⃣ Tomar capturas de pantalla

pytest --slowmo 500 --headed tests/test_cpl_localizador.py::test_buscar_por_dni

Las imágenes se guardarán en `reports/screenshots/`.

### 2️⃣ Grabar video de la ejecución

pytest tests/test_cpl_localizador.py::test_limpiar_campos2

Los videos se guardarán en `reports/videos/`.

---

## 🗄️ Guardar Resultados en la Base de Datos

### 1️⃣ Ejecutar test con registro en BD

pytest tests/test_cpl_localizador.py::test_filtro_tipo


---

## 📊 Generación de Reportes

### 1️⃣ Generar un reporte HTML
```sh
pytest --html=reports/test_report.html --self-contained-html
```

### 2️⃣ Abrir el reporte
```sh
start reports\test_report.html  # En Windows
xdg-open reports/test_report.html  # En Linux
```



