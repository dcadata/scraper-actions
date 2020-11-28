import pandas as pd


def main():
    dfs = pd.read_html('https://en.wikipedia.org/wiki/List_of_Mayday_episodes')
    dfs[0].to_csv('mayday.csv')


if __name__ == '__main__':
    main()
