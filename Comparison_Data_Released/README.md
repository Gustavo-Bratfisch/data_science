# Comparison of the Disclosed Data for the City of Indaiatuba and the State of São Paulo.

## The Problem

A few months after the pandemic/"lockdown" started in Indaiatuba, I got curious to see the behavior of the disease here, so I searched in the official website of the Indaiatuba City Hall for some data at the same time I saw some posting on social networks about the offical data released by the state government, when I did the comparison it didn't match the values.


## Data

Os dados do governo foram facieis de conseguir, esta disponibilizado no github (https://github.com/seade-R/dados-covid-sp/tree/master/data) com o formato de csv. Enquanto os dados da prefeitura foram obtidos atraves das notas divulgadas no https://www.indaiatuba.sp.gov.br/saude/vigilancia-em-saude/vigilancia-epidemiologica/novo-coronavirus/notas/, retirando dentro do texto, o número de obitos, número de infectados, leitos UTI e internados clinicos, idades, comorbidade e gênero. Dessa forma foi criado dois diferentes conjunto de dados, no primeiros temos a data do acontecimento, número de obitos, infectados tanto do governo quanto da prefeitura, no segundo conjunto de dados temos as caracteristicas das pessoas que vieran a óbito como idades, sexo, comorbidadade (levamos em consideração as doenças hipertensão, diabetes, doenças renais, doenças pulmonares, obesidade e problemas cardiacos.

## Resultados
Para as analises e visualizações de dados eu decidi utilizar o Tableau para testar as ferramentas. Todos os Graficos vão estar na minha pagina do Tableau public. A vantagem do Tableau é que interativo, voce pode clicar nas idades ou no genero que ele faz a filtragem dos dados dentros dos graficos feito.

Vou dar uma visão geral dos resultados. Vemos que os óbitos ocorrem com pessoas acima de 30 anos e majoritariamente com pessoas acima de 60 anos. Sendo 60% homem e 92% tiveram alguma comorbidade podendo ter sido listado nesse projeto ou algo diferente. Além disso 40% das pessoas tinham hipertensão, apenas 20% com diabetes(https://tabsoft.co/2J2Hh7s).

![Painel_Caract](https://user-images.githubusercontent.com/11478711/102696186-34a16d00-420b-11eb-983d-061de2ebd16e.png)

Visualizando os crescimentos de infectados é evidente uma diferença nos casos de infectados após junho um diferença que chega na casa dos 2000 mil casos, essa diferença aumenta durante um bom tempo até chegar na fase verde do plano São Paulo onde os casos para o Governo de SP começaram a aumentar. Olhando para os casos diarios os dados da prefeitura se mantem dentro de um intervalo enquanto o do Governo tem uma alta variancia.

![Conf1](https://user-images.githubusercontent.com/11478711/102696374-98786580-420c-11eb-9b0e-9a6c06af773a.png)

Porém quando olhamos para os dados de Óbitos vemos o mesmo comportamento até o dia da mudança para fase verde, que acontece um pico de morte com 187, depois desse pico onde valores ficam na mesma.

![Obi2](https://user-images.githubusercontent.com/11478711/102696451-2e13f500-420d-11eb-843a-60030beaa720.png)

Somandos os valores por mês do número de infectados/óbito, de Maio até Setembro os dados da prefeitura são superiores ao do Governos, após esses meses tem um acrescimos nos valores do governo. Principalmente para Outubro, onde o numero de casos do Governos é o maior de todos os meses dos dois conjuntos de dados.

![Men_da](https://user-images.githubusercontent.com/11478711/102696725-002fb000-420f-11eb-936f-9e2faf85a905.png)


## Conclusion

Podemos concluir que para os 5 meses iniciais da pandemia exestiu uma grande diferença para o número de infectados (na média 2 mil casos) e numero de obitos (cerca de 30 óbitos), depois desse tempo podemos notar valores altos para aproximar dos valores divulgados pela prefeitura de Indaiatuba. Acredito que até o fim de Dezembro esses dados estejam no mesmo valores.

Esse projeto foi feito para treinar as habilidades de web scraping e começar a utilizar Tableau para visualização de dados.
