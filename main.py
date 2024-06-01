import pandas as pd
import matplotlib.pyplot as plt


netflix_df = pd.read_csv("netflix_data.csv", index_col=0)

netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

netflix_movies = netflix_subset.loc[:, ["title", "country", "genre", "release_year", "duration"]]

short_movies = netflix_movies[netflix_movies["duration"] < 60]

colors = []
for lab, row in netflix_movies.iterrows():
    if row['genre'] == "Children":
        colors.append("Green")
    elif row['genre'] == "Documentaries":
        colors.append("Red")
    elif row['genre'] == "Stand-Up":
        colors.append("Blue")
    else:
        colors.append("Black")

fig = plt.figure(figsize=(12, 8))
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors, alpha=0.5)
plt.title('Movie Duration by Year of Release')
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.show()

answer = "no"
