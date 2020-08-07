import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import sigmoid_kernel
from sklearn.metrics.pairwise import linear_kernel
import zarr

#O cache é utilizado quando é feito o rerun do programa (quando colocamos outro nome de jogo) para que essas funções não necessitam rodar
#novamente
@st.cache
def load_data(file_uploaded):
    return (pd.read_csv(file_uploaded))

@st.cache
def load_zarr(file_uploaded):
    return (zarr.load(file_uploaded))

df2 = load_data('https://raw.githubusercontent.com/Gustavo-Bratfisch/data_science/master/Recomendacao_Steam/Final_Steam.csv')
df2 = df2.drop(["Unnamed: 0"],axis = 1)
Data_Steam = load_data('https://raw.githubusercontent.com/Gustavo-Bratfisch/data_science/master/Recomendacao_Steam/Final_Steam.csv')
Data_Steam = Data_Steam.rename(columns={'name': 'Nome_do_Jogo','release_date':'Data de Lançamento'})

#Rodei anteriomente e salvei em um arquivo zarr, que tem o processamento mais veloz de que outras maneiras
#Nessse arquivos temos a matrix de associações dos jogos (quais são mais proximos)
sig_kern = load_zarr("C:/DataZero/sig_kern.zarr")

df2 = df2.reset_index()
indices = pd.Series(df2.index, index=df2['name'])

#criando a função que vai pegar os indices do 10 jogos mais parecidos
def get_recommendations(title,cosine_sim = sig_kern):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    jogos_indices = [i[0] for i in sim_scores]
    return jogos_indices


#Layout para aparecer no site
st.latex('\LARGE \mathbf {Entre \space com \space o \space nome \space do \space Jogo}')
st.latex('\scriptsize \mathbf {O \space nome \space precisa \space estar \space o \space mesmo \space da \space Steam}')
title2 = st.text_input('')

start = st.button("Start")

if start:
    if title2 in Data_Steam.Nome_do_Jogo.values:
        predict = get_recommendations(title = title2)
        Final = Data_Steam.iloc[predict].sort_values("Scoring",ascending = False)[["Nome_do_Jogo","Data de Lançamento","Scoring","Url"]]
        st.table(Final)
    else:
        st.latex('\color{red} \LARGE \mathbf {O \space jogo \space não \space está \space em \space nosso \space conjunto \space de \space Dados}')

