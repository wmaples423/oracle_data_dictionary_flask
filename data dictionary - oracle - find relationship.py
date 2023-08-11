import polars as pl

df = pl.read_csv("C:\\Users\\MaplesWi\\OneDrive - Clayton Homes\\Desktop\\oracle_data_dictionary.csv")

table_1 = input("Enter your first table name: ")
table_2 = input("Enter your second table name: ")

if table_1 and table_2:
    filtered_df = df.filter(pl.col("RELATIONSHIPS").str.contains(table_1))

    # Filter the resulting dataframe to only include rows where table_2 is in the RELATIONSHIPS column
    filtered_df = filtered_df.filter(pl.col("RELATIONSHIPS").str.contains(table_2))

    # Get the list of matching column names
    matching_columns = set(filtered_df["COLUMN_NAME"].to_list())

    if matching_columns:
        print(f"Matching columns for {table_1} and {table_2}:")
        for column in matching_columns:
            print(column)
    else:
        print("No matching columns found.")
