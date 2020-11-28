from traceback import format_exc
from pandas import read_html


def main():
    exception_text = ''

    try:
        read_html('https://en.wikipedia.org/wiki/List_of_Mayday_episodes')[0].to_csv('data/mayday.csv')
    except Exception as exc:
        exception_text = '\n\n'.join((str(exc), format_exc()))

    open('exceptions/task_mayday.txt', 'w').write(exception_text)


if __name__ == '__main__':
    main()
