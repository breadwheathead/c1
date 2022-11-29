import sys


def show_sales(args):
    result = ''
    with open('bakery.csv', 'r', encoding='utf-8') as file:
        if len(args) == 0:
            result = file.read()
        elif len(args) == 1 and args[0].isdigit():
            file.seek((int(args[0]) * 12) - 12)
            result = file.read()
        elif len(args) == 2 and args[0].isdigit() and args[1].isdigit():
            file.seek((int(args[0]) * 12) - 12)
            while file.tell() <= ((int(args[1]) * 12) - 12):
                result += file.read(11)

        else:
            raise Exception('Вы ввели что-то не то!')

    return result


if __name__ == '__main__':
    exit(show_sales(sys.argv[1:]))
