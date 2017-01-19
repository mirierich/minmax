def find_max_min(input):
  
  resultingList = []
  max_num = max(input)
  min_num = min(input)
  if min_num == max_num:
    num_of_elements = len(input)
    resultingList.append(num_of_elements)
  else:
    resultingList.append(min_num)
    resultingList.append(max_num)
  return resultingList

print(find_max_min([1, 2, 3, 4]))
print(find_max_min([6, 4]))
print(find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2]))
print(find_max_min([4, 4, 4, 4]))