def get_max_values(dict_to_check):
    if not isinstance(dict_to_check, dict):
        print('TypeError: input not a dictionary')
        return None

    top_3_dict = sorted(dict_to_check.items(), key=lambda x: -x[1])[:3]
    top_3_keys = [elem[0] for elem in top_3_dict]

    return top_3_keys


my_dict = {'a': 500,
           'b': 5874,
           'c': 560,
           'd': 400,
           'e': 5874,
           'f': 20}


print(get_max_values(my_dict))  # prints ['b', 'e', 'c']
