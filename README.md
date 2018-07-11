
# Project Goal

New York has more than 3.5 million apartments in the housing stock. Sixty percent of those are rentals! This project is focusing on one-bedroom apartments in five-boroughs of New York and identifies what factors dictate the rent price. I decided to do analysis on one-bedroom only in order to eliminate the most obvious predictor: number of bedrooms and explore other features contributing to price of rent. 


### Data:
1. **Trulia one-bedroom features.**  First, I used *BeatifulSoup* to get individual URLs for one bedroom apartments in New York. Then I collected apartment features using *Scrapy*. Below is an example from apartment features that I collected.

<img src="https://github.com/elenabohenick/trulia_1br_rentals/blob/master/trulia_data.png" width="331" height="435" />
  
2. Yelp. Number of restaurants within 1 mile of the apartment location scraped from Yelp using *Selenium*.
3. Income data: Medium Income & Percent of High Income Households within the apartment ZIP code scraped from www.incomebyzipcode.com
4. Demographical data from Census. 

### EDA & Feature Engeneering

-	Trulia dataset required a lot of cleaning and preprocessing: Features describing an apartment needed to be converted to categorical variables. First they needed to be cleaned: there were instances where the same features would be described in different words. I combined those features. Then I identified how many times each feature appeared in the dataset and created binary variables out of the top 30 most popular apartment features.
-	All datasets were merged at a zip code level. Thus demo and income metrics were the same for all the apartments within the same ZIP code which is not ideal, but it was the most granular level that was available. Yelp data however was at an address level.
-	The dependent variable is right skewed
-	Based on EDA the following features have moderate positive correlation with the rent price: number of restaurants, median income, and pct of high income households.
-	Out of all apartment features (binary variables) 'fitness center' has the highest correlation with the 1br apt rent price

### Tested Methods and Models
Response variable is apartment price, which is a continuous variable and requires a use of a Linear Regression Model.
- I tested Statsmodels first. I created feature matrix (X) and target vector (y) using patsy.dmatrices. Then ran OLS model and got an R-sqr of ~58% on my test set. 


TO BE CONTINUED





