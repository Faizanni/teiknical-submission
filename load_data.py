import sqlite3 as s3
import pandas as pd

# connect to .db
df = pd.read_csv("cell-count.csv")
cnct = s3.connect('data.db')
df.to_sql("immune_cells", cnct, if_exists="replace")
# csr = cnct.cursor()