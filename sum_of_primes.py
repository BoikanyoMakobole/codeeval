def findPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


current_total = 0
i = 1
primes = 0
while True:
    if findPrime(i):
        current_total += i
        primes += 1
    i += 1
    if primes == 1000:
        break

print(current_total)

