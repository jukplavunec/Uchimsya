def get_words_distribution(queries):
    words_distribution = {}
    for query in queries:
        words_count = len(query.split(' '))
        if words_count in words_distribution:
            words_distribution[words_count] += 1
        else:
            words_distribution[words_count] = 1
    return dict(sorted(words_distribution.items()))


def get_stats(words_distribution, queries_count):
    stats = {}
    for words_count in words_distribution:
        stats[words_count] = round(words_distribution[words_count] / queries_count, 4) * 100
    return stats


queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт',
]

print('Результат:')
words_distribution = get_words_distribution(queries)
stats = get_stats(words_distribution, len(queries))

for words_count in stats:
    print(f'Поисковых запросов, содержащих {words_count} слов(а): {stats[words_count]}%')
