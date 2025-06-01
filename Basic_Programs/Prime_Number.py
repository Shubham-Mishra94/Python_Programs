# Prime Number

number = 5
temp = False

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            temp = True
            break
if(temp):
    print("The given number", number, "is not a prime number")
else:
    print("The given number", number, "is prime number")

    