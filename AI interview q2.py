import pandas as pd
movies_df = pd.read_csv("movies_data.csv")
movies_df["count"] = 1
print(movies_df.groupby(["rating"]).count()[["count"]])