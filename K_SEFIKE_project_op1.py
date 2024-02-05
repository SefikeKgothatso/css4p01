# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:13:16 2024

@author: NWUUSER
"""

import pandas as pd
file = pd.read_csv("movie_dataset.csv")
print(file)
file.isnull()
missing_values = file.isnull()
missing_count = missing_values.sum()

file['Metascore'].fillna(file['Metascore'].mean(), inplace=True)
file['Revenue (Millions)'].fillna(file['Revenue (Millions)'].mean(), inplace=True)

#Question 1
highest_rating = file['Rating'].max()
print(f"The highest rating in the dataset is: {highest_rating}")

max_rating_index = file['Rating'].idxmax()
highest_rated_movie = file.loc[max_rating_index]
print(highest_rated_movie)

#Question 2
average_revenue = file['Revenue (Millions)'].mean()
print(f"The average revenue of all movies in the dataset is: {average_revenue} million dollars")

#Question 3
filtered_file = file[(file['Year'] >= 2015) & (file['Year'] <= 2017)]
average_revenue_2015_to_2017 = filtered_file['Revenue (Millions)'].mean()
print(f"The average revenue of movies from 2015 to 2017 in the dataset is: {average_revenue_2015_to_2017} million dollars")

#Question 4
movies_2016 = file[file['Year'] == 2016].shape[0]
print(f"The number of movies released in the year 2016 is: {movies_2016}")

#Question 5
nolan_movies = file[file['Director'] == 'Christopher Nolan']
num_nolan_movies = len(nolan_movies)
print(f"The number of movies directed by Christopher Nolan is: {num_nolan_movies}")

#Question 6
high_rated_movies = file[file['Rating'] >= 8.0]
num_high_rated_movies = len(high_rated_movies)
print(f"The number of movies with a rating of at least 8.0 is: {num_high_rated_movies}")

#Question 7
nolan_movies = file[file['Director'] == 'Christopher Nolan']
median_rating_nolan_movies = nolan_movies['Rating'].median()
print(f"The median rating of movies directed by Christopher Nolan is: {median_rating_nolan_movies}")

#Question 8
average_rating_by_year = file.groupby('Year')['Rating'].mean()
max_avg_rating_year = average_rating_by_year.idxmax()
max_avg_rating_value = average_rating_by_year.max()
print(f"The year with the highest average rating is {max_avg_rating_year} with an average rating of {max_avg_rating_value:.2f}")

#Question 9
movies_2006_to_2016 = file[(file['Year'] >= 2006) & (file['Year'] <= 2016)]
movies_count_2006 = len(file[file['Year'] == 2006])
movies_count_2016 = len(file[file['Year'] == 2016])
percentage_increase = ((movies_count_2016 - movies_count_2006) / movies_count_2006) * 100
print(f"The percentage increase in the number of movies made between 2006 and 2016 is: {percentage_increase:.2f}%")

#Question 10
from collections import Counter
import re

all_actors = [actor for actors in file['Actors'].str.split(', ') if isinstance(actors, list) for actor in actors]
actors_count = Counter(all_actors)
most_common_actor, num_occurrences = actors_count.most_common(1)[0]
print(f"The most common actor in all the movies is: {most_common_actor} with {num_occurrences} occurrences.")

#Question 11
unique_genres = file['Genre'].unique()
num_unique_genres = len(unique_genres)
print(f"The number of unique genres in the dataset is: {num_unique_genres}")

all_genres = [genre.strip() for sublist in file['Genre']. apply(lambda x: re.split(',|and', x)).tolist() for genre in sublist]
unique_genres = file['Genre'].unique()
num_unique_genres = len(unique_genres)
print(f"The number of unique genres in the dataset is: {num_unique_genres}")

#Question 12
numerical_columns = ['Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']
numerical_file = file[numerical_columns]
correlation_matrix = numerical_file.corr()
print("Correlation Matrix:")
print(correlation_matrix)
