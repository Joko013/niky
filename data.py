
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load data from an excel file given by a path."""
    return pd.read_excel(path)


def add_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Add a new column filled with zeroes."""
    df[column_name] = 0
    return df


def save_to_excel(df: pd.DataFrame):
    df.to_excel('data/vystup.xlsx', index=False)


def update_counts(df: pd.DataFrame) -> pd.DataFrame:
    """Update Count column values for new `vz` columns."""
    vz_rows = df[df.columns[7:]]  # take all the values except the first 6 descriptive columns
    for i, r in df.iterrows():
        cnt = 0
        vz_row = vz_rows.iloc[i]
        for vz in vz_row.values:
            if vz:  # if there is any value in the current cell, add 1 to Count
                cnt += 1

        df.at[i, 'Count'] = cnt

    return df
