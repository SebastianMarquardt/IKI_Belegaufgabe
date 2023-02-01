import matplotlib.pyplot as plt
import pandas as pd


def visualise_prop_tables(tables: list[pd.DataFrame], titles: list[str]):
    for ind, tab in enumerate(tables):
        tab['abs_up'] = tab['up'] * tab['total']
        tab['abs_down'] = tab['down'] * tab['total']
        tab['label'] = tab[['PrevDayOpen', 'PrevDayClose', 'PrevDayHigh', 'PrevDayLow']].agg('-'.join, axis=1)
        tab.plot.bar(x='label',
                     y=['abs_up', 'abs_down'],
                     stacked=True,
                     color={"abs_up": "green", "abs_down": "red"})
        plt.legend(['up', 'down'])
        plt.title(titles[ind])
        plt.xlabel('Movement (Open, Close, High, Low)')
        plt.ylabel('Total')
    plt.show()
