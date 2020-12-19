# Comparison of the Disclosed Data for the City of Indaiatuba and the State of São Paulo.

## The Problem

A few months after the pandemic/"lockdown" started in Indaiatuba, I got curious to see the behavior of the disease here, so I searched in the official website of the Indaiatuba City Hall for some data at the same time I saw some posting on social networks about the offical data released by the state government, when I did the comparison it didn't match the values.


## Data

Government data was easy to obtain, it is available on github at https://github.com/seade-R/dados-covid-sp/tree/master/data. While city hall data was obtained from each note released ino https://www.indaiatuba.sp.gov.br/saude/vigilancia-em-saude/vigilancia-epidemiologica/novo-coronavirus/notas/, removing from the text, the number of deaths, number of infected, ICU beds and clinical inmates, ages, comorbidity and gender. Thus, two different data sets were created, in the first we have the date of the event, number of deaths, infected by both the government and the city, in the second data we have the characteristics of people who died, such as ages, sex, comorbidity (we take into account hypertension, diabetes, kidney disease, lung disease, obesity and heart problems.

## Results
For data analysis and visualization I decided to use Tableau to test the tools. All the graphics will be on my Tableau public page. The advantage of Tableau is that interactive, you can click on the ages or the genre that it does the filtering of the data within the graphics done.

I will give an overview of the results. We see that deaths occur with people over 30 years old and mostly with people over 60 years old. Being 60% male and 92% had some comorbidity, they may have been listed in this project or something different. In addition 40% of people had hypertension, only 20% had diabetes(https://tabsoft.co/2J2Hh7s), with you click in these barplot you can see the distribution per age of the comorbity and the division by genre.

![Painel_Caract](https://user-images.githubusercontent.com/11478711/102696186-34a16d00-420b-11eb-983d-061de2ebd16e.png)

Visualizing the growths of infected, a difference in cases of infected is evident after June, a difference that reaches around 2000 thousand cases, this difference increases for a long time until reaching the green phase of the São Paulo plan where the cases for the Government of SP started to increase. Looking at the daily cases, the data from the city hall remains within a range while the government data has a high variance.

![Conf1](https://user-images.githubusercontent.com/11478711/102696374-98786580-420c-11eb-9b0e-9a6c06af773a.png)


However, when we look at the data from number of deaths we see the same behavior until the day of the change to the green phase, which happens a death peak with 187, after that peak where values stay the same

![Obi2](https://user-images.githubusercontent.com/11478711/102696451-2e13f500-420d-11eb-843a-60030beaa720.png)

Adding the values per month of the number of infected / death, from May to September the data from the city hall are higher than those from the governments, after these months there is an increase in the government figures. Especially for October, where the number of Government cases is the highest of all months of the two data sets.

![Men_da](https://user-images.githubusercontent.com/11478711/102696725-002fb000-420f-11eb-936f-9e2faf85a905.png)


## Conclusion

We can conclude that for the initial 5 months of the pandemic there was a big difference for the number of infected (on average 2 thousand cases) and the number of deaths (about 30 deaths), after these months we can see an increase of infected people in the government data trying to get the difference smaller. I believe that by the end of December these data will be even.

This project was made to train web scraping skills and to learn and train Tableau .
