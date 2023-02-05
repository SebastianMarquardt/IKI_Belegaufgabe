import distutils.util
import sys
from sys import argv
from extraction import get_and_save_data
from probability_calc import calculate_all_probability_tables
from modelling import evaluate_model
from modelling_simple import evaluate_model_simple
from visuals import visualise_prop_tables, visualise_eval
from constants import DEFAULT_RUN_CONFIG
from examples import btc_example, spx_example
import argparse


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
    if '-examples.py' in argv:
        btc_example()
        spx_example()
    else:
        conf = DEFAULT_RUN_CONFIG.copy()
        parser = argparse.ArgumentParser()
        parser.add_argument("-s", "--symbol", help="Symbol as used in Yahoo-finance-API)", required=True)
        parser.add_argument("-i", "--interval",
                            help="Interval e.g. 1d|1w (For fomats check the yfinance documentation)")
        parser.add_argument("-ts", "--train-start", help="Format YYYY-MM-DD")
        parser.add_argument("-te", "--train_end", help="Format YYYY-MM-DD")
        parser.add_argument("-vs", "--val_start", help="Format YYYY-MM-DD")
        parser.add_argument("-ve", "--val_end", help="Format YYYY-MM-DD")
        parser.add_argument("--save-csv", help="If true saves all csv files to the output folder", type=lambda x:bool(distutils.util.strtobool(x)))
        parser.add_argument("--show-plots", help="If true, shows the created charts during runtime", type=lambda x:bool(distutils.util.strtobool(x)))
        parser.add_argument("--save-plots", help="If true, save the charts to PNG ", type=lambda x:bool(distutils.util.strtobool(x)))
        args = vars(parser.parse_args())
        for arg in args:
            if args[arg] is None:
                continue
            else:
                conf[arg] = args[arg]
        complex_model(conf.get('symbol'), conf.get('interval'), conf.get('train_start'),
                      conf.get('train_end'), conf.get('val_start'), conf.get('val_end'),
                      conf.get('save_csv'), conf.get('show_plots'), conf.get('save_plots'))
