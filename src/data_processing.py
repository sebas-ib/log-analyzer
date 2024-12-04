import pandas as pd


def parse_data(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    header = []
    data_rows = []
    reading_header = True

    for line in lines:
        clean_line = line.strip()
        if not clean_line:
            continue

        if reading_header:
            if clean_line.startswith('"'):
                fields = clean_line.split(',')
                cleaned_header = []

                for field in fields:
                    # Strip any leading whitespace and remove double quotes from each field
                    cleaned_field = field.strip().replace('"', '')
                    cleaned_header.append(cleaned_field)

                header = cleaned_header
            else:
                reading_header = False

        if not reading_header:
            row = clean_line.split(',')
            data_rows.append(row)

    # Convert data to DataFrame
    dataframe = _log_to_df(header, data_rows)

    # Apply transformation to the 3rd column
    dataframe.iloc[:, 2] = dataframe.iloc[:, 2].apply(_min_to_sec_format)
    dataframe.rename(columns={'ElapsedTime|Min|0.0|0.0|10': 'ElapsedTime|Sec|0.0|0.0|10'}, inplace=True)
    dataframe = dataframe.apply(pd.to_numeric, errors='coerce')

    return dataframe


def clean_df(data):
    data.columns = _clean_header(data.columns)
    data = data.dropna()
    return data


def _clean_header(header):
    cleaned_header = []

    for col in header:
        parts = col.split('|')

        if len(parts) > 1:
            cleaned_column = f"{parts[0]} ({parts[1]})"
        else:
            cleaned_column = parts[0]

        cleaned_header.append(cleaned_column)

    return cleaned_header


def _log_to_df(header, data_rows):
    data_rows_df = pd.DataFrame(data_rows)
    data_rows_df.columns = header
    return data_rows_df


def _min_to_sec_format(minutes):
    seconds = round(float(minutes) * 60, 0)
    return str(seconds)
