n = 18
result = ''

while n > 0:
    result = f'{n % 2}{result}'
    n //= 2

print(result)