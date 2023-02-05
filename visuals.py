import matplotlib.pyplot as plt
import pandas as pd


def visualise_prop_tables(tables: list[pd.DataFrame], titles: list[str], save_charts: bool = True,
                          show_chart: bool = True):
    for ind, tab in enumerate(tables):
        tab['abs_up'] = tab['up'] * tab['total']
        tab['abs_down'] = tab['down'] * tab['total']
        tab['label'] = tab[['PrevDayOpen', 'PrevDayClose', 'PrevDayHigh', 'PrevDayLow']].agg('-'.join, axis=1)
        ax = tab.plot.bar(x='label',
                          y=['abs_up', 'abs_down'],
                          stacked=True,
                          color={"abs_up": "green", "abs_down": "red"}, )
        for container in ax.containers:
            ax.bar_label(container)
        plt.legend(['up', 'down'])
        plt.title(titles[ind])
        plt.xticks(rotation=30, horizontalalignment='right')
        plt.xlabel('Movement (Open, Close, High, Low)')
        plt.ylabel('Total')
        plt.tight_layout()
        if save_charts:
            plt.savefig(f"output/{titles[ind].replace(' ', '')}.png")
    if show_chart:
        plt.show()

def visualise_prop_tables_simple(tables: list[pd.DataFrame], titles: list[str], save_charts: bool = True,
                          show_chart: bool = True):
    for ind, tab in enumerate(tables):
        tab['abs_up'] = tab['up'] * tab['total']
        tab['abs_down'] = tab['down'] * tab['total']
        tab['label'] = tab[['trend_open', 'trend_close']].agg('-'.join, axis=1)
        ax = tab.plot.bar(x='label',
                          y=['abs_up', 'abs_down'],
                          stacked=True,
                          color={"abs_up": "green", "abs_down": "red"}, )
        for container in ax.containers:
            ax.bar_label(container)
        plt.legend(['up', 'down'])
        plt.title(titles[ind])
        plt.xticks(rotation=30, horizontalalignment='right')
        plt.xlabel('Movement (Open, Close)')
        plt.ylabel('Total')
        plt.tight_layout()
        if save_charts:
            plt.savefig(f"output/simple_{titles[ind].replace(' ', '')}.png")
    if show_chart:
        plt.show()

def visualise_eval(table: pd.DataFrame, title: str, save_chart: bool = True, show_charts=True):
    table['label'] = table['open_bool'].astype(str) + '-' + table['close_bool'].astype(str)
    ax = table.plot.bar(x='label',
                        y='count')
    ax.bar_label(ax.containers[0])
    plt.xticks(rotation=0)
    plt.title(title, wrap=True)
    plt.xlabel('Correct (Open-Close)')
    plt.ylabel('Total')
    if save_chart:
        plt.savefig(f"output/{title.replace(' ', '')}.png")
    if show_charts:
        plt.show()


def visualise_eval_simple(table: pd.DataFrame, title: str, save_chart: bool = True, show_charts=True):
    table['label'] = table['open_bool'].astype(str) + '-' + table['close_bool'].astype(str)
    ax = table.plot.bar(x='label',
                        y='count')
    ax.bar_label(ax.containers[0])
    plt.xticks(rotation=0)
    plt.title(title, wrap=True)
    plt.xlabel('Correct (Open-Close)')
    plt.ylabel('Total')
    if save_chart:
        plt.savefig(f"output/simple_{title.replace(' ', '')}.png")
    if show_charts:
        plt.show()