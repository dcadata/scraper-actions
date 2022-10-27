import pandas as pd


def download_governor_polls() -> None:
    df = pd.read_csv('https://projects.fivethirtyeight.com/polls/data/governor_polls.csv')
    df = df[
        (df.cycle == 2022) & (df.election_date == '11/8/22') & df.start_date.str.endswith('/22')
        & (df.stage == 'general') & (df.state == 'Michigan') & (df.answer == 'Dixon')
        ]
    df.to_csv('data/governor_polls.filtered.csv', index=False)


def download_list_of_mayday_episodes() -> None:
    pd.read_html('https://en.wikipedia.org/wiki/List_of_Mayday_episodes')[0].to_csv('data/mayday.csv')


if __name__ == '__main__':
    download_governor_polls()
