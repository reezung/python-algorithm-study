bowls = input()
curr = bowls[0]
height = 10
for b in bowls[1:]:
    if b == curr:
        height += 5
    else:
        height += 10
    curr = b
print(height)
