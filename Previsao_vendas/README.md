# Previsão de vendas de uma desenvolvedora e distribuidora relacionada a softwares

**Previsão de vendas de softwares e jogos utilizando Random Forest**

## O problema

As empresas quando estão pensando em fazer um investimento ou uma reforma de uma das lojas, necessitam saber quanto de receita vão receber dentro de um periodo do tempo para saber o quanto desse dinheiro pode ser utilizado. Com Modelos de Machine Learning para Séries Temporais para prever a receita tanto para a compania toda ou apenas para uma loja especifica. No conjunto de dados que trabalhamos tinhamos informação do dia da compra, a quantidade, o produto ( ID do produto), a categoria do produto, o ID da loja e em outro conjunto de dados temos o nome da loja e o endereço da loja (a lojas estão espalhados por toda Russia e tambem vendem online).

## Hipóteses de negócio
- Lojas que vendem maior diversidades de produtos tem uma receita maior.
- Lojas em Cidades Grandes na média não vendem mais que as demais.


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

Nesse projeto testamos esses dois modelos, depois de realizar teste com os parametros encotramos Random Forest que melhor se encaixou no nosso problema.

## Resultados
