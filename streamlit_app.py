import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(page_title="Análise de Recomendação de Telas", layout="wide")

# Título e Introdução
st.title("📊 Análise teste A/B - Recomendação de Telas")
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

#Hipotese 1
st.subheader("📋 Hipótese: Aumento do Engajamento dos Usuários")
st.markdown("""
Usuários que recebem recomendações personalizadas entre telas interagem mais com o aplicativo, aumentando o número de cliques em comparação com os que não recebem recomendações e em comparação à utilização nos meses anteriores.

Retorno do teste: Os usuários com acesso à recomendação realizaram 204% mais acessos medios mensais às funcionalidades sugeridas.
""")
# Gráfico de acessos às funcionalidades

fig2 = px.bar(
    df_acessos,
    x="Grupo",
    y="Acessos às Funcionalidades",
    text_auto=True,
    title="Média de Acessos mensal às Funcionalidades por Grupo (nov/dez)"
)
fig2.update_traces(textposition='outside')
st.plotly_chart(fig2, use_container_width=True)

#Hipotese 2
st.subheader("📋 Hipótese: Adesão às Recomendações ")
st.markdown("""
Usuários expostos ao algoritmo de recomendação aderem as recomendações na maior parte das vezes, de forma a não precisarem mudar sua rota de navegação para buscarem por outras telas de indicadores no aplicativo.
                      
Retorno do teste: No geral, o app sofreu uma queda no percentual de cliques entre outubro/novembro e dezembro/janeiro. No entanto, o grupo com recomendação apresentou uma taxa de cliques no menu inicial 5% menor que o grupo sem recomendação. 
            Além disto, tivemos 88% de adesão às recomendações por parte dos usuários.
""")


fig1 = go.Figure()
fig1.add_trace(go.Bar(
    name="Redução geral no Uso do App",
    x=df_uso["Grupo"],
    y=df_uso["Redução geral no Uso do App"],
    text=df_uso["Redução geral no Uso do App"].apply(lambda x: f"{x}%"),
))
fig1.add_trace(go.Bar(
    name="Redução nos Cliques do Menu inicial",
    x=df_uso["Grupo"],
    y=df_uso["Redução nos Cliques do Menu inicial"],
    text=df_uso["Redução nos Cliques do Menu inicial"].apply(lambda x: f"{x}%"),
))
fig1.update_layout(
    barmode='group',
    title="Comparativo de Reduções (Out-Nov vs Dez-Jan)",
    yaxis_title="Percentual de Redução (%)"
)
st.plotly_chart(fig1, use_container_width=True)

# Hipótese 3
st.subheader("📋 Hipótese: Descoberta de Novas Funcionalidades")
st.markdown("""
Os usuários descobrem e passam a utilizar funcionalidades que não acessavam anteriormente através das recomendações.

Retorno do teste: Observamos que usuários específicos começaram a acessar novas funcionalidades que não faziam parte de sua rotina após a implementação das recomendações.
""")

# Dados de descoberta de funcionalidades
dados_descoberta = {
    "Usuário": ["Rogério Paini", "Rogério Paini", "Luiz Franco", "Vlademir Barbosa"],
    "Funcionalidade": ["Rebanho", "Qualidade da Rotina", "Score de Fezes", "Itens Produtivos"],
    "Período": ["Antes", "Depois", "Antes", "Antes"],
    "Acessos": [0, 1, 0, 0]
}

df_descoberta = pd.DataFrame(dados_descoberta)

# Criar uma linha "Depois" para cada funcionalidade com valor 1
novas_linhas = []
for usuario in df_descoberta["Usuário"].unique():
    funcionalidades = df_descoberta[df_descoberta["Usuário"] == usuario]["Funcionalidade"].unique()
    for func in funcionalidades:
        novas_linhas.append({
            "Usuário": usuario,
            "Funcionalidade": func,
            "Período": "Depois",
            "Acessos": 1
        })

df_descoberta = pd.concat([df_descoberta, pd.DataFrame(novas_linhas)], ignore_index=True)

# Criar o gráfico de barras agrupadas
fig3 = px.bar(
    df_descoberta,
    x="Funcionalidade",
    y="Acessos",
    color="Período",
    barmode="group",
    title="Descoberta de Novas Funcionalidades por Usuário",
    text="Usuário",
    color_discrete_map={"Antes": "#E8E8E8", "Depois": "#2E86C1"}
)

fig3.update_traces(
    textposition='outside',
    textangle=0
)

fig3.update_layout(
    showlegend=True,
    xaxis_title="Funcionalidade",
    yaxis_title="Status de Acesso",
    yaxis=dict(
        tickmode='array',
        tickvals=[0, 1],
        ticktext=['Não Acessava', 'Passou a Acessar']
    )
)

st.plotly_chart(fig3, use_container_width=True)

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
- O grupo com recomendação apresentou uma taxa de cliques no menu inicial 5% menor que o grupo sem recomendação.
- Os usuários com acesso à recomendação realizaram 33% mais acessos medios mensais às funcionalidades sugeridas.
""")