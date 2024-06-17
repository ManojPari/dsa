def trailingZeroes(n: int):
    count = 0
    # Keep dividing n by powers of 5 and update the count
    while n >= 5:
        n //= 5
        count += n
    return count    

n = 15
print(trailingZeroes(n))