print((2 > 1 or 3 > 4) and 5 > 4)
print(2 > 1 or (3 > 4 and 5 > 4))
print(1 > 2 or (3 > 4 and 5 > 4))
print((1 > 2 or 3 > 4) and 5 > 4)
print('\n'.join([''.join([('loveAngel'[(x - y) % len('lovAngel')] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
            x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else '') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
