import pandas as pd

# TODO functionality


def calculate_all_probability_tables(data: pd.DataFrame, endNode: str):
    # creating a new DataFrame for the probability tables with labelled rows and columns
    # TODO not sure this index makes sense, we loose info on what is what and don't stay genera
    #  Instead keep column names open, close, high, low
    index_columns = ['PrevDayUpUp', 'PrevDayUpDown', 'PrevDayDownUp', 'PrevDayDownDown']
    prop_table = pd.DataFrame(calculate_probability_data(data, endNode), index=index_columns)
    prop_table['total'] = prop_table.sum(axis=1)

    for col in prop_table.columns:
        prop_table[col] = prop_table[col]/prop_table['total']

    return prop_table.drop(columns=['total'])


def calculate_probability_data(data: pd.DataFrame, target_col: str):
    # TODO this function only makes sense for the assumptions of 'trend_open' -> either more general or more functions
    # labels for columns
    first_column_name = "up"
    second_column_name = "down"

    # table used to fill the DataFrame later
    prop_data = {
        first_column_name: [0, 0, 0, 0],
        second_column_name: [0, 0, 0, 0]
    }

    for ind in range(len(data.index) - 1):
        # if prev day was open up and close up
        if data['trend_open'][ind] == 'up' and data['trend_close'][ind] == 'up':
            # check if next day was open up or close up, depending on mode
            if data[target_col][ind + 1] == 'up':
                # add 1 to the right point of the prop data
                prop_data[first_column_name][0] = prop_data[first_column_name][0] + 1
            else:
                prop_data[second_column_name][0] = prop_data[second_column_name][0] + 1
        if data['trend_open'][ind] == 'up' and data['trend_close'][ind] == 'down':
            if data[target_col][ind + 1] == 'up':
                prop_data[first_column_name][1] = prop_data[first_column_name][1] + 1
            else:
                prop_data[second_column_name][1] = prop_data[second_column_name][1] + 1
        if data['trend_open'][ind] == 'down' and data['trend_close'][ind] == 'up':
            if data[target_col][ind + 1] == 'up':
                prop_data[first_column_name][2] = prop_data[first_column_name][2] + 1
            else:
                prop_data[second_column_name][2] = prop_data[second_column_name][2] + 1
        if data['trend_open'][ind] == 'down' and data['trend_close'][ind] == 'down':
            if data[target_col][ind + 1] == 'up':
                prop_data[first_column_name][3] = prop_data[first_column_name][3] + 1
            else:
                prop_data[second_column_name][3] = prop_data[second_column_name][3] + 1

    return prop_data


def calculate_probability_table_for_col(col):
    # Open: Depends on Previous Open and Previous Close
    # Close: Depends on Previous Close and Current Open
    raise NotImplementedError
