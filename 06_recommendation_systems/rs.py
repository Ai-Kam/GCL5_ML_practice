import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ratings = pd.read_csv('ml-latest-small/ratings.csv')
movies = pd.read_csv('ml-latest-small/movies.csv')

data = pd.merge(ratings, movies, on='movieId')

rating_average = pd.DataFrame(data.groupby('title')['rating'].mean())
rating_average['rating_count'] = pd.DataFrame(data.groupby('title')['rating'].count())

movie_matrix = data.pivot_table(index='userId', columns='title', values='rating')

favorite_movie_ratings = movie_matrix["Mr. Bean's Holiday (2007)"]
similar_movies = movie_matrix.corrwith(favorite_movie_ratings)

correlation = pd.DataFrame(similar_movies, columns=['Correlation'])
correlation.dropna(inplace=True)
correlation = correlation.join(rating_average['rating_count'])

recommendation = correlation[correlation['rating_count'] > 100].sort_values('Correlation', ascending=False)

recommendation = recommendation.merge(movies, on='title')

print(recommendation.head(10))
