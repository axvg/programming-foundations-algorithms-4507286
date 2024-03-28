arr = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def selection_sort(arr):
  for fill_slot in range(len(arr) - 1, 0, -1):
      max_idx = 0
      for location in range(1, fill_slot + 1):
        if arr[location] > arr[max_idx]:
          max_idx = location
      
      arr[fill_slot], arr[max_idx] = arr[max_idx], arr[fill_slot]


print(arr)
selection_sort(arr)
print(arr)
