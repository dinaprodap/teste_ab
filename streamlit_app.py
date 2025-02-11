import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(page_title="Análise de Recomendação de Telas", layout="wide")

# Título e Introdução
st.title("📊 Análise teste A/B - Recomendação de Telas")
st.markdown("""
    <p Obetivo geral do teste:</p> Melhorar a usabilidade e aumentar o engajamento dos usuários do LORE
""")


st.write("Para este teste, foram selecionados aleatoriamente 24 usuários do tipo cliente que realizaram ao menos um clique na LORE em funcionalidades de pasto, entre 09/09/24 e 09/10/24.")

st.write("O grupo 1, formado por 12 desses usuários, recebeu a funcionalidade de recomendação de telas.")

st.write("Já o grupo 2, com as mesmas características e também definido aleatoriamente, continuou utilizando o app sem essa recomendação, servindo como grupo de comparação.")


# KPIs principais
st.subheader("KPIs principais")

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
Através da funcionalidade de recomendação de telas, observamos mudanças significativas no comportamento dos usuários. Rogério Paini, que anteriormente não costumava acessar as funcionalidades de rebanho e qualidade da rotina, incorporou essas análises em sua rotina de uso. De forma similar, Luiz Franco descobriu o score de fezes, uma funcionalidade que não acessava antes. Já Vlademir Barbosa expandiu seu uso do sistema ao começar a acessar o menu de itens produtivos, demonstrando como as recomendações podem incentivar a exploração de novas funcionalidades.
            """)

# Criando um layout estilizado para mostrar as descobertas
st.markdown("""
<style>
.descoberta-box {
    background-color: #f8f9fa;
    border-radius: 10px;
    padding: 20px;
    margin: 10px 0;
}
.usuario-nome {
    color: #2E86C1;
    font-weight: bold;
    font-size: 1.1em;
}
.funcionalidades {
    margin-left: 20px;
    color: #555;
}
</style>

<div class="descoberta-box">
    <div class="usuario-nome">👤 Rogério Paini</div>
    <div class="funcionalidades">
        ➜ Rebanho<br>
        ➜ Qualidade da Rotina
    </div>
</div>

<div class="descoberta-box">
    <div class="usuario-nome">👤 Luiz Franco</div>
    <div class="funcionalidades">
        ➜ Score de Fezes
    </div>
</div>

<div class="descoberta-box">
    <div class="usuario-nome">👤 Vlademir Barbosa</div>
    <div class="funcionalidades">
        ➜ Itens Produtivos
    </div>
</div>
""", unsafe_allow_html=True)

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