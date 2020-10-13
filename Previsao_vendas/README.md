# Previsão de vendas de uma desenvolvedora e distribuidora relacionada a softwares

**Previsão de vendas de softwares e jogos utilizando Random Forest**

## O problema

As empresas quando estão pensando em fazer um investimento ou uma reforma de uma das lojas, necessitam saber quanto de receita vão receber dentro de um periodo do tempo para saber o quanto desse dinheiro pode ser utilizado. Com Modelos de Machine Learning para Séries Temporais para prever a receita tanto para a compania toda ou apenas para uma loja especifica. No conjunto de dados que trabalhamos tinhamos informação do dia da compra, a quantidade, o produto ( ID do produto), a categoria do produto, o ID da loja e em outro conjunto de dados temos o nome da loja e o endereço da loja (a lojas estão espalhados por toda Russia e tambem vendem online).

## Hipóteses de negócio
- Lojas que vendem maior diversidades de produtos tem uma receita maior. Depende, temos que lojas que vendem abaixo de 45 categorias elas tem uma receita baixa comparadas com as demais porém não mostra que lojas que vendem mais de 55 estão com a receita mais alta. 

![Quantidade_per_receita](https://user-images.githubusercontent.com/11478711/95864715-2b43e200-0d3c-11eb-845d-942349f11e86.png)

- Lojas em Cidades Grandes na média não vendem mais que as demais. Falsa, se olharmos apenas para a soma final tem sentido as lojas em cidades maiores ter valores superiores que se deve ao tamanho da loja, porém quando calculamos a média notamos que os valores proximas até abaixo das demais.

![Per_city](https://user-images.githubusercontent.com/11478711/95865007-88d82e80-0d3c-11eb-8425-10272d6aa5ec.png)

## Feature engineering

O feature enginering serve tanto para tratarmos o nosso dados, assim como a criação de novas variaveis para aprimorar nosso modelo. Nessa fase fizemos:
- **Tratamento de dados**
  - Missing values 
  - Outliers.
  
- **Criação da variavel** 
  - Variaveis Ligada a time series para que o modelo melhor entenda sazionalidade e vendas de datas anteriores:
    - Sazionalidade que foi feito a diferença entre a venda com a venda feita a 360 dias atrás.
    - Variavel Lag 1 que é a diferença entre a venda pela a venda feita no dia anterior.
  - Separamos o dia, o mês e o ano da nossa data e tambem criamos a variavel tempo de loja.
  - Retiramos do Endereço das lojas apenas a cidades
  
- **Transformação das variaveis** é utilizado para que o nosso modelo consiga entender e trabalhar melhor com os nossos dados:
  - Númericas: Fizemos o reescalamos dos valores númericos para ficar em intervalos menores.
  - Categóricas: Transformamos as cidades em valores númericos utilizando o Label Enconder
  - Cíclicas: As variaveis transformadas foram as datas (dia, mês, mês do ano ...)
  
- **Seleção de Variaveis**, vamos pegar apenas as variaveis mais importantes para o modelo
  - Algoritmo Boruta
  - Inspeção visual
## Modelos
Como estamos trabalhando com uma serie temporal multivariada é possivel utilizar modelos como Random Forest ou XGBoost, entretanto temos que modelos como VAR (Vector autoregressive model) ou modelos de aprendizado supervisionado tambem funcionam bem (usualmente series temporais univariado são modelados utilizado modelos de ARIMA - ARIMAX).

Os dois modelos utilizados não preve valores no tempo t+1 por isso que foi feito o Feature Engineering em relação ao tempo, para conseguir que nosso modelo aprenda precisamos que nossos dados sejam um serie historica. Além disso precisamos dividir corretamente, não podemos separar nossos dados aleatoriamente e sim cortando em um periodo.

## Resultados
Para fazer a avaliação do modelo vamos utilizar 3 diferentes métricas:
- MAE: O valor absoluto da media da diferença entre o valor real e o valor predito
- MAPE: É a porcentagem do valor absoluto da media da diferença entre o valor real e o valor predito
- RMSE: É a raiz quadrada da media da diferença entre o valor real e o valor predito

Para nosso modelo final chegamos ao resultado:

![Resultado_final_modelo](https://user-images.githubusercontent.com/11478711/95860653-ba4dfb80-0d36-11eb-991d-7c0e2dc373c9.png)

Com esse resultado foi possivel encontrar o pior e o melhor cenario possivel, seria o minimo e o maximo que o nosso negocio vai lucrar.

![cenarios](https://user-images.githubusercontent.com/11478711/95860843-013bf100-0d37-11eb-89a1-1b7cdad8edbc.png)

Podemos ver os shop que foram piores colocados em relação as metricas estão com os valores muito acima do que encontrados no geral, para esses cincos shops esse modelo não é util, teriamos que fazer uma analise nessas lojas para ver oque esta acontecendo (pode ser que tenha poucos dados para essas lojas)

![image](https://user-images.githubusercontent.com/11478711/95859982-c9807980-0d35-11eb-8002-2a80fe76d235.png)

Porém quando vemos a disposição de todas as lojas conseguimos ver tirando esses outliers, temos que o modelo conseguiu representar bem para o restante ficando com o MAPE em torno de 17%.

![Mape_shops](https://user-images.githubusercontent.com/11478711/95860122-fd5b9f00-0d35-11eb-8389-78784409f5b0.png)

Plotando os valores reais pelo previsto, temos que nosso modelo conseguiu aprender bem, até mesmo a sazionalidade que geralmente é um problema em series temporais.

![Predito_real](https://user-images.githubusercontent.com/11478711/95861349-ad7dd780-0d37-11eb-884a-0ac9fa3b8d6c.png)

Por fim criamos a taxa do erro que não nada mais que dividir as nossas predições dividido pelos valores reais. Pelo grafico notamos que os nossos valores preditos estão sempre acima dos reais, o modelo está superestimando os valores mas com valores toleraveis. Entretanto no ultimos dois dias tempo uma alta taxa do erro que pode estar ocacionando por causa daqueles 5 shops que vimos anteriormente.

![taxa_erro](https://user-images.githubusercontent.com/11478711/95861533-f3d33680-0d37-11eb-9906-3eb8797e5094.png)

## Conclusão

A construção do modelo foi bem sucedida, temos um modelo robusto que consegue prever a receita para as proximas 6 semanas, entretanto tem espaço para melhorar principalmente sabendo que algumas lojas não estão respondendo bem ao modelo. Conseguimos encontrar que o lucro total da empresa das ultimas semanas vai estar em torno de 94 milhôes, podendo realocar esses valor para fazer o investimento/reforma da maneira necessaria.

No futuro podemos fazer implementar diferentes modelos para fazer a comparação dos modelos e também para colocar em produção podemos criar uma API junto com um chat-bot do Telegram que devolve as previsões diretamente para o celular.
