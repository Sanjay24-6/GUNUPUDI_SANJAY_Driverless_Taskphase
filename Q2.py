class SelectionSorter:
	def selection_sort(self, l1):
		l=len(l1)
		for ci in range(l - 1): # need only n-1 iterations, last one is automatically the greatest
			si = ci
			for ni in range(ci + 1, l): #accessing each string in the list l1
				if l1[ni] < l1[si]:
					si = ni
			l1[ci], l1[si] = (l1[si],l1[ci],)
		return l1
if __name__ == "__main__":
	ns = int(input("Enter the number of strings: "))
	l1 = [input("Enter a string: ").lower() for _ in range(ns)]

	sorter = SelectionSorter() #accessing the class
	print("Sorted list:", sorter.selection_sort(l1))
