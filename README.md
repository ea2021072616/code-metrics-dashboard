# COVID-19 Interactive Dashboard with Streamlit

Este proyecto es un dashboard interactivo desarrollado en **Python** utilizando **Streamlit** y **Plotly**, con datos obtenidos directamente desde el repositorio de GitHub de Our World in Data. Permite visualizar los casos globales de COVID-19, las muertes y las tendencias en tiempo real.

## ¿Qué es Streamlit?

Streamlit es una biblioteca de Python de código abierto que facilita la creación y compartición de hermosas aplicaciones web personalizadas para ciencia de datos y aprendizaje automático. A diferencia de Dash, no requiere conocimientos de programación frontend (HTML/CSS/JS).

## Requisitos previos

- Python 3.8+
- Conexión a internet estable (para obtener datos en tiempo real)
- Navegador web (recomendado Chrome/Firefox)

## Instrucciones de instalación y ejecución

### 1. Clona el repositorio

-git clone https://github.com/your_username/covid-dashboard.git
-cd covid-dashboard

### 2. Crea un entorno virtual (recomendado)
-python -m venv venv
-source venv/bin/activate    # En Mac/Linux
-venv\Scripts\activate       # En Windows

### 3. Instala las dependencias

Crea un archivo requirements.txt con el siguiente contenido:
    -streamlit
    -pandas
    -plotly
Instala todas las dependencias ejecutando:
pip install -r requirements.txt

### 4. Ejecuta la aplicación

streamlit run app.py

### 5. Accede al dashboard

La aplicación se abrirá automáticamente en tu navegador predeterminado en la siguiente URL:

http://localhost:8501

### Características clave

-Filtros interactivos: Selecciona países y rangos de fechas.

-Datos en tiempo real: Obtiene automáticamente las estadísticas más recientes de COVID-19.

-Visualizaciones:

    -Gráficos de series temporales de casos y muertes.

    -Mapa global choropleth.

    -Dashboard con métricas clave.

-Diseño responsivo: Funciona en dispositivos de escritorio y móviles.