import pandas as pd


def download_list_of_mayday_episodes() -> None:
    pd.read_html('https://en.wikipedia.org/wiki/List_of_Mayday_episodes')[0].to_csv('data/mayday.csv')


if __name__ == '__main__':
    download_list_of_mayday_episodes()
