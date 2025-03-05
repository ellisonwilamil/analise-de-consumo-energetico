#main.py
import streamlit as st
import modules.data_loader as dl
import modules.analysis as an
import modules.visualization as vz
import modules.text_content as txt

st.set_page_config(layout="wide", page_title="Análise de Consumo Energético")

st.sidebar.title("Menu de Análises")
opcao = st.sidebar.selectbox("Escolha uma análise:", ["Visão Geral", "Métricas", "Modelos de Previsão"])

st.title("Análise de Consumo Energético")
st.markdown(txt.introducao)

df = dl.carregar_dados()

if opcao == "Visão Geral":
    st.markdown(txt.visao_geral)
    st.dataframe(df.head())

elif opcao == "Métricas":
    st.markdown(txt.metricas)
    vz.plot_consumo(df)

elif opcao == "Modelos de Previsão":
    st.markdown(txt.modelos)
    previsao = an.random_forest(df)
    st.write("Previsão feita pelo modelo:", previsao)
