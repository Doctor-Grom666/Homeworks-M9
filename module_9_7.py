def is_prime(func):
    def wrapper(*args):
        check = func(*args)
        prime = False
        summa = sum(args)
        for i in range(2, summa):
            if summa % i == 0:
                prime = True
        if prime:
            print('Составное')
        else:
            print('Простое')
        return check
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
