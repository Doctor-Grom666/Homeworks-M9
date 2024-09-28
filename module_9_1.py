def apply_all_func(int_list: list, *functions):
    try:
        results = {}
        for i in functions:
            results.update({i.__name__: i(int_list)})
        return results
    except TypeError:
        return 'Список должен состоять только из чисел'


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))