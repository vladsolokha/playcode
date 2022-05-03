def insertionSort(arr):
  length = len(arr)
  item = 1
  while item < length: 
    # item to be inserted
    item_ins = arr[item]
    counter = item-1
    while counter >= 0 and arr[counter] > item_ins:
      arr[counter+1] = arr[counter] #swap if next elem is > cururent item_ins
      counter -= 1
    arr[counter+1] = item_ins
    item += 1

print(insertionSort([40,13,20,8]))