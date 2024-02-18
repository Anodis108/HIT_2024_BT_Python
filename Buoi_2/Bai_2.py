c = input()
print(*map(lambda a: True if a in c else False, ['HIT', 'hit']))
print(True if ('14' not in c ) else False)
    