
import argparse

from data import load_data, add_column, save_to_excel, update_counts
from rows import find_match, add_row_to_result, fill_sample_value


def process_file(name: str):
    """Process a file - load data, add new column, check for matches, fill in values, add rows, export to excel."""
    out_data = add_column(df=load_data('data/vystup.xlsx'), column_name=name)
    in_data = load_data(f'data/{name}.xlsx')

    for i, in_row in in_data.iterrows():
        match_index, remark = find_match(row=in_row, df=out_data)
        if match_index is not None and remark is None:
            out_data = fill_sample_value(
                row_index=match_index,
                df=out_data,
                column_name=name,
                value=in_row['Area']
            )
        else:
            out_data = add_row_to_result(row=in_row, df=out_data, origin=name, remark=remark)

    out_data = update_counts(out_data)
    save_to_excel(out_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file_name',
        type=str,
        help='name of the file to be processed located in the data folder'
    )
    args = parser.parse_args()

    file_name = args.file_name.lower()
    process_file(file_name)
