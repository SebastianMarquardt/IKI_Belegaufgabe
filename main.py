from extraction import get_and_save_data
from probability_calc import calculate_all_probability_tables

"""
    Program Entry Point. This starts the Process of gathering & processing
"""
if __name__ == '__main__':
    # Can replace ticker, interval and period here, otherwise use standard values (^GSPC=SPX500)
    # Cleans Data, saves it to CSV and saves into cleanedData Variable
    cleanedData = get_and_save_data("^GSPC", interval='1d')

    # TODO should calculate and return all Probability Tables
    calculate_all_probability_tables(cleanedData, 'trend_open')





