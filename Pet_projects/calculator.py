def calculator(num, base):
    total = ''
    while num > 1:
        quotient = num // base
        remains = num % base
        num = quotient
        total += str(remains)
    return total [::-1]

calculator(513, 2)