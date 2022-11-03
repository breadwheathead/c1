"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
содержащие имена, начинающиеся с соответствующей буквы. Например:

>>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
"И": ["Иван", "Илья"],
"М": ["Мария"], "П": ["Петр"]
}

Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется
сортировка по ключам? Можно ли использовать словарь в этом случае?

"""

import operator


def sort_keys(dictionary):
    return dict(sorted(dictionary.items(), key=operator.itemgetter(0), reverse=False))


def thesaurus(*names):
    dictionar = {}
    for name in names:
        lit = name[0]
        if lit in dictionar.keys():
            dictionar[lit].append(name)
        else:
            dictionar[lit] = [name]

    return sort_keys(dictionar)


if __name__ == '__main__':
    dictionary = thesaurus("Иван", "Мария", "Петр", "Илья")
    print(dictionary)
