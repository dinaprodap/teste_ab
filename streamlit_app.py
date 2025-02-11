import streamlit as st
import pandas as pd
import plotly.express as px

# Simulação de Dados
data = {
    "Grupo": ["Com Recomendação", "Sem Recomendação"],
    "Redução Uso (%)": [-43, -42],
    "Redução Cliques (%)": [-48, -43],
    "Acessos Funcionalidades": [295, 97],
}

df = pd.DataFrame(data)

# Layout do Painel
st.title("📊 Painel de BI - Comparação de Uso")

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Usuários com Recomendação", "12")
col2.metric("Usuários que Utilizaram", "7")
col3.metric("Redução de Uso (%)", "-43%")
col4.metric("Acessos Funcionalidades (Recom.)", "295")

# Gráfico de Barras - Redução de Uso
fig1 = px.bar(df, x="Grupo", y=["Redução Uso (%)", "Redução Cliques (%)"], 
              barmode="group", title="Redução no Uso e Cliques")
st.plotly_chart(fig1)

# Gráfico de Acessos
fig2 = px.bar(df, x="Grupo", y="Acessos Funcionalidades", 
              title="Acessos às Funcionalidades", text_auto=True)
st.plotly_chart(fig2)

# Tabela de Comparação
st.subheader("📋 Resumo Comparativo")
st.dataframe(df)