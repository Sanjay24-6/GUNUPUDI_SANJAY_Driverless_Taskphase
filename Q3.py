from Q2 import SelectionSorter

class BinarySearcher:
	def binary_search(self, l1, target):
		f = 0
		l = len(l1) - 1

		while f <= l:
			mid = (f + l) // 2

			if l1[mid] == target:
				return mid
			if l1[mid] < target:
				f = mid + 1
			else:
				l = mid - 1
		return -1
ns = int(input("Enter number of strings: "))
l1 = []
for _ in range(ns):
	l1.append(input("Enter a string: ").lower())
sorter = SelectionSorter()
sorted_l1 = sorter.selection_sort(l1)
target = input("Enter the string to be searched: ").lower()

searcher = BinarySearcher() #accessing the class
index = searcher.binary_search(sorted_l1, target)

print("Sorted list:", sorted_l1)
if index == -1:
	print("String not found")
else:
	print("String found at index:", index)
# change made on main