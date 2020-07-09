import pandas as pd

ppp_df = pd.read_csv("data/foia_150k_plus.csv", index_col='BusinessName')
wilshire_df = pd.read_csv("data/wilshire-5000.csv", index_col='Name')

wilshire_df.join(ppp_df, how='inner').to_csv("data/matched.csv")