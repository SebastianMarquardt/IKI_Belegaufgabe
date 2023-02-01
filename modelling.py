import pandas as pd


def evaluate_model(validation_data: pd.DataFrame, probability_tables: list[pd.DataFrame]) -> pd.DataFrame:
    # Make predictions, compare to actual values and return Evaluation Data
    probability_tables = rename_prop_tables(tabs=probability_tables)
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
                          (prob_table['trend_close'] == curr['trend_close']) &
                          (prob_table['trend_high'] == curr['trend_high']) &
                          (prob_table['trend_low'] == curr['trend_low'])].reset_index()
    if pred.up[0] > pred.down[0]:
        return 'up'
    elif pred.down[0] > pred.up[0]:
        return 'down'


def rename_prop_tables(tabs: list[pd.DataFrame]):
    for tab in tabs:
        tab.rename(columns={'PrevDayOpen': 'trend_open', 'PrevDayClose': 'trend_close',
                            'PrevDayHigh': 'trend_high', 'PrevDayLow': 'trend_low'}, inplace=True)
    return tabs


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

