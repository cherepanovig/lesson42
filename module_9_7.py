# Домашнее задание по теме "Декораторы".
# Цель задания:
# Освоить механизмы создания декораторов Python.

def is_prime(func):
    def wrapper(*args):
        res_fun = func(*args)
        if res_fun < 2:  # Числа меньше 2 не простые
            num_type = 'Составное число:'
        elif res_fun == 2:  # 2 - простое число
            num_type = 'Простое число:'
        else:
            for i in range(2, res_fun):
                if (res_fun % i) == 0:
                    num_type = 'Составное число:'
                    break
                else:
                    num_type = 'Простое число:'
        #print(range(2, res_fun))
        print(num_type)
        return res_fun
    return wrapper
@is_prime
def sum_three(*args):
    #sum_num = sum(args)
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
#print(sum_three(2, 3, 6))