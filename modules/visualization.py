 # Funções para gráficos (Plotly, Matplotlib, etc.)
import plotly.graph_objects as go
import streamlit as st

def plot_consumo(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df.p3, name='Potência Trifásica', line=dict(width=3)))
    fig.update_layout(
    title="Consumo IFSC/Florianópolis", xaxis_title="Data", 
    yaxis_title="Consumo (kW)", template="plotly_white")
    st.plotly_chart(fig)

    