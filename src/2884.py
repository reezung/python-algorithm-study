H, M = map(int, input().split())

if M >= 45:
    print(H, M - 45)
else:
    print((24 + H - 1) % 24, 60 + M - 45)
