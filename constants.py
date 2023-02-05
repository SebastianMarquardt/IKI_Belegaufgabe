DEFAULT_RUN_CONFIG = {
    'symbol': '',
    'interval': '1d',
    'train_start': '2020-01-01',
    'train_end': '2021-12-31',
    'val_start': '2022-01-01',
    'val_end': '2022-12-31',
    'save_csv': False,
    'show_plots': False,
    'save_plots': False
}

HELP = """Usage help:
    Run examples.py: 
        main.py -examples.py (run example for BTC and SPX500)
    When running without any arguments the following default config will be loaded:
        {'symbol': '^GSPC',
        'interval': '1d',
        'train_start': '2020-01-01',
        'train_end': '2021-12-31',
        'val_start': '2022-01-01',
        'val_end': '2022-12-31',
        'save_csv': False,
        'show_plots': False,
        'save_plots': True}
    The values in the config can be overwritten with the following flags (ones not set will be taken from default config)
        -s      <Symbol> (as used in Yahoo-finance-API)
        -i      <Interval> (For fomats check the yfinance documentation)
        -ts     <train_start> (Format YYYY-MM-DD)
        -te     <train_end> (Format YYYY-MM-DD)
        -vs     <validation_start> (Format YYYY-MM-DD)
        -ve     <validation_end> (Format YYYY-MM-DD)
        -scsv   <True|False>
        -showp  <True|False>
        -savep  <True|False>
    To show his explanation:
        -h
"""