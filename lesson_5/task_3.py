"""
Есть два списка:
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>),
например:

('Иван', '9А')
('Анастасия', '7В')

Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в
списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние
кортежи в виде: (<tutor>, None), например:

('Станислав', None)

Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.

"""

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Владимир', 'Артём', 'Илья', 'Саня']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def double_gen(ts, ks):
    for i in range(len(ts)):
        if i >= len(ks):
            yield ts[i], None
        else:
            yield ts[i], ks[i]


def school(t, k):
    _tutors = (tutor for tutor in t)
    _klasses = (klass for klass in k)

    for _school in zip(_klasses, _tutors):
        yield _school[::-1]
    for _tutor in tutors:
        yield _tutor, None


print(*school(tutors, klasses))
print()
result = double_gen(tutors, klasses)
print(next(result))
print(*result)
