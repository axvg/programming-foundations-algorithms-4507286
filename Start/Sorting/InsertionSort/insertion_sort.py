arr = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def insertion_sort(arr):
  for idx in range(1, len(arr)):
    position = idx
    curr_value = arr[idx]

    while position > 0 and arr[position - 1] > curr_value:
      arr[position] = arr[position - 1]
      position -= 1
    
    arr[position] = curr_value


print(arr)
insertion_sort(arr)
print(arr)
