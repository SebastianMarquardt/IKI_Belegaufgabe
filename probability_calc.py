import pandas as pd
pd.options.mode.chained_assignment = None

complex_format = [
    ['up', 'up', 'up', 'up', 0, 0],
    ['up', 'up', 'up', 'down', 0, 0],
    ['up', 'up', 'down', 'up', 0, 0],
    ['up', 'up', 'down', 'down', 0, 0],
    ['up', 'down', 'up', 'up', 0, 0],
    ['up', 'down', 'up', 'down', 0, 0],
    ['up', 'down', 'down', 'up', 0, 0],
    ['up', 'down', 'down', 'down', 0, 0],
    ['down', 'up', 'up', 'up', 0, 0],
    ['down', 'up', 'up', 'down', 0, 0],
    ['down', 'up', 'down', 'up', 0, 0],
    ['down', 'up', 'down', 'down', 0, 0],
    ['down', 'down', 'up', 'up', 0, 0],
    ['down', 'down', 'up', 'down', 0, 0],
    ['down', 'down', 'down', 'up', 0, 0],
    ['down', 'down', 'down', 'down', 0, 0]
]

def calculate_all_probability_tables(data: pd.DataFrame, complex: bool):

    prop_table_ope = pd.DataFrame
    prop_table_clo = pd.DataFrame
    if (complex):
        prop_table_ope, prop_table_clo = calculate_probability_complex(data)
        
        prop_table_ope['total'] = prop_table_ope['up']+prop_table_ope['down']
        prop_table_clo['total'] = prop_table_clo['up']+prop_table_clo['down']

        prop_table_ope['up'] = prop_table_ope['up']/prop_table_ope['total']
        prop_table_ope['down'] = prop_table_ope['down']/prop_table_ope['total']
        prop_table_clo['up'] = prop_table_clo['up']/prop_table_clo['total']
        prop_table_clo['down'] = prop_table_clo['down']/prop_table_clo['total']
        
        return prop_table_ope.drop(columns=['total']), prop_table_clo.drop(columns=['total'])
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

    prop_table_ope = build_table_complex()
    prop_table_clo = build_table_complex()

    build_data_complex(prop_table_ope, data, 'trend_open')
    build_data_complex(prop_table_clo, data, 'trend_close')

    return prop_table_ope, prop_table_clo

def build_data_complex(prop_table, data, target: str):
    for ind in range(len(data.index) - 1):
        update_entry(data, ind, target, prop_table)

def update_entry(data, ind, target, prop_table):
    for x in range(16): 
        if data['trend_open'][ind] == complex_format[x][0] and data['trend_close'][ind] == complex_format[x][1] and data['trend_high'][ind] == complex_format[x][2] and data['trend_low'][ind] == complex_format[x][3]:
            if data[target][ind + 1] == 'up':
                prop_table['up'][x] = prop_table['up'][x] + 1
            else:
                prop_table['down'][x] = prop_table['down'][x] + 1

def build_table_complex():
    prop_table = pd.DataFrame(complex_format, columns=['PrevDayOpen','PrevDayClose','PrevDayHigh','PrevDayLow','up','down'])

    return prop_table