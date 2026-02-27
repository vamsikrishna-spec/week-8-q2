data = [(9, 18, 28), (6, 12, 18), (4, 20, 40), (3, 6, 9)]
def sort_key(item):
 return item[-1]
sort_data = sorted(data, key=sort_key)
print("Original list: ",data)
print("Sorted list: ",sort_data)

