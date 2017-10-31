class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None
    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1
        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)
        if index >= len(inputValues):
            break
        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

def pre_traversal(root):
    if root:
        print root.val
        pre_traversal(root.left)
        pre_traversal(root.right)
def in_traversal(root):
    if root:
        in_traversal(root.left)
        print root.val
        in_traversal(root.right)
def post_traversal(root):
    if root:
        post_traversal(root.left)
        post_traversal(root.right)
        print root.val

####### Applications
def trimBST(root, L, R):
    if not root:
        return None
    if root.val > R:
        return trimBST(root.left, L, R)
    elif root.val < L:
        return trimBST(root.right, L, R)
    else:
        root.left = trimBST(root.left, L, R)
        root.right = trimBST(root.right, L, R)
    return root

def mergeTrees(root1, root2):
    if not root1 and not root2:
        return None
    root = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
    root.left = mergeTrees(root1 and root1.left, root2 and root2.left)
    root.right = mergeTrees(root1 and root1.right, root2 and root2.right)
    return root

# ----- new added by zxh -----
pass
# ----------------------------

#### Test the functions
if __name__ == '__main__':
    s1 = "[1,3,2,5]"
    s2 = "[2,1,3,null,4,null,7]"
    root1 = stringToTreeNode(s1)
    root2 = stringToTreeNode(s2)
    pre_traversal(root1)
    pre_traversal(root2)
    new_root = mergeTrees(root1, root2)
    pre_traversal(new_root)


