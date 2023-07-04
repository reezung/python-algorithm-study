word = input()
length = len(word)
is_palindrome = 1
for i in range(0,length//2+1):
    if word[i] != word[length-1-i]:
        is_palindrome = 0
        break
print(is_palindrome)