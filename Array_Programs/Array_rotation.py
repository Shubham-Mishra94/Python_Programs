# Rotation of an array
# Array, Array size (n), steps of rotation (d)

def rotarray(arr, n, d):
    temp = []
    i = 0
    while (i<d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d<n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
        arr[:] = arr[:1] + temp 
        return arr
    

arr = [1, 2, 3, 4, 5, 6, 7, 8]
print("Array after left rotation is: ", end='')
print(rotarray(arr, len(arr),7 ))

