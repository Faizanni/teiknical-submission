import sqlite3 as s3
import pandas as pd

input_csv = "cell-count.csv"
output_db = "data.db"
tb = "immune_cells"

# # connect to .db
df = pd.read_csv(input_csv)
connection = s3.connect(output_db)

# convert pandas df to sql db w/ table name "immune-cells"
df.to_sql(tb, connection, if_exists="replace")
# csr = connection.cursor()