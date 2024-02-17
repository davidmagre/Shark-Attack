def duplicates_elim(df):
    rows_without_duplicates = df.drop_duplicates()
    columns_without_duplicates = rows_without_duplicates.transpose().drop_duplicates().transpose()
    return columns_without_duplicates