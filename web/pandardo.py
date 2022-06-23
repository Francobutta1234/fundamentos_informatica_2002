import pandas as pd

dato ={1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
df = pd.DataFrame(dato)
print(df, "\n")

print(df.loc[df[1] == 4])

s1 = pd.Series([1, 4, 3, 4, 5])
print(s1)

df = df.append(s1, ignore_index = True)
print(df)

df1 =df.loc[1:]
print(df1)
