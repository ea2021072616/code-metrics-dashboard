## COVID-19 Interactive Dashboard with Streamlit

This project is an interactive dashboard developed in **Python** using **Streamlit** and **Plotly**, with data pulled directly from the Our World in Data GitHub repository. It allows you to visualize global COVID-19 cases, deaths, and trends in real time.

## What is Streamlit?

Streamlit is an open-source Python library that makes it easy to build and share beautiful custom web applications for data science and machine learning. Unlike Dash, it requires no front-end programming knowledge (HTML/CSS/JS).

## Prerequisites

- Python 3.8+
- Stable internet connection (for real-time data)
- Web browser (Chrome/Firefox recommended)

## Installation and Run Instructions

### 1. Clone the repository

-git clone https://github.com/your_username/covid-dashboard.git

-cd covid-dashboard

### 2. Create a virtual environment (recommended)

-python -m venv venv

-source venv/bin/activate # On Mac/Linux

-venv\Scripts\activate # On Windows

### 3. Install Dependencies

Create a requirements.txt file with the following contents:
-streamlit
-pandas
-plotly
Install all dependencies by running:
pip install -r requirements.txt

### 4. Run the application

streamlit run app.py

### 5. Access the dashboard

The application will automatically open in your default browser at the following URL:

http://localhost:8501

### Key Features

-Interactive filters: Select countries and date ranges.

-Real-time data: Automatically retrieve the latest COVID-19 statistics.

-Visualizations:

    -Time series charts of cases and deaths.

    -Global choropleth map.

    -Dashboard with key metrics.

-Responsive design: Works on desktop and mobile devices.
