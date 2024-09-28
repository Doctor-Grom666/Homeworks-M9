first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[x]) == len(second[y]) for x in range(len(first)) for y in range(len(second))
                 if first.index(first[x]) == second.index(second[y]))

print(list(first_result))
print(list(second_result))