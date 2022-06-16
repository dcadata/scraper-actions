from pandas import read_html

if __name__ == '__main__':
    read_html('https://en.wikipedia.org/wiki/List_of_Mayday_episodes')[0].to_csv('data/mayday.csv')
