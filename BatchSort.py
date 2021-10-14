file1 = open('numbers-1.txt')
file2 = open('numbers-2.txt')

def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]     
  
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


numbers1 = []
for line in file1:
    numbers1.append(int(line.replace('\n', '')))

quickSort(numbers1, 0, len(numbers1)-1)
partial1 = open('partial-1.txt', 'w')

for number in numbers1:
    partial1.write(str(number) + '\n')

numbers2 = []
for line in file2:
    numbers2.append(int(line.replace('\n', '')))

quickSort(numbers2, 0, len(numbers2)-1)
partial2 = open('partial-2.txt', 'w')

for number in numbers2:
   partial2.write(str(number) + '\n')
