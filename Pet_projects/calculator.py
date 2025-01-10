def calculator(num, base):
    total = ''
    while num > 1:
        quotient = num // base
        remains = num % base
        num = quotient
        total += str(remains)
    if num == 1:
        total += '1'
    
    return total [::-1]

calculator(513, 2)