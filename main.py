from extraction import get_and_save_data
from probability_calc import calculate_all_probability_tables
from modelling import evaluate_model
from visuals import visualise_prop_tables


def spx_example():
    spx500_2020_21 = get_and_save_data("^GSPC", interval='1d', start='2020-01-01', end='2021-12-31')
    spx500_2022 = get_and_save_data("^GSPC", interval='1d', start='2022-01-01', end='2022-12-31')

    open_2years, close_2years = calculate_all_probability_tables(spx500_2020_21, True)
    open_2years.to_csv(f"cpd_opening_price_spx500_2020_21.csv")
    close_2years.to_csv(f"cpd_closing_price_spx500_2020_21.csv")
    visualise_prop_tables([open_2years, close_2years], ['Distribution Table for Opening Data SPX 500',
                                                        'Distribution Table for Close Data SPX 500'])
    open_preds, close_preds = evaluate_model(spx500_2022, [open_2years, close_2years])


def btc_example():
    spx500_2020_21 = get_and_save_data("BTC-USD", interval='1d', start='2020-01-01', end='2021-12-31')
    spx500_2022 = get_and_save_data("BTC-USD", interval='1d', start='2022-01-01', end='2022-12-31')

    open_2years, close_2years = calculate_all_probability_tables(spx500_2020_21, True)
    open_2years.to_csv(f"cpd_opening_price_btc_2020_21.csv")
    close_2years.to_csv(f"cpd_closing_price_btc_2020_21.csv")
    visualise_prop_tables([open_2years, close_2years], ['Distribution Table for Opening Data BTC',
                                                        'Distribution Table for Close Data BTC'])
    open_preds, close_preds = evaluate_model(spx500_2022, [open_2years, close_2years])


"""
    Program Entry Point. This starts the Process of gathering & processing
"""
if __name__ == '__main__':
    spx_example()
    btc_example()




