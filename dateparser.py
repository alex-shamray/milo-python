import logging
import sys
from datetime import date

formatter = logging.Formatter('{pathname:s}:{lineno:d}:{levelname:s}: {message:s}', style='{')

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

root = logging.getLogger()
root.addHandler(handler)
root.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)

YEAR_FROM = 2000
YEAR_TO = 3000


def parse(d):
    l = list(map(int, d.split('/')))

    possible_orderings = [
        (l[0], l[1], l[2]),  # Y/m/d
        (l[2], l[1], l[0]),  # d/m/Y
        (l[2], l[0], l[1]),  # m/d/Y
        # Exotic formats
        (l[0], l[2], l[1]),  # Y/d/m
        (l[1], l[0], l[2]),  # m/Y/d
        (l[1], l[2], l[0]),  # d/Y/m
    ]
    for data in possible_orderings:
        year, month, day = data
        if year + YEAR_FROM < YEAR_TO:
            year = year + YEAR_FROM
        try:
            return date(year, month, day).strftime('%Y-%m-%d')
        except ValueError as e:
            logger.debug(e)
    return '{} is illegal'.format(d)


def main():
    with open('data.txt') as f:
        data = f.readline()

    print(parse(data))


if __name__ == '__main__':
    main()
