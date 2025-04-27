import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Dashboard COVID-19",
    page_icon="🦠",
    layout="wide"
)

# Título del dashboard
st.title("🌍 Análisis Global de COVID-19")
st.markdown("Datos actualizados de la pandemia (Fuente: Our World in Data)")

# Cargar datos desde GitHub (cache para mejor rendimiento)
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
    df = pd.read_csv(url)
    df['date'] = pd.to_datetime(df['date'])  # Convertir fecha a formato datetime
    return df

df = load_data()

# --- FILTROS EN EL SIDEBAR ---
st.sidebar.header("🔍 Filtros")

# 1. Selector de país
paises = df['location'].unique()
pais_seleccionado = st.sidebar.selectbox(
    "Selecciona un país:",
    paises,
    index=0  # Por defecto muestra el primer país (Afghanistan)
)

# 2. Rango de fechas
fecha_min = df['date'].min()
fecha_max = df['date'].max()
rango_fechas = st.sidebar.date_input(
    "Selecciona un rango de fechas:",
    [fecha_min, fecha_max],
    min_value=fecha_min,
    max_value=fecha_max
)

# --- DATOS FILTRADOS ---
df_filtrado = df[
    (df['location'] == pais_seleccionado) &
    (df['date'] >= pd.to_datetime(rango_fechas[0])) &
    (df['date'] <= pd.to_datetime(rango_fechas[1]))
]

# --- KPI PRINCIPALES ---
st.header(f"📊 Estadísticas para {pais_seleccionado}")
col1, col2, col3 = st.columns(3)
with col1:
    total_casos = int(df_filtrado['total_cases'].max())
    st.metric("Total de casos", f"{total_casos:,}")
with col2:
    total_muertes = int(df_filtrado['total_deaths'].max())
    st.metric("Total de muertes", f"{total_muertes:,}")
with col3:
    tasa_mortalidad = (total_muertes / total_casos * 100) if total_casos > 0 else 0
    st.metric("Tasa de mortalidad", f"{tasa_mortalidad:.2f}%")

# --- GRÁFICOS ---
st.header("📈 Evolución Temporal")

# 1. Gráfico de nuevos casos
fig_nuevos_casos = px.line(
    df_filtrado,
    x="date",
    y="new_cases",
    title="Nuevos casos por día",
    labels={"date": "Fecha", "new_cases": "Nuevos casos"}
)
st.plotly_chart(fig_nuevos_casos, use_container_width=True)

# 2. Gráfico acumulado (casos vs muertes)
fig_acumulado = px.line(
    df_filtrado,
    x="date",
    y=["total_cases", "total_deaths"],
    title="Casos y muertes acumuladas",
    labels={"value": "Cantidad", "variable": "Métrica"}
)
st.plotly_chart(fig_acumulado, use_container_width=True)

# --- MAPA INTERACTIVO ---
st.header("🗺️ Mapa Global de Casos")
df_ultima_fecha = df[df['date'] == df['date'].max()]  # Datos más recientes
fig_mapa = px.choropleth(
    df_ultima_fecha,
    locations="iso_code",
    color="total_cases",
    hover_name="location",
    projection="natural earth",
    title="Casos totales por país",
    color_continuous_scale=px.colors.sequential.Plasma
)
st.plotly_chart(fig_mapa, use_container_width=True)