# Reverse string using slicing

inp_str = str(input("Enter any string value: "))

length = len(inp_str)
reverse_str = inp_str[len(inp_str)::-1]
print("The reverse string is: ",reverse_str)
