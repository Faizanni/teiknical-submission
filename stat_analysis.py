import sys
import sqlite3 as s3
import pandas as pd

def load_csv(db_file):
    # Connect to sqlite db
    # connection = s3.connect(db_file)    

    # # Load sqlite db into pandas df
    # df = pd.read_sql_query("SELECT * FROM immune_cells", connection)
    # connection.close()
    df = pd.read_csv(db_file)
    return df


def main():
    csv_file = "cell-count.csv"
    if len(sys.argv) < 2:
        print("Usage: python stat_analysis.py <overview *.db>")
        return 1
    db_file = sys.argv[1]

    overview_df = load_csv(db_file)

    print(overview_df)

if __name__ == "__main__":
    sys.exit(main())