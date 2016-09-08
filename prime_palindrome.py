def findPrime(num):
    if num == 1:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


king_of_palindrome = 0
for i in range(1, 1000):
    if not findPrime(i):
        continue
    if not str(i) == str(i)[::-1]:
        continue
    if i > king_of_palindrome:
        king_of_palindrome = i
    else:
        pass

print(king_of_palindrome)
