import streamlit as st
import pandas as pd
import plotly.express as px

# Simulação de Dados
data = {
    "Grupo": ["Com Recomendação", "Sem Recomendação"],
    "Redução geral uso do app (%)": [-43, -42],
    "Redução Cliques no menu inicial (%)": [-48, -43],
    "Clique médio nas funcionalidades": [295, 97],
}

df = pd.DataFrame(data)

# Layout do Painel
st.title("📊 Teste A/B - recomendação de telas")

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Usuários com Recomendação", "12")
col2.metric("Usuários que utilizaram o APP", "8")
col3.metric("Usuários que utilizaram a recomendação", "7")
col4.metric("Redução de Uso geral no app (%)", "-43%")

# Gráfico de Barras - Redução de Uso
fig1 = px.bar(df, x="Grupo", y=["Redução geral uso do app (%)", "Redução Cliques no menu inicial (%)"], 
              barmode="group", title="Redução no Uso e Cliques")
st.plotly_chart(fig1)

# Gráfico de Acessos
fig2 = px.bar(df, x="Grupo", y="Clique médio nas funcionalidades", 
              title="Acessos às Funcionalidades", text_auto=True)
st.plotly_chart(fig2)

# Tabela de Comparação
st.subheader("📋 Resumo Comparativo")
st.dataframe(df)