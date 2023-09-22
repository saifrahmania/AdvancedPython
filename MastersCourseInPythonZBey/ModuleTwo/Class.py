class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order(root):
    """
    Traverses a binary tree in pre-order (root, left, right) and prints the value of each node.

    Args:
    =====
        root: The root node of the binary tree.

    Returns:
    ========
        None
    """
    if root is not None:
        print(root.value)
        pre_order(root.left)
        pre_order(root.right)

def level_order(root):
    """
    Traverses a binary tree in level-order (left to right) and prints the value of each node.

    Args:
    =====
        root: The root node of the binary tree.

    Returns:
    ========
        None
    """
    if root is None:
        return
    queue = []
    queue.append(root)
    while(len(queue) > 0):
        print(queue[0].value)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def post_order(root):
    """
    Traverses a binary tree in post-order (left, right, root) and prints the value of each node.

    Args:
    =====
        root: The root node of the binary tree.

    Returns:
    ========
        None
    """
    if root is not None:
        post_order(root.left)
        post_order(root.right)
        print(root.value)

def in_order(root):
    """
    Traverses a binary tree in in-order (left, root, right) and prints the value of each node.

    Args:
        root: The root node of the binary tree.

    Returns:
        None
    """
    if root is not None:
        in_order(root.left)
        print(root.value)
        in_order(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Pre-order traversal:")
#pre_order(root)
print("In-order traversal:")
#in_order(root)
print("Level-order traversal:")
#level_order(root)
print("Post-order traversal:")
#post_order(root)

import os
for dirpath, _, filenames in os.walk("C:\\Users\\Admin\\Documents\\GitHub\\AdvancedPython\\ModuleTwo"):
    print("Current Path: ", dirpath)
    print("Files: ", filenames)
    
def list_files(startpath):
    """
    Prints all files in a directory recursively.

    Args:
    =====
        startpath: The directory to start in.

    Returns:
    ========
        None
    """
    for root, _, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
list_files("C:\\Users\\Admin\\Documents\\GitHub\\AdvancedPython\\ModuleTwo")    

import glob

files = glob.glob("C:\\Users\\Admin\\Documents\\GitHub\\AdvancedPython\\ModuleTwo\\*.py", recursive=True)
for file in files:
    print(file)

