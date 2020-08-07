# Recomendação de Jogos na Steam

Nesse projeto iremos fazer uma análise exploratorio dos dados mostrando um pouco mais sobre os dados e 
depois utilizaremos Flask para criar uma aplicação local para recomendação de jogos na steam (jogos com lançamento até maio de 2019).

## Inicio

Podemos dividir esse trabalho em duas partes.

### - Primeira Parte: Visualização dos dados: **https://bit.ly/31r7Gkv**

Nessa parte tentamos entender um pouco mais de como os dados estão distribuidos, fizemos alguns agrupamentos para ver quais são os generos majoritarios(grafico abaixo) e o tipo de jogo
![genre_game](https://user-images.githubusercontent.com/11478711/89574241-35100d00-d802-11ea-84d4-8226507566c1.png)

Criamos uma medida de avaliação baseada nas taxas de avaliações positivas e negativas dos jogos e fazendo um simples agrupamento conseguimos notar alguns pontos interessant e 
plotando conseguimos notar que jogos MM são que tem o maior feedback tanto positivo quanto negativo e nos restante seguem o mesmo padrão

![ratin_gem](https://user-images.githubusercontent.com/11478711/89574165-1447b780-d802-11ea-950b-6246a6c4b9a3.png)


### - Segunda Parte: Visualização dos dados: **https://bit.ly/2EXESZj**


Nessa segunda parte criamos nosso modelo utilziando a metodologia de recomendação baseada em conteúdo onde passamos descrições dos jogos, o modelo computa TF-IDF (Term Frequency-Inverse Document Frequency) 
que calcula uma matrix onde na coluna representa a uma avaliação da frequencia da palavra aparecer. Com essa matrix utilizamos uma metrica de similaridade (no nosso caso foi sigmoid_kernel) e por fim ordenamos pelo score feito anteriormente para ver os 10 jogos mais semelhantes. 

Para finalizar cronstruímos um local web usando StreamLit (https://www.streamlit.io/https://www.streamlit.io/), o streamlit é super intuitivo, com muitas opções para se trabalhar, porém antes de construi em StreamLit eu tinha feito em Flask que também não é complicado, o Flask trabalha mais com a parte de Html.

Porém como estou trabalhando com um modelo grande, o arquivo com a matrix de dependencia é de 5Gb não foi possivel colcoar em um servidor de forma gratuita, pelo menos no Google Cloud e no Heroku não foi possivel.

Fotos do website pronto localmente.

Nessa foto temos o caso que o Jogo pertence ao nosso conjunto de dados e o resultado dos 10 jogos mais parecidos com as tag da steam.
![stream_1](https://user-images.githubusercontent.com/11478711/89694521-4d0d8c80-d8e7-11ea-971b-c0d94bc1966d.png)

Caso o jogo não esteja dentro do nosso conjunto de dados da uma mensagem como na foto abaixo.

![stream_2](https://user-images.githubusercontent.com/11478711/89694582-78907700-d8e7-11ea-999c-0a66a92a748c.png)
## Deployment

O próximo passo é implementar um Deploy em algum servidor para deixar publico nosso sistema de recomendação de jogos. Estou em duvida entre utilziar Heroku ou Apache.

## Futuro
Meus proximos passos é fazer um programa dinamico. Se o jogo não esta contido dentro do nosso conjunto, pretendo fazer um web scrap do jogo dentro do site da Steam e pego
os dados necessarios para fazer o calculo de semelhança e retorno a resposta, e no fim acrescento jogo no conjunto final de dados.
