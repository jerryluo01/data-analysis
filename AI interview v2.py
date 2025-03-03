import pandas as pd
genre_df = pd.read_csv("genre_data.csv")
movies_df = pd.read_csv("movies_data.csv", usecols=["imdb_rating"])
df = pd.concat([genre_df, movies_df], axis=1)
df1 = df.groupby(["Main_Genre"])[["imdb_rating"]].mean()
print(df1)