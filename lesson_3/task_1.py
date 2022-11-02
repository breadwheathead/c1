"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
русский язык. Например:

>>> num_translate("one")
"один"
>>> num_translate("eight")
"восемь"

Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить
информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или
снаружи.

"""


dictionary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(en_numeral):
    if en_numeral.lower() in dictionary.keys():
        return dictionary[en_numeral.lower()]
    return None


if __name__ == '__main__':
    print(num_translate('twO'))
