import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(page_title="Análise de Recomendação de Telas", layout="wide")

# Título e Introdução
st.title("📊 Análise de Impacto - Recomendação de Telas")
st.markdown("""
    Análise comparativa entre dois grupos de controle com 12 usuários cada, avaliando o impacto 
    da implementação da funcionalidade de recomendação de telas.
""")

# KPIs principais
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        "Taxa de adesão (usuários)",
        "88%",
        "7 de 8 usuários ativos utilizaram"
    )
with col2:
    st.metric(
        "Diferença na Redução de Cliques no menu inicial",
        "5%",
        "menos cliques em menu inicial no grupo com recomendação"
    )
with col3:
    st.metric(
        "Diferença nos Acessos",
        "33%",
        "mais acessos no grupo com recomendação"
    )

# Dados de uso do app
dados_uso = {
    "Grupo": ["Com Recomendação", "Sem Recomendação"],
    "Redução geral no Uso do App": [-43, -42],
    "Redução nos Cliques do Menu inicial": [-48, -43]
}
df_uso = pd.DataFrame(dados_uso)

# Dados de acessos às funcionalidades
dados_acessos = {
    "Grupo": ["Com Recomendação", "Sem Recomendação"],
    "Acessos às Funcionalidades": [295, 97]
}
df_acessos = pd.DataFrame(dados_acessos)

# Visualizações
st.subheader("📉 Comparativo de Reduções")
fig1 = go.Figure()
fig1.add_trace(go.Bar(
    name="Redução no Uso do App",
    x=df_uso["Grupo"],
    y=df_uso["Redução no Uso do App"],
    text=df_uso["Redução no Uso do App"].apply(lambda x: f"{x}%"),
))
fig1.add_trace(go.Bar(
    name="Redução nos Cliques do Menu",
    x=df_uso["Grupo"],
    y=df_uso["Redução nos Cliques do Menu"],
    text=df_uso["Redução nos Cliques do Menu"].apply(lambda x: f"{x}%"),
))
fig1.update_layout(
    barmode='group',
    title="Comparativo de Reduções (Out-Nov vs Dez-Jan)",
    yaxis_title="Percentual de Redução (%)"
)
st.plotly_chart(fig1, use_container_width=True)

# Gráfico de acessos às funcionalidades
st.subheader("📈 Acessos às Funcionalidades Sugeridas")
fig2 = px.bar(
    df_acessos,
    x="Grupo",
    y="Acessos às Funcionalidades",
    text_auto=True,
    title="Média de Acessos mensal às Funcionalidades por Grupo (nov/dez)"
)
fig2.update_traces(textposition='outside')
st.plotly_chart(fig2, use_container_width=True)

# Detalhamento dos grupos
st.subheader("🔍 Detalhamento dos Grupos")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Grupo Com Recomendação:**
    - 12 usuários totais
    - 8 usuários ativos no período
    - 7 utilizaram a recomendação
    - Redução de 43% no uso geral
    - Redução de 48% nos cliques no menu inicial
    - 295 acessos médios às funcionalidades
    """)

with col2:
    st.markdown("""
    **Grupo Sem Recomendação:**
    - 12 usuários totais
    - Redução de 42% no uso geral
    - Redução de 43% nos cliques no menu inicial
    - 97 acessos médios às funcionalidades
    """)

# Conclusões principais
st.subheader("📋 Principais Conclusões")
st.markdown("""
- A funcionalidade de recomendação teve uma alta taxa de adoção (88% dos usuários ativos).
- Ambos os grupos apresentaram redução similar no uso geral do app (42-43%).
- O grupo com recomendação apresentou uma redução 5% menor nos cliques do menu inicial.
- Os usuários com acesso à recomendação realizaram 33% mais acessos medios mensais às funcionalidades sugeridas.
""")