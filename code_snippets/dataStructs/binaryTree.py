class node(object):
	def __init__(self, value):
		self.value = value
		self.left = None 
		self.right = None

class BinaryTree(object):
	def __init__(self, root):
		self.root = node(root)

	def print_tree(self, traversal_type):
		if traversal_type == "preorder":
			return self.preorder_print(mytree.root, "")
		else:
			print("Traversal type "+str(traversal_type)+" is not supported.")


	def preorder_print(self, start, traversal):
		if start:
			traversal += (str(start.value) + "-")
			traversal = self.preorder_print(start.left, traversal)
			traversal = self.preorder_print(start.right, traversal)
		return traversal



# TEST

mytree = BinaryTree(1)
mytree.root.left = node(2)
mytree.root.right = node(3)
mytree.root.left.left = node(4)
mytree.root.left.right = node(5)
mytree.root.right.left = node(6)
mytree.root.right.right = node(7)

print(mytree.print_tree("preorder"))