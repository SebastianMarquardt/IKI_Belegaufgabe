from extraction import get_and_save_data
from probability_calc import calculate_all_probability_tables
from modelling import evaluate_model
"""
    Program Entry Point. This starts the Process of gathering & processing
"""
if __name__ == '__main__':
    # Can replace ticker, interval and period here, otherwise use standard values (^GSPC=SPX500)
    # Cleans Data, saves it to CSV and saves into cleanedData Variable
    spx500_2020_21 = get_and_save_data("^GSPC", interval='1d', start='2020-01-01', end='2021-12-31')
    spx500_2021 = get_and_save_data("^GSPC", interval='1d', start='2021-01-01', end='2021-12-31')
    spx500_2022 = get_and_save_data("^GSPC", interval='1d', start='2022-01-01', end='2022-12-31')

    # TODO should calculate and return all Probability Tables
    open_2years, close_2years = calculate_all_probability_tables(spx500_2020_21, True)
    open_1years, close_1years = calculate_all_probability_tables(spx500_2021, True)
    open_preds, close_preds = evaluate_model(spx500_2022, [open_1years, close_1years])
    print(open_preds)
    print(close_preds)





