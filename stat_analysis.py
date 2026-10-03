import sys
import sqlite3 as s3
import pandas as pd

# run using:  python stat_analysis.py data.db overview.csv

def load_db(db_file):
    # Connect to sqlite db
    connection = s3.connect(db_file)    

    # Load sqlite db into pandas df
    df = pd.read_sql_query("SELECT * FROM immune_cells", connection)
    connection.close()
    return df

def load_csv(csv_file):
    df = pd.read_csv(csv_file)
    return df


def main():
    csv_file = "cell-count.csv"
    if len(sys.argv) < 3:
        print("Usage: python stat_analysis.py <full db *.db> <overview *.csv>")
        return 1
    db_file = sys.argv[1]
    csv_file = sys.argv[2]

    # Load files
    db_df = load_db(db_file)
    overview_df = load_csv(csv_file)
    populations = ["b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"]

    # Organize desired data; pbmc samples of melanoma patients on miraclib treatment
    pbmc_only = db_df[db_df["sample_type"] == "PBMC"]
    miraclibs = pbmc_only[pbmc_only["treatment"] == "miraclib"]
    melanomas = miraclibs[miraclibs["condition"] == "melanoma"]
    sort_responses = melanomas.sort_values(["response"]).dropna(subset=["response"]) 

    # melted = compare_frequencies()
    # print(melted)

if __name__ == "__main__":
    sys.exit(main())