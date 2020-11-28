from traceback import format_exc
from pandas import read_html


def main():
    exception_text = ''

    try:
        read_html('https://en.wikipedia.org/wiki/List_of_Mayday_episodes')[0].to_csv('mayday.csv')
    except Exception as exc:
        exception_text = '\n\n'.join((str(exc), format_exc()))

    open('exception.txt', 'w').write(exception_text)


if __name__ == '__main__':
    main()
