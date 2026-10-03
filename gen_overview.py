import sys

import sqlite3 as s3
import pandas as pd

# run w/ python gen_overview.py data.db out.csv
def main():
    csv_file = "cell-count.csv"
    if len(sys.argv) < 3:
        print("Usage: python gen_overview.py <input *.db> <output filename *.csv>")
        return 1
    db_file = sys.argv[1]
    out_file = sys.argv[2]

    # Connect to sqlite db
    connection = s3.connect(db_file)    

    # Load sqlite db into pandas df
    df = pd.read_sql_query("SELECT * FROM immune_cells", connection)
    connection.close()

    # Get total_count of each cell population
    populations = ["b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"]
    df["total_count"] = df[populations].sum(axis=1)

    # generate summary table; 5 rows per sample 
    # sample x5 | total_count | population | count | percentage
    
    # NOT MINE; suggested by Claude; 
    # Converts table from wide -> tall; essentially isolates pops cols, then transposes
    # sample & total_count cols
    overview_df = df.melt(
                        id_vars=["sample", "total_count"],
                        value_vars=populations,
                        var_name="population",
                        value_name="count",
                    )

    # Calculate percentages per immune cell type
    overview_df["percentage"] = (overview_df["count"] / overview_df["total_count"]) * 100
    sorted_overview_df = overview_df.sort_values(["sample", "population"])

    # Print summary table to filename arg
    with open(out_file, 'w') as f:
        f.write(sorted_overview_df.to_csv(index=False))

if __name__ == "__main__":
    sys.exit(main())
