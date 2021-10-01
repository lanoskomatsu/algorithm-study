insert_price = input('insert: ')
product_price = input('product: ')
change = int(insert_price) - int(product_price)

# 5000円の枚数
r5000 = change // 5000
q5000 = change % 5000
print(f'5000: {r5000}')

# 1000円の枚数
r1000 = q5000 // 1000
q1000 = q5000 % 1000
print(f'1000: {r1000}')

# 500円の枚数
r500 = q1000 // 500
q500 = q1000 % 500
print(f'500: {r500}')

# 100円の枚数
r100 = q500 // 100
q100 = q500 % 100
print(f'100: {r100}')

# 50円の枚数
r50 = q100 // 50
q50 = q100 % 50
print(f'50: {r50}')

# 10円の枚数
r10 = q50 // 10
q10 = q50 % 10
print(f'10: {r10}')

# 5円の枚数
r5 = q10 // 5
q5 = q10 % 5
print(f'5: {r5}')

# 1円の枚数
r1 = q5 // 1
q1 = q5 % 1
print(f'1: {r1}')

print(change)
