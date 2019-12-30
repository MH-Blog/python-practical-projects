l = [x for x in range(10)]


def is_prime(num):
    return num % 2 == 0

prime_num = []
for num in l:
    if is_prime(num):
        prime_num.append(num)
print(prime_num)
