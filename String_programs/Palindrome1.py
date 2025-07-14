# Palindrome

given_num = 12321

duplicate_num = given_num
reverse_num = 0

while (given_num>0):
    remainder = given_num % 10
    reverse_num = (reverse_num * 10) + remainder
    given_num = given_num // 10

if (duplicate_num == reverse_num):
    print("The given number", duplicate_num, "is palindrome")
else:
    print("The given number", duplicate_num, "is not palindrome")

