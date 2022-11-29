"""
*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
должен быть с заглавной. Например:

>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"

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


def num_translate_adv(en_numeral):
    if en_numeral.lower() in dictionary.keys():
        if en_numeral == en_numeral.capitalize():
            return dictionary[en_numeral.lower()].capitalize()
        return dictionary[en_numeral.lower()]
    return None


if __name__ == '__main__':
    print(num_translate_adv('two'))
