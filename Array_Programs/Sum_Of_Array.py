# Find sum of array

def Sum(arr):
    sum =0

    for i in arr:
        sum = sum +i
    return sum
    

if __name__ == "__main__":
    arr = [10, 12, 14, 16]
    n = len(arr)
    ans = Sum(arr)
    print('Sum of the array is: ', ans)

