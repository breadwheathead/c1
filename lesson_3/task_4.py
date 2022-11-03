"""
*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
фамилий, а значения — словари, реализованные по схеме предыдущего задания и
содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:

 thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр
Алексеев", "Илья Иванов", "Анна Савельева")
{
"А": {
"П": ["Петр Алексеев"]
},
"С": {
"И": ["Иван Сергеев", "Инна Серова"],
"А": ["Анна Савельева"]
}
}

Как поступить, если потребуется сортировка по ключам?

"""

import operator


def sort_keys(dictionary):
    return dict(sorted(dictionary.items(), key=operator.itemgetter(0), reverse=False))


def thesaurus_adv(*names_surnames):
    external = {}

    for name_surname in names_surnames:
        name, surname = name_surname.split()
        n, s = name[0], surname[0]

        if s in external.keys():
            internal = external[s]
            if n in internal.keys():
                internal[n].append(name_surname)
            else:
                internal[n] = [name_surname]
            external[s].update(internal)
        else:
            internal = {n: [name_surname]}
            external[s] = internal

    for k, v in external.items():
        external[k] = sort_keys(v)

    return sort_keys(external)


result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Глеб Романов", "Петр Алексеев", "Илья Иванов", "Анна Савельева",
                       "Марина Аннушкина")
for row in result.items():
    print(row)
