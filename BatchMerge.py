def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):

        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

partial1 = open('partial-1.txt')
partial2 = open('partial-2.txt')
sorted = open('sorted.txt', 'w')

list1 = []
list2 = []

for line in partial1:
    list1.append(int(line.replace('\n', '')))

for line in partial2:
    list2.append(int(line.replace('\n', '')))

mergedList = merge(list1, list2)
for number in mergedList:
    sorted.write(str(number)+'\n')
