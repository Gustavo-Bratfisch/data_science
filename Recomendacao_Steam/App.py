from flask import Flask, request, render_template
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

df2 = pd.read_csv('https://raw.githubusercontent.com/Gustavo-Bratfisch/data_science/master/Recomendacao_Steam/model/Final_Steam.csv')
Data_Steam = pd.read_csv('https://raw.githubusercontent.com/Gustavo-Bratfisch/data_science/master/Recomendacao_Steam/model/Final_Steam.csv')
Data_Steam = Data_Steam.rename(columns={'name': 'Nome_do_Jogo','release_date':'Data de Lançamento'})

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df2['overview'])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

df2 = df2.reset_index()
indices = pd.Series(df2.index, index=df2['name'])
all_titles = [df2['name'][i] for i in range(len(df2['name']))]

@app.route("/")
def hello():
    return render_template('inicio.html')

@app.route('/predict', methods = ['Get'])
def get_recommendations(title,cosine_sim = cosine_sim2):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
  
    return movie_indices

# handling form data
@app.route('/form-handler', methods=['POST'])
def handle_data():
    title2 = request.form['name']
    if title2 in Data_Steam.Nome_do_Jogo.values:
        predict = get_recommendations(title = title2)
        Final = Data_Steam.iloc[predict].sort_values("Scoring",ascending = False)[["Nome_do_Jogo","Data de Lançamento","Scoring","Url"]]
        return render_template('simple.html',  tables=[Final.to_html(classes='data')])
    else:
        return render_template('Erro.html')
    #predict = get_recommendations(title = title2)
    #Final = Data_Steam.iloc[predict].sort_values("Scoring",ascending = False)[["Nome do Jogo","Data de Lançamento","Scoring"]]
    #return render_template('simple.html',  tables=[Final.to_html(classes='data')])

@app.route('/return')
def retur():
    return render_template('inicio.html')
# Set up the main route
#@app.route('/predict', methods = ['GET'])
#def render_html():
#    return render_template('dropdown.html')

if __name__ == '__main__':
    app.run(debug = True)