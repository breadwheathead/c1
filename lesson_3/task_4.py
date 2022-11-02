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


def thesaurus_adv(*names_surnames):
    dict_result = {}
    for name_surname in names_surnames:
        pair = name_surname.split()
        cap_lit_sur = pair[1][0]
        cap_lit_name = pair[0][0]

        if cap_lit_sur in dict_result.keys():
            dict_result[cap_lit_sur].append(name_surname)
        else:
            dict_result[cap_lit_sur] = {cap_lit_name: pair[1]}
    return dict_result


result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(result)
