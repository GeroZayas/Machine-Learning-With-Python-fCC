import pandas as pd

iris = pd.read_csv("https://sololearn.com/uploads/files/iris.csv")

print("These are the columns:")
print(iris.columns)


# ----------------------
def sep():
    print("---" * 30)


# ----------------------

sep()

# print(iris.head())

# print("This is the SHAPE", iris.shape)

# Drop the id columnn
iris.drop("id", axis=1, inplace=True)

print(iris.head())
print("New Shape", iris.shape)

sep()
print("IRIS. DESCRIBE -> Statitics" + "\n")
print(iris.describe())

sep()

print("SAMPLE by CATEGORY:")
print(iris.groupby("species").sample(10))

sep()
