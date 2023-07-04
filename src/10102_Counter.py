from collections import Counter
V = int(input())
vote = Counter(input())
if vote['A'] == vote['B']:
    print('Tie')
else:
    print((lambda v: 'A' if v['A']>v['B'] else 'B')(vote))