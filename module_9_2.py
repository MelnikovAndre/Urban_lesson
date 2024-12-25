def is_prime(func):

    def wrappper(*args):
        summa = func(*args)
        condition = True
        for i in range (2, summa - 1):
            if summa % i == 0:
                condition = False
                break
        if condition:
            print("Простое")
        else:
            print("Составное")
        return summa
    return wrappper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)