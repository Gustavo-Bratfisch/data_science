# Recomendação de Jogos na Steam

Nesse projeto iremos fazer uma análise exploratorio dos dados mostrando um pouco mais sobre os dados e 
depois utilizaremos Flask para criar uma aplicação local para recomendação de jogos na steam (jogos com lançamento até maio de 2019).

## Inicio

Podemos dividir esse trabalho em duas partes.

### - Primeira Parte: Visualização dos dados: **https://bit.ly/30wq5xg**

Nessa parte tentamos entender um pouco mais de como os dados estão distribuidos, fizemos alguns agrupamentos para ver quais são os generos majoritarios(grafico abaixo) e o tipo de jogo
![genre_game](https://user-images.githubusercontent.com/11478711/89574241-35100d00-d802-11ea-84d4-8226507566c1.png)

Criamos uma medida de avaliação baseada nas taxas de avaliações positivas e negativas dos jogos e fazendo um simples agrupamento conseguimos notar alguns pontos interessant e 
plotando conseguimos notar que jogos MM são que tem o maior feedback tanto positivo quanto negativo e nos restante seguem o mesmo padrão

![ratin_gem](https://user-images.githubusercontent.com/11478711/89574165-1447b780-d802-11ea-950b-6246a6c4b9a3.png)


### - Segunda Parte: Visualização dos dados: **https://bit.ly/30y8HIe**


Nessa segunda parte criamos nosso modelo utilziando a metodologia de recomendação baseada em conteúdo onde passamos descrições dos jogos, o modelo computa TF-IDF (Term Frequency-Inverse Document Frequency) 
que calcula uma matrix onde na coluna representa a uma avaliação da frequencia da palavra aparecer. Com essa matrix utilizamos uma metrica de similaridade (no nosso caso foi sigmoid_kernel) e por fim ordenamos pelo score feito anteriormente para ver os 10 jogos mais semelhantes. 

Para finalizar cronstruímos um local web usando Flask, inicalmente voce sente uma diferença por precisar criar um template para que os resultados apareçam, necessitando um conhecimento basico de html (não é muito dificil aprender).


![final_app](https://user-images.githubusercontent.com/11478711/89566880-2ff99080-d7f7-11ea-928e-c60843044940.png)
## Deployment

O próximo passo é implementar um Deploy em algum servidor para deixar publico nosso sistema de recomendação de jogos. Estou em duvida entre utilziar Heroku ou Apache.
