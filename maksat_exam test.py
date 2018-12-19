# arr = []
# arr.append('adasd')
# arr.append(234234)
# arr.append(0.23234)
# arr.append(8.456)
# arr.append('getet')
# def print_member_type(arr):
#   print(arr[0])
#   print(arr[1])
#   print(arr[2])
#   print(arr[3])
#   print(arr[4])
#   for string in arr:
#     print(string)

arr = ['adasd',234234,0.23234,8.456,'getet',True]
arr.append('adasd')
arr.append(234234)
arr.append(0.23234)
arr.append(8.456)
arr.append('getet')
arr.append(True)
def print_member_type(arr):
  print(type(arr[0]))
  print(arr[1])
  print(arr[2])
  print(arr[3])
  print(type(arr[4]))
  print(arr[5])
for string in arr:
  print(type(string))

