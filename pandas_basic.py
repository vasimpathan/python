import pandas as pd
# People: P1, P2, P3
# Age: 20, 30, 40

d = {'People': ['P1', 'P2', 'P3'], 'Age': [20, 30, 40]}

df = pd.DataFrame(d)

# pd.read_excel("score_updated.xlsx")
# pd.read_csv("sample.csv")
print(df)