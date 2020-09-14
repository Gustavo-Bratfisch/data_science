from flask import Flask, request, render_template
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import sigmoid_kernel
from sklearn.metrics.pairwise import linear_kernel
import pickle

app = Flask(__name__)

#df2 = pd.read_csv('https://raw.githubusercontent.com/Gustavo-Bratfisch/data_science/master/Recomendacao_Steam/Final_Steam.csv')
Data_Steam = pd.read_csv('https://raw.githubusercontent.com/Gustavo-Bratfisch/data_science/master/Recomendacao_Steam/Final_Steam.csv')
#Data_Steam = Data_Steam.rename(columns={'name': 'Nome_do_Jogo','release_date':'Data de Lançamento'})


tfidf_vect_pkl = pickle.load(open('tfidf_vectorizer.pickle', 'rb'))


@app.route("/")
def hello():
    return render_template('inicio.html')

@app.route('/predict', methods = ['Get'])
def recomendation(title,df = Data_Steam,tfidf_vect = tfidf_vect_pkl):
    title_iloc = df.index[df['name'] == title][0]
    
    show_cos_sim = cosine_similarity(tfidf_vect[title_iloc], tfidf_vect).flatten()
    
    sim_titles_vects = sorted(list(enumerate(show_cos_sim)), key=lambda x: x[1], reverse=True)[1:10]
    
    #response = '\n'.join([f'{df.iloc[t_vect[0]][2]} --> confidence: {round(t_vect[1],1)}' for t_vect in sim_titles_vects])
    Nome = []
    Lanca =[]
    Aval = []
    Aproxi =[]
    Url = []
    for sins in sim_titles_vects:
        Nome.append(df.iloc[sins[0]][1])
        Lanca.append(df.iloc[sins[0]][2])
        Aval.append(round(df.iloc[sins[0]]['Scoring'],2))
        Aproxi.append(round(sins[1],2))
        Url.append(df.iloc[sins[0]]['Url'])
    
    Dict_final = {'Nome':Nome,'Data_Lancamento':Lanca,'Avaliacao':Aval,'Aproximacao':Aproxi,'Url':Url}
    Data_Final = pd.DataFrame(Dict_final)
    return Data_Final


# handling form data
@app.route('/form-handler', methods=['POST'])
def handle_data():
    title2 = request.form['name']
    if title2 in Data_Steam['name'].values:
        predictions = recomendation(title = title2)
        #links = Final['Url']
        #return render_template('simple.html',  tables=[Final.to_html(classes='data')],predictions = links)
        return render_template('simple.html',  predictions = [predictions.to_html(classes='data')] )
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