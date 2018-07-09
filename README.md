
# Project Goal

New York has more than 3.5 million apartments in the housing stock. Sixty percent of those are rentals! This project is focusing on one-bedroom apartments in five-boroughs of New York and identifies what factors dictate the rent price. I decided to do analysis on one-bedroom only in order to eliminate the most obvious predictor: number of bedrooms and explore other features contributing to price of rent. 


### Data:
1. **Trulia one-bedroom features.**  First, I used *BeatifulSoup* to get individual URLs for one bedroom apartments in New York. Then I collected apartment features using *Scrapy*. Below is an example from apartment features that I collected.

<img src="https://github.com/elenabohenick/trulia_1br_rentals/blob/master/trulia_data.png" width="331" height="435" />
  
2. Yelp. Number of restaurants within 1 mile of the apartment location scraped from Yelp using *Selenium*.
3. Income data: Medium Income & Number of High Income Households within the apartment ZIP code scraped from <www.incomebyzipcode.com>
4. Demographical data from Census. 


### Hypothesis:



