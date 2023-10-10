class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def delete(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.val = find_min_value(root.right)
        root.right = delete(root.right, root.val)
    return root

def find_min_value(root):
    while root.left is not None:
        root = root.left
    return root.val

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

root = None
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)

print("Inorder Traversal:")
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)
inorder_traversal(root)

search_key = 40
if search(root, search_key):
    print(f"\n{search_key} found in the tree.")
else:
    print(f"\n{search_key} not found in the tree.")

delete_key = 30
root = delete(root, delete_key)
print(f"\nAfter deleting {delete_key}, Inorder Traversal:")
inorder_traversal(root)
