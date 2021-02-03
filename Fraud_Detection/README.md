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

For this project we tested 5 different models, the first test was our baseline which was IsolationForest (which is  model for identifying anomalies within the data), in addition we tested Logistic Regression, Random Forest, Extra Tree and a KNN.


Our data set contains unbalanced data, this means that we have much more than one class than the other, for our problem we have a 99.91% of data are non-fraudulent transactions. In order to get around this problem, we passed to the model a vector with the weight for each class, it was defined for the non fraud class - 0.00091 and for fraud: 0.999, so the model will give an importance to the minority class.

In the Figure below, a table was made with the result for the training data, for the accuracy metrics, Recall, Precision, F1-Score and Kappa-Score, for all metrics, except Kappa-Score.

![tab_metric](https://user-images.githubusercontent.com/11478711/106520051-f14d4600-64ba-11eb-833e-95bb57140c9d.png)

We noticed that the Random Forest model was the one with the best results in all metrics with 99.99% and with a high kappa-score showing that it was wrong in a few cases (we can see in the confusion matrix Figure (A) that it was only 7 values ​​in the total), we don't want to use the random forest for the given values, we have a great chance of overfitting the data.

We will use the second model with the best results, Extra Tree, with the best results, but we can see by Figure B that the Fraud class did not learn so well, the last step is to tune our model to find the best parameters, we used GridSearchcv (we combine all the parameters to find the best one).


Figure A                   | Figure B
:-------------------------:|:-------------------------:
![Heatmap_rf](https://user-images.githubusercontent.com/11478711/106523974-b221f380-64c0-11eb-92eb-45e50beec6f4.png) | ![Heatmap_et](https://user-images.githubusercontent.com/11478711/106524070-cfef5880-64c0-11eb-80fa-c976e887f064.png)

## Bussiness Results
The main questions it was to create a tool to help to minimize the number of fraud transaction, to answer this question we deployed the model together with the data pipeline (cleaning, create features and transformation) in Heroku, to use you have to pass a json and will receive the result back.

Using the model for our test data set, the confusion matrix and the metrics used before was:
![buss_cm](https://user-images.githubusercontent.com/11478711/106536964-2916b680-64d8-11eb-97a2-0e4ccbd04fbc.png)

![metric_bus](https://user-images.githubusercontent.com/11478711/106537040-4ea3c000-64d8-11eb-8ddd-2ef6bbea7bbe.png)
Now we can start answer a few question, like:
- What is the Recall and Precision (Accuracy) of the model?

Acuraccy: 0.961622

Recall: 0.961622

Precision: 0.99872

F1-Score: 0.979236

- What is the reliability of the model in classification as fraud or not?

My model is predicting 96% right non-fraud and 96.8% fraud.


Now answering the questions related to how much the company will receive we have:
![tab_buss](https://user-images.githubusercontent.com/11478711/106536490-56af3000-64d7-11eb-951d-5a6bac9462a8.png)

- What is the revenue of the company if we classify all the transaction in the data?

The revenue of the Blocker Fraud will be R$ 1.35 bilions

- What is the Loss expected if the model fails?

The loss expected is the R$ 3.8 milions

- What is the profit expected to Blocker fraud ?

The profit of the Blocker Fraud will be R$ 1.21 bilions

## Leassons Learned and Next steps.
The lessons learned during this project were that when we work with unbalanced data we need to be more careful because if not treated correctly (in our case, passing a weight vector to our models) we will have a problem in identifying this class. In addition, for the first time I tested QuantileTransformer for numerical variables for the transformation and I liked the results, mapping the data between a uniform Gaussian distribution, helping the model to learn better.

For the next steps I'll try differents transformations to the categorical variables ( it was used label enconder) and to numerical variables trying the combinations. I want to test creating a synthetic variable for the minority class (Fraud), even though I know that fraud in bank data is not a nature with a lot of data. I am also interested in leaving only the two types of payments that are generating fraud and in the others to withdraw from the data set to see the behavior.
