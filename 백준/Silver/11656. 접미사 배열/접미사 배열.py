s = input()
print('\n'.join(sorted([s[i:] for i in range(len(s))])))