import sqlite3 as s3
import pandas as pd

csv_file = "cell-count.csv"
db_file = "data.db"
tb_name = "immune_cells"

# # connect to .db
df = pd.read_csv(csv_file)
connection = s3.connect(db_file)

# convert pandas df to sql db w/ table name "immune-cells"
df.to_sql(tb_name, connection, if_exists="replace")
connection.close()
# csr = connection.cursor()