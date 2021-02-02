# A model to Fraud Detection.

## Fraud Detection Problem

In this project we seek to help the Blocker Fraud enterprise to detect the fraud transactions.

A empresa vai receber: The company will receive: 25% of the value of each transaction truly detected as fraud. 5% of the value of each transaction detected as fraud, but the transaction is truly legitimate.

However it returns 100% of the value to the customer, for each transaction detected as legitimate, however the transaction is truly a fraud.

Main Goal Create a tool to help to minize the number of fraud transaction

## Business Question?

- Main Goal is to create a tool to help to minize the number of fraud transaction
- What is the Recall and Precision (Accuracy) of the model?
- What is the reliability of the model in classification as fraud or not?
- What is the revenue of the company if we classify all the transaction in the data?
- What is the Loss expected if the model fails?
- What is the profit expected to Blocker fraud ?

## Data

The raw data was download at https://www.kaggle.com/ntnu-testimon/paysim1, with 6 milions rows and 11 features that are, the name of the origin and destination, the old and new balance for the origin and the destination account, the amount, type (CASH-IN, CASH-OUT, DEBIT, PAYMENT and TRANSFER), an hour step (maps a continue unit of time in the real world, the max is 744 - 30 days of simulation), if was a fraud or not and a fraud flagged to control massive transfers from one account to another and flags illegal attempts.

 ## Insights
 Doing an exploratory data analysis to find usefull insights for our problem/model.
 
 ### The amount of fraud is the same for all hours
Looking to the Figure 2, we have the hour of the day of each non-fraud tansaction happens between 9:00 to 23:00, meanwhile for fraudulent transactions (Figure 1) they happen constant for all hours of the day. Thus, between 0-7 there is a greater chance of a fraudulent transaction to happen.

Figure 1                   | Figure 2
:-------------------------:|:-------------------------:
![Hour_fraud](https://user-images.githubusercontent.com/11478711/106042641-18bba180-60bc-11eb-8a89-d339e06a4820.png) | ![Hour_nonfraud](https://user-images.githubusercontent.com/11478711/106042743-3ab52400-60bc-11eb-976d-699506dfda1a.png)


### The payments are made between day 6 until 17 of the month

The transaction are made between 6 until 17 due to the receipt of the salary.

![day_trans](https://user-images.githubusercontent.com/11478711/106500412-8e4eb580-64a0-11eb-944c-f0ce654e9824.png)

### The transfer represents the highest percentage of money transferred

Transfer represents 71.5% of the gross money transferred in total and Debit the lowest amount

![tabel](https://user-images.githubusercontent.com/11478711/106503978-1767eb80-64a5-11eb-8446-0920fe49b257.png)


## Model

Para esse projeto testamos 5 diferentes modelos, sendo 1 o baseline que foi IsolationForest (que não é um modelo para identifica anomalias dentro dos dados), além disso testamos Regressão Logistica, Random Forest, Extra Tree e uma KNN.

Nosso conjunto de dados contém dados desbalanceados, isso quer dizer que temos muito mais de uma classe do que da outra, para o nosso problema estamos com um 99.91% de dados são transação não fraudulentas. Para contornar esse problema passamos para o modelo um vetor com o peso para cada classe, foi definido para a classe non fraud - 0.00091 e para fraud:0.999, dessa forma o modelo dará uma importancia para a classe minoritaria.

Na Figura abaixo foi feito uma tabela com o resultado para os dados de treino, para as metricas de Accuracia, Recall, Precision, F1-Score e Kappa-Score, para todas as mettricas, menos Kappa-Score.

![tab_metric](https://user-images.githubusercontent.com/11478711/106520051-f14d4600-64ba-11eb-833e-95bb57140c9d.png)

Notamos que o modelo de Random Forest foi o com os melhors resultados em todas as metricas com 99.99% e com um kappa-score alto mostrando que errou em poucos casos (podemos ver na matrix de confusão Figura (A) que errou apenas 7 valores no total), não queremos utilizar o random forest pelos valores dado temos uma grande chance de acontecer um overfitting nos dados. 

Vamos utilizar o segundo modelo com melhor resultados que foi o Extra Tree, com melhores resultados, porém vemos pela Figure B nao aprendeu tão bem a classe Fraud, the last step is to tune our model to find the best parameters, we used GridSearchcv (we combine all the parameters to find the best one).

Figure A                   | Figure B
:-------------------------:|:-------------------------:
![Heatmap_rf](https://user-images.githubusercontent.com/11478711/106523974-b221f380-64c0-11eb-92eb-45e50beec6f4.png) | ![Heatmap_et](https://user-images.githubusercontent.com/11478711/106524070-cfef5880-64c0-11eb-80fa-c976e887f064.png)

## Bussiness Results

![buss_cm](https://user-images.githubusercontent.com/11478711/106536964-2916b680-64d8-11eb-97a2-0e4ccbd04fbc.png)


![metric_bus](https://user-images.githubusercontent.com/11478711/106537040-4ea3c000-64d8-11eb-8ddd-2ef6bbea7bbe.png)

![tab_buss](https://user-images.githubusercontent.com/11478711/106536490-56af3000-64d7-11eb-951d-5a6bac9462a8.png)

