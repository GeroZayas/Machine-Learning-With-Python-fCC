import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

rent_df = pd.read_csv("./assets/Barcelona_rent_price.csv")

columns = rent_df.columns
print(columns)

avg_price_by_nbhood= rent_df[["District", "Neighbourhood", "Price"]].groupby("Neighbourhood")

print(rent_df[["District", "Neighbourhood", "Price"]])

print("-------------------")

print(avg_price_by_nbhood)
 