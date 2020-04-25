#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
# Primeira aula de quarent. Dados
# Estudar p n morrer de tédio
print ('-------------------Quarentena dados-----------------------')
print ('------------------------------------------------------------')

filmes = pd.read_csv('../filmes/movies.csv')
rates = pd.read_csv('../filmes/ratings.csv')

### Basicos ###
# Exibindo a media <metodo mean()> das notas <rating> de todos os filmes (top 5 -> head())

# Juntar um data frame e um series*?*  Unir conjunto de dados
# Diferente de unir dois data frames

# Data frame + Series : 
# ERRADO  
#filmes["nota_media"] = rates.groupby("movieId")["rating"].mean()
# NaN -> Not a number | Filmes sem voto

# ---this MAY be the corrent one
mediaFilme = rates.groupby("movieId")["rating"].mean()
print(mediaFilme.head())
print(filmes.join(mediaFilme, on="movieId"))
# Basic Tip -> var com a referencia p/ msm informacao (data grip?*)
moviesAndRate = filmes.join(mediaFilme, on="movieId")
print ('------------------------------------------------------------')
print(moviesAndRate.head())
# Exibe a lista movieAndRate, com sort ordenando crescentemente (ordena pela nota, clarious)
# Valores [filmes] q nao tem nota -> NaN (Not a nUmber)
print ('------------------------------------------------------------')
print(moviesAndRate.sort_values('rating', ascending=False).head())

#Grafico com votos do filme 1 
rates.query("movieId== 2 ")["rating"].plot(kind='hist')




#sample pra exibir grafico abaixo c caracteri
#rates.groupby("movieId")["rating"].mean().head().plot()
plt.show()

