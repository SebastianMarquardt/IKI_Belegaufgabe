import sys
from sys import argv

from extraction import get_and_save_data
from probability_calc import calculate_all_probability_tables
from modelling import evaluate_model
from modelling_simple import evaluate_model_simple
from visuals import visualise_prop_tables, visualise_eval

default_config = {
    'symbol': '',
    'interval': '1d',
    'train_start': '2020-01-01',
    'train_end': '2021-12-31',
    'val_start': '2022-01-01',
    'val_end': '2022-12-31',
    'save_csv': False,
    'show_plots': False,
    'save_plots': True
}


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


def complex_model(symbol: str, interval: str, train_start: str, train_end: str, val_start: str, val_end: str,
                  save_csv: bool, show_plots: bool, save_plots: bool):
    training_data = get_and_save_data(symbol, interval=interval, start=train_start, end=train_end, save_to_csv=save_csv)
    val_data = get_and_save_data(symbol, interval=interval, start=val_start, end=val_end, save_to_csv=save_csv)
    open_train, close_train = calculate_all_probability_tables(training_data, use_complex_model=True)
    if save_csv:
        open_train.to_csv(f"output/cpd_opening_price_{symbol}_{train_start}{train_end}.csv")
        close_train.to_csv(f"output/cpd_closing_price_{symbol}_{train_start}{train_end}.csv")
    visualise_prop_tables([open_train, close_train], [f'Distribution Table for Opening Data {symbol}',
                                                      f'Distribution Table for Close Data {symbol}'],
                          show_chart=show_plots, save_charts=save_plots)
    pred_eval = evaluate_model(val_data, [open_train, close_train])
    visualise_eval(pred_eval, f'Distribution of correct&wrong predictions for {symbol})',
                   show_charts=show_plots, save_chart=save_plots)


"""
    Program Entry Point. This starts the Process of gathering & processing
"""
if __name__ == '__main__':
    if '-examples' in argv:
        btc_example()
        spx_example()
    else:
        conf = default_config.copy()
        for arg in argv:
            if arg == '-h':
                print('Usage help:')
                sys.exit()
            elif arg == '-s':
                conf.symbol = arg
            elif arg == '-i':
                conf.interval = arg
            elif arg == '-ts':
                conf.train_start = arg
            elif arg == '-te':
                conf.train_end = arg
            elif arg == '-vs':
                conf.val_start = arg
            elif arg == '-ve':
                conf.val_end = arg
            elif arg == '-scsv':
                conf.save_csv = arg
            elif arg == '-showp':
                conf.show_plots = arg
            elif arg == '-savep':
                conf.save_plots = arg
        complex_model(conf.get('symbol'), conf.get('interval'), conf.get('train_start'),
                      conf.get('train_end'), conf.get('val_start'), conf.get('val_end'),
                      conf.get('save_csv'), conf.get('show_plots'), conf.get('save_plots'))
