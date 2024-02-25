import streamlit as st
import pandas as pd
import altair as alt
import folium
from streamlit_folium import folium_static

def formatar_valor_monetario(valor):
    """
    Função para formatar o valor em formato monetário.
    """
    return "R$ {:,.2f}".format(valor)

def main():
    # Título do aplicativo
    st.title('Unidade')

    # Dados
    data = {
        "Cidade": ["Recife", "São Loureço da Mata", "Gloria do Goita"],
        "Unidades": [50, 40, 45],
        "Usuario": [1000, 888, 414],
        "Funcionário": [600, 400, 100],
        "Valor Gasto": [1002000,200000,456000],
        "Latitude": [-8.05428, -8.004016, -8.0017459],
        "Longitude": [-34.8813, -35.1240409, -35.3140097]
    }

    df = pd.DataFrame(data)

    # Seletor para selecionar o município
    cidade_selecionada = st.selectbox("Selecione o município:", ["Todos"] + df["Cidade"].tolist())

    # Exibir métricas para o município selecionado ou para todos os municípios
    if cidade_selecionada == "Todos":
        col1, col2, col3 = st.columns(3)
        col1.metric("Total de Unidades", df["Unidades"].sum())
        col2.metric("Total de Usuário", df["Usuario"].sum())
        col3.metric("Total de Funcionário", df["Funcionário"].sum())
        # col4.metric("Total do Valor Gasto", formatar_valor_monetario(df["Valor Gasto"].sum()))
        # Define cidade_df como o DataFrame completo
        cidade_df = df
    else:
        # Filtrar o DataFrame com base na cidade selecionada
        cidade_df = df[df["Cidade"] == cidade_selecionada]

        # Exibir métricas para a cidade selecionada
        col1, col2, col3 = st.columns(3)
        col1.metric("Unidades", cidade_df["Unidades"].iloc[0])
        col2.metric("Usuário", cidade_df["Usuario"].iloc[0])
        col3.metric("Funcionário", cidade_df["Funcionário"].iloc[0])
        # col4.metric("Total do Valor Gasto", formatar_valor_monetario(cidade_df["Valor Gasto"].iloc[0]))

    # Crie o mapa Folium
    mapa = folium.Map(location=[-8.0517459, -35.094281], zoom_start=8)

    # Adicione um marcador para o município selecionado (se houver apenas um)
    if cidade_selecionada == "Todos":
        for i in range(df.shape[0]):
            cidade = df.loc[i, "Cidade"]
            unidades = df.loc[i, "Unidades"]
            folium.Marker([df.loc[i, "Latitude"], df.loc[i, "Longitude"]], 
                        popup=f"{cidade}: {unidades} unidades").add_to(mapa)
    else:
        if not cidade_df.empty:
            cidade = cidade_df.iloc[0]["Cidade"]
            unidades = cidade_df.iloc[0]["Unidades"]
            folium.Marker([cidade_df.iloc[0]["Latitude"], cidade_df.iloc[0]["Longitude"]], 
                        popup=f"{cidade}: {unidades} unidades").add_to(mapa)

    # Exibir o mapa
    folium_static(mapa, width=700, height=280)

    # Criar o gráfico de colunas com o valor gasto por município
    chart_data = cidade_df[["Cidade", "Valor Gasto"]]
    st.subheader("Valor Gasto por Município")
    chart = alt.Chart(chart_data).mark_bar().encode(
        x='Cidade',
        y='Valor Gasto',
        color=alt.Color('Cidade', legend=None)
    ).properties(
        width=600,
        height=400
    )
    st.altair_chart(chart, use_container_width=True)

if __name__ == '__main__':
    main()
