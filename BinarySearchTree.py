
class BinarySearchTree:
	class Node:

		def __init__(self, val):
			self.val = val
			self.left = None
			self.right = None

		def get_value(self):
			return self.val

		def set_value(self, newval):
			self.val = newval

		def get_left(self):
			return self.left

		def get_right(self):
			return self.right

		def set_left(self, newleft):
			self.left = newleft

		def set_right(self, newright):
			self.right = newright

		def __iter__(self):
			if self.left != None:
				for elem in self.left:
					yield elem

			yield self.val

			if self.right != None:
				for elem in self.right:
					yield elem

	def __init__(self):
		self.root = None
	def insert(self, val):
		def __insert(root,val):
			if root is None:
				return BinarySearchTree.Node(val)

			if val < root.get_value():
				root.set_left(__insert(root.get_left(),val))
			else:
				root.set_right(__insert(root.get_right(),val))

			return root
		self.root = __insert(self.root, val)

	def __iter__(self):
		if self.root != None:
			return self.root.__iter__()
		else:
			return [].__iter__()


def main():
	s = input("enter a list of numbers ")
	lst = s.split()

	tree = BinarySearchTree()

	for x in lst:
		tree.insert(float(x))

	for x in tree:
		print(x)

if __name__ == "__main__":
	main()










