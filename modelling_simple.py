import pandas as pd


def evaluate_model_simple(validation_data: pd.DataFrame, probability_tables: list[pd.DataFrame]):
    for i in range(len(validation_data)-1):
        validation_data.loc[validation_data.index[i+1], 'pred_open'] = get_prediction(validation_data.iloc[i], probability_tables[0])
        validation_data.loc[validation_data.index[i+1], 'pred_close'] = get_prediction(validation_data.iloc[i], probability_tables[1])
    validation_data = validation_data.apply(check_predictions, axis=1)
    open_bool = validation_data['open_bool'].value_counts()
    close_bool = validation_data.close_bool.value_counts()
    bool_combination_count = validation_data[['open_bool', 'close_bool']].value_counts().reset_index(name='count')
    return bool_combination_count


def get_prediction(curr: pd.Series, prob_table: pd.DataFrame):
    pred = prob_table.loc[(prob_table['trend_open'] == curr['trend_open']) &
                          (prob_table['trend_close'] == curr['trend_close'])].reset_index()
    if pred.up[0] > pred.down[0]:
        return 'up'
    elif pred.down[0] > pred.up[0]:
        return 'down'


def check_predictions(row: pd.Series):
    if row['pred_open'] == row['trend_open']:
        row['open_bool'] = True
    else:
        row['open_bool'] = False

    if row['pred_close'] == row['trend_close']:
        row['close_bool'] = True
    else:
        row['close_bool'] = False
    return row
