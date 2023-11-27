def is_lists_same_length(boys_names, girls_names):
    return len(boys_names) == len(girls_names)


def get_dating_pairs(boys_names, girls_names):
    boys_names = sorted(boys_names)
    girls_names = sorted(girls_names)
    dating_pairs = [pair for pair in zip(boys_names, girls_names)]
    return dating_pairs


def print_pairs(dating_pairs):
    for boy_name, girl_name in dating_pairs:
        print(f'{boy_name} и {girl_name}')


boys_names = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls_names = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

print('Результат:')
if is_lists_same_length(boys_names, girls_names):
    dating_pairs = get_dating_pairs(boys_names, girls_names)
    print_pairs(dating_pairs)
else:
    print('Внимание, кто-то может остаться без пары!')


boys_names = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls_names = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

print('Результат:')
if is_lists_same_length(boys_names, girls_names):
    dating_pairs = get_dating_pairs(boys_names, girls_names)
    print_pairs(dating_pairs)
else:
    print('Внимание, кто-то может остаться без пары!')
