import pandas as pd
from traceback import format_exc


def main():
    try:
        dfs = pd.read_html('https://en.wikipedia.org/wiki/List_of_Mayday_episodes')
        dfs[0].to_csv('mayday.csv')
    except Exception as exc:
        text = '\n\n'.join((str(exc), format_exc()))
        open('exception.txt', 'w').write(text)


if __name__ == '__main__':
    main()
