import pandas as pd

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

def evaluate_model(validation_data: pd.DataFrame, probability_table: pd.DataFrame, complex: bool, target: str):
    if complex:
        evaluate_model_complex(validation_data, probability_table, target)
    else:
        evaluate_model_simple(validation_data, probability_table, target)

def evaluate_model_complex(validation_data: pd.DataFrame, probability_table: pd.DataFrame, target: str):
    validation_table = pd.DataFrame(columns=['open','close','high','low','prediction_'+target,'is_true'])
    validation_table['open'] = validation_data['trend_open']
    validation_table['close'] = validation_data['trend_close']
    validation_table['high'] = validation_data['trend_high']
    validation_table['low'] = validation_data['trend_low']
    
    for ind in range(len(validation_table.index) - 1):
        update_prediction(validation_table, ind, probability_table, target, validation_data)

    print(validation_table)

def update_prediction(validation_table, ind, probability_table, target, validation_data):
    for x in range(16): 
        if validation_table['open'][ind] == complex_format[x][0] and validation_table['close'][ind] == complex_format[x][1] and validation_table['high'][ind] == complex_format[x][2] and validation_table['low'][ind] == complex_format[x][3]:
            if probability_table['up'][x] >= 0.5:
                validation_table['prediction_'+target][ind] = 'up'
                if validation_data['trend_open'][ind + 1] == 'up':
                    validation_table['is_true'][ind] = True
            else:
                validation_table['prediction_'+target][ind] = 'down'
                if validation_data['trend_open'][ind + 1] == 'up':
                    validation_table['is_true'][ind] = False

def evaluate_model_simple(validation_data: pd.DataFrame, probability_table: pd.DataFrame, target: str):
    validation_table = pd.DataFrame(columns=['open','close','prediction_'+target,'is_true'])
    validation_table['open'] = validation_data['trend_open']
    validation_table['close'] = validation_data['trend_close']

def use_model(data: pd.DataFrame, probability_tables: list[pd.DataFrame]):
    # Make Predictions based on Probability Tables and given data
    raise NotImplementedError
