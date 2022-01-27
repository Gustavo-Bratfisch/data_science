# Churn Bank

## This projects aims decrease the number of clients that leaves the company (churn) and show the financial return of these clients

#### This project was made by Gustavo Bratfisch.

# 1. Business Problem.

TopBank is a large banking services company. It operates mainly in European countries offering financial products, from bank accounts to investments, passing through some types of insurance and investment product.

The main product of the company is a bank account, which the client can deposit his salary, withdrawals, deposits and transfer to other accounts. The bank account has no cost to the client and it's valid for 12 month, after these 12 month the client has to renew the account for another 12 months.

According to analytics team of TopBank, each client that has an account return a monetery amount of 15% of their estimated salary if it is below of the average salary of all clients and 20% if this salary is above the average. The average and the porcetage of return if calculated annualy.

In the last few month, the Analytics team realized that the rate of customers cancelling their bank account reached unprecedented numbers in the company. Concerned about this high rate, the company contract me as a Data Sciencts to create a plan to reduce the churn rate (rate of customers cancelling their accounts) and show a financial return to the bank. 

At the end of the work, we will delivery a machine learning model in production that return in order all the probability of each client to churn and a report answer these three question:

**1. What is the current churn rate of TopBank? How it varies monthly?**

**2. What is the model performance to classify clients as churn?**

**3. What is the expected return, in terms of revenue, if the company uses its model to avoid customer churn?**

A possible action for retain these clients, is to offer a discount cupom or a tax incentive, which clients do you offer theses discount cupom and what value. Remembering that the sum of the incentives cannot exceed R$10,000.00. 

# 2. Business Assumptions.

- In these project we are working with company data, where each column represent a client.

## 2.1 Data

- RowNumber: The number of the row
- CustomerID: Customer unique identifier
- Surname: The client surname.
- CreditScore: Customer Credit score for the consumer market.
- Geography: The country where the client live.
- Gender: The client gender.
- Age: The client age.
- Tenure: Number of years the customer has been active.
- Balance: The monetary value the client has in his account.
- NumOfProducts:The number of product the client bought of the bank.
- HasCrCard: Indicate if the client has a credit card or not.
- IsActiveMember: Indicates if the client made at least one movement in the bank account within 12 months.
- EstimateSalary: Estimate of the client's monthly salary.
- Exited: Indicate if the client leaves or not.

# 3. Solution Strategy

My strategy to solve this challenge was:

**Step 01. Data Description:** We first analyse data: to see data type, see if have some inconsistency and missing value. And in the end make the descriptive statistics.

**Step 02. Feature Engineering:** Create new features based on the coluns, to create a new informations. In the part we also create a some hypothesis about the business, to gain import informations. 

**Step 03. Data Filtering:** We filter the data of some incosistency.

**Step 04. Exploratory Data Analysis:** In this part, we divide in three parts: 
1. First we do a univariate analysis
2. Second we do a bivariate analysis, trying to respond the hypothesis we create in the step 2
3. Third we made a multivariate analysis doing a data correlation 

**Step 05. Data Preparation:** Data Preparation for best fit in machine learning, doing some scaler to keep inside a good range.

**Step 06. Feature Selection:** Select the best features for the model (using Boruta and Random Forest for it).

**Step 07. Machine Learning Modelling:** Test differents models, to find those have the best metrics (in this case Recall to have less false negative). For this problem we are going to use the probability for the client be in churn.

**Step 08. Hyperparameter Fine Tunning:** After get the best model, we tunning the parameters to give an best metrics

**Step 09. Convert Model Performance to Business Values:** In this part, we give back the financial return and the clients who will receive cupom discount. We are going to order for the higher probability to churn and give a cupom of discount.

# 4. Top 3 Data Insights

**Hypothesis 01: Person with age above 50 year has more chance of Chrun**

**True.** - We see the group have more chance to churn is above 50 years, and running a hypothesis test to group above 50 and below 50 years old has a different distribuition between than.

![hyphotesis1](https://user-images.githubusercontent.com/11478711/151144231-05273523-d669-4969-9163-05e896177411.png)

**Hypothesis 02: The Highest time as client in the bank the lower is the credit score**

**False.** We can see the line in the middle show they have the same median.

![hyphotesis2](https://user-images.githubusercontent.com/11478711/151145001-34e45bf2-c609-4701-8296-80008900a0c1.png)

**Hypothesis 03: Client with more tenure has last chance to churn**

**False.** There is no difference between churn and not churn in the distribuition.

![hyphotesis3](https://user-images.githubusercontent.com/11478711/151145121-b18800e7-a027-4544-88df-4c7dbace6a83.png)

# 5. Machine Learning Model Applied
At the first CRISP cycle for this project, the following models was tested:

1. Logistic Regression
2.  Random Forest
3.   KNN
4.   XGBoost 
5.   ExtraTree

The metrics for each model, in this project we are focusing in do a recall metric better to have less false negative.

![image](https://user-images.githubusercontent.com/11478711/151150943-5b29175a-f4e8-40b2-ae8d-4505a979381e.png)

# 6. Machine Learning Modelo Performance

The model chosen was XGBoost, 

![image](https://user-images.githubusercontent.com/11478711/151341856-c0275602-0a97-4bcb-91eb-811cee1c6e96.png)

ALso we plotted the cumulative gain curve that shows us where all the positive cases are in the porcentage of all population (example 20% of our churn people represent 60% of all cases) and the Lift curve that show how our model is better in choose client that will be in churn than a random choice.

# 7. Business Results

Respond to CEO question:
**1. What is the current churn rate of TopBank? How it varies monthly?**
The churn Rate of the company is 20.37% and monthly is 7.07%.

**2. What is the model performance to classify clients as churn?**
The model is correct classifying clients as churn in 68%

**3. What is the expected return, in terms of revenue, if the company uses its model to avoid customer churn?**

Using the model to predict all the churn corretly, we will have a return of R$6 milion, but the problem here that to have back these clients we are going to give discount cupom and we only have R$10.000, for this we are going to choose the clients with higher Revenue for the company. 

In this scenarios, we will give cupons of R$100,00 for the  100 clients with high probability churn, in this way the return will be of R$2328180,00 +/- 4545,00, where we predict right 85% clients that churn in did.

Here we tested differents values of cupons.

# 8. Conclusions

# 9. Lessons Learned

# 10. Next Steps to Improve

- Create new features to help to improve the model.
- Investigate some salary that is below R$100,00
- Create a rule, what client will the company already lost and the company has the chance to continue
- Improve a KnapSack to optimization problem to give discount cupom for clients in churn. 

# LICENSE

# All Rights Reserved - Comunidade DS 2022
