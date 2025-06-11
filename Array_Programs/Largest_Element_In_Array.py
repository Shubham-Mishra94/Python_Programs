# Finding largest element in an array

def largest(arr, n):
    max = arr[0]

    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [10, 19, 9221, 14, 9118]
n = len(arr)

ans = largest(arr, n)
print("the largest elemnt in an array is: ", ans)
