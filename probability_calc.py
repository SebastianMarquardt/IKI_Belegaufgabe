import pandas as pd

def calculate_all_probability_tables(data: pd.DataFrame, complex: bool):

    prop_table_ope = pd.DataFrame
    prop_table_clo = pd.DataFrame
    if (complex):
        prop_table_ope, prop_table_clo = calculate_probability_complex(data)
    else:
        prop_table_ope, prop_table_clo = calculate_probability_simple(data)

    prop_table_ope['total'] = prop_table_ope.sum(axis=1)
    prop_table_clo['total'] = prop_table_clo.sum(axis=1)

    for col in prop_table_ope.columns:
        prop_table_ope[col] = prop_table_ope[col]/prop_table_ope['total']

    for col in prop_table_clo.columns:
        prop_table_clo[col] = prop_table_clo[col]/prop_table_clo['total']

    return prop_table_ope.drop(columns=['total']), prop_table_clo.drop(columns=['total'])

def calculate_probability_simple(data: pd.DataFrame):

    index_columns = ['PrevDayUpUp', 'PrevDayUpDown', 'PrevDayDownUp', 'PrevDayDownDown']
    prop_table_ope = pd.DataFrame(build_data_simple(data, 'trend_open'), index=index_columns)
    prop_table_clo = pd.DataFrame(build_data_simple(data, 'trend_close'), index=index_columns)
    return prop_table_ope, prop_table_clo

def build_data_simple(data: pd.DataFrame, target: str):

    first_column_name = "up"
    second_column_name = "down"

    prop_data = {
        first_column_name: [0, 0, 0, 0],
        second_column_name: [0, 0, 0, 0]
    }

    for ind in range(len(data.index) - 1):
        # if prev day was open up and close up
        if data['trend_open'][ind] == 'up' and data['trend_close'][ind] == 'up':
            # check if next day was open up or close up, depending on mode
            if data[target][ind + 1] == 'up':
                # add 1 to the right point of the prop data
                prop_data[first_column_name][0] = prop_data[first_column_name][0] + 1
            else:
                prop_data[second_column_name][0] = prop_data[second_column_name][0] + 1
        if data['trend_open'][ind] == 'up' and data['trend_close'][ind] == 'down':
            if data[target][ind + 1] == 'up':
                prop_data[first_column_name][1] = prop_data[first_column_name][1] + 1
            else:
                prop_data[second_column_name][1] = prop_data[second_column_name][1] + 1
        if data['trend_open'][ind] == 'down' and data['trend_close'][ind] == 'up':
            if data[target][ind + 1] == 'up':
                prop_data[first_column_name][2] = prop_data[first_column_name][2] + 1
            else:
                prop_data[second_column_name][2] = prop_data[second_column_name][2] + 1
        if data['trend_open'][ind] == 'down' and data['trend_close'][ind] == 'down':
            if data[target][ind + 1] == 'up':
                prop_data[first_column_name][3] = prop_data[first_column_name][3] + 1
            else:
                prop_data[second_column_name][3] = prop_data[second_column_name][3] + 1

    return prop_data

def calculate_probability_complex(data):
    raise NotImplementedError
