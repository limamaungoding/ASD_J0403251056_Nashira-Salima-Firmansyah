print("Nama : Nashira Salima Firmansyah")
print("NIM  : J0403251056")
print("="*40)


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    
    return root
def inorderTraversal(root, result):
    if root:
        inorderTraversal(root.left, result)
        result.append(root.data)
        inorderTraversal(root.right, result)
def preorderTraversal(root, result):
    if root:
        result.append(root.data)
        preorderTraversal(root.left, result)
        preorderTraversal(root.right, result)
def postorderTraversal(root, result):
    if root:
        postorderTraversal(root.left, result)
        postorderTraversal(root.right, result)
        result.append(root.data)

# =========================
# DATA BERDASARKAN NIM
# =========================
root_value = 56
data = [36, 76, 26, 46, 66, 86, 41]

root = Node(root_value)
for d in data:
    root = insert(root, d)

# =========================
# HASIL TRAVERSAL
# =========================
inorder_result = []
preorder_result = []
postorder_result = []

inorderTraversal(root, inorder_result)
preorderTraversal(root, preorder_result)
postorderTraversal(root, postorder_result)


# Output
print("Data Tree :", [root_value] + data)
print()

print("In-order   :", inorder_result)
print("Pre-order  :", preorder_result)
print("Post-order :", postorder_result)