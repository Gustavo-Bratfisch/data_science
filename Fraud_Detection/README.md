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

 ## Features 
