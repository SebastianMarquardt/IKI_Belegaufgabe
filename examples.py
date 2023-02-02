from IKI_Belegaufgabe.extraction import get_and_save_data
from IKI_Belegaufgabe.modelling import evaluate_model
from IKI_Belegaufgabe.probability_calc import calculate_all_probability_tables
from IKI_Belegaufgabe.visuals import visualise_prop_tables, visualise_eval


def spx_example():
    spx500_2020_21 = get_and_save_data("^GSPC", interval='1d', start='2020-01-01', end='2021-12-31')
    spx500_2022 = get_and_save_data("^GSPC", interval='1d', start='2022-01-01', end='2022-12-31')
    open_2years, close_2years = calculate_all_probability_tables(spx500_2020_21, True)
    open_2years.to_csv(f"output/cpd_opening_price_spx500_2020_21.csv")
    close_2years.to_csv(f"output/cpd_closing_price_spx500_2020_21.csv")
    visualise_prop_tables([open_2years, close_2years], ['Distribution Table for Opening Data SPX 500',
                                                        'Distribution Table for Close Data SPX 500'])
    pred_eval = evaluate_model(spx500_2022, [open_2years, close_2years])
    visualise_eval(pred_eval, 'Distribution of correct&wrong predictions for SPX500 in 2022 (trained on 2020 & 2022)',
                   True)


def btc_example():
    btc_2020_21 = get_and_save_data("BTC-USD", interval='1d', start='2020-01-01', end='2021-12-31')
    btc_2022 = get_and_save_data("BTC-USD", interval='1d', start='2022-01-01', end='2022-12-31')

    open_2years, close_2years = calculate_all_probability_tables(btc_2020_21, True)
    open_2years.to_csv(f"output/cpd_opening_price_btc_2020_21.csv")
    close_2years.to_csv(f"output/cpd_closing_price_btc_2020_21.csv")
    visualise_prop_tables([open_2years, close_2years], ['Distribution Table for Opening Data BTC',
                                                        'Distribution Table for Close Data BTC'])
    pred_eval = evaluate_model(btc_2022, [open_2years, close_2years])
    visualise_eval(pred_eval, 'Distribution of correct&wrong predictions for BTC in 2022 (trained on 2020 & 2022)',
                   True)
