import pandas


def find_match(row: pandas.Series, df: pandas.DataFrame) -> (int, str):
    """Find a matching row (if one exists) and return it's index."""
    for i, df_row in df.iterrows():
        matched = compare_rows(row, df_row)
        if matched:
            # if a match is found, return it's index and a remark
            remark = get_remark(row, df_row)
            return i, remark

    return None, None  # if no match is found


def compare_rows(a: pandas.Series, b: pandas.Series) -> bool:
    """Check if two rows `a` and `b` are the same substance."""
    if abs(a['Retention index'] - b['Retention index']) > 0.2:
        return False
    elif abs(a['2nd retention time'] - b['2nd retention time']) > 0.05:
        return False
    else:
        return True


def get_remark(a: pandas.Series, b: pandas.Series) -> str:
    if a['Spectrum'].split(':')[0] != b['Spectrum'].split(' ')[0]:
        if (
            a['Spectrum'].split(':')[0] == b['Spectrum'].split(' ')[1] and
            a['Spectrum'].split(':')[1] == b['Spectrum'].split(' ')[0]
        ):
            return 'yellow'
        else:
            return 'red'


def add_row_to_result(row: pandas.Series, df: pandas.DataFrame, origin: str, remark: str) -> pandas.DataFrame:
    """Add new row to a DataFrame and fill it with values."""
    id_ = f'M{len(df)+1}'
    cnt = 1
    ret_index = row['Retention index']
    sec_ret_time = row['2nd retention time']
    spectrum = get_spectrum(row)
    vz_values = get_vz_values(row, df)

    new_row = pandas.Series([id_, origin, cnt, ret_index, sec_ret_time, spectrum, remark, *vz_values], index=df.columns)
    df = df.append(new_row, ignore_index=True)
    return df


def fill_sample_value(row_index: int, df: pandas.DataFrame, column_name: str, value: int) -> pandas.DataFrame:
    """Fill a column_name column of a df Data Frame on a row given by row_index with a value."""
    df.at[row_index, column_name] = value
    return df


def get_spectrum(row: pandas.Series) -> str:
    """Parse spectrum value from the row['Spectrum'] field."""
    space_separated_vals = row['Spectrum'].split(' ')  # split the Spectrum values by space
    no_dot_vals = [item.replace('.', '') for item in space_separated_vals]  # delete trailing dots
    spectrum = [val.split(':') for val in no_dot_vals]  # split it once more by :
    str_spectrum = spectrum[0][0] + ' ' + spectrum[1][0]  # take the first element from each of the values
    return str_spectrum


def get_vz_values(row: pandas.Series, df: pandas.DataFrame) -> list:
    """Fill all previous `vz` columns with 0 and fill `Area` value into the current `vz` column."""
    len_ = len(df.columns) - 8  # get length of vz columns: 7 descriptive columns + 1 for the current `vz` column
    vz_values = [0] * len_
    vz_values.append(row['Area'])  # add the value of Area to the end of the values
    return vz_values
