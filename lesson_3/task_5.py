"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
случайных слов, взятых из трёх списков (по одному из каждого):

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный",
"мягкий"]

Например:

# >>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий
повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?

"""

from random import choice


def get_jokes(n, no_repeat=False):
    """
    Функция возвращает заданное количество шуток, сформированных из трёх случайных слов
    :return: str:

    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    jokes = []

    for _ in range(n):
        if no_repeat:
            while nouns:
                jokes.append(f'{nouns.pop()} {adverbs.pop()} {adjectives.pop()}')
        else:
            jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return jokes


jokes = get_jokes(6, no_repeat=True)

for joke in jokes:
    print(joke)
