#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
filmes = pd.read_csv('../filmes/movies.csv')
rates = pd.read_csv('../filmes/ratings.csv')
#print(filmes)
print ('------------------- Desaf 3 -----------------------')
print('Colocar o numero de avaliacoes por filme, nao é só a media mas o total de votos por filme')
print('-> UserID: Quantidade de votos por filme')

mediaFilme = rates.groupby("movieId")["rating"].mean()
#O correto seria contar a rate? o rsultado calculado é o mesmo (not sure about)
#Mas  poderia ser diferente dependendo dos dados?? 
qtdVotos = rates.groupby("movieId")["userId"].count()
grado = filmes.join(mediaFilme, on="movieId")
gradoT = grado.join(qtdVotos, on="movieId")
print(gradoT)
## parte 2 desafio Arrendondar valores de nota_media p/ duas casas decimais
print ('------------------- Arrendondar vlres de rates -----------------------')
gradoT['rating'] = gradoT.rating.astype('double64')
#gradoT['userId'] = gradoT.userId.astype('int64')
print(gradoT)







### descobrir os generos dos filmes -> quais sao únicos) - HARD
####

plt.show()
