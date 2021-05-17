# 트리 순회
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


def pre_order(cur_node):
    print(cur_node.data, end="")
    if cur_node.left_node != ".":
        pre_order(tree[cur_node.left_node])
    if cur_node.right_node != ".":
        pre_order(tree[cur_node.right_node])


def in_order(cur_node):
    if cur_node.left_node != ".":
        in_order(tree[cur_node.left_node])
    print(cur_node.data, end="")
    if cur_node.right_node != ".":
        in_order(tree[cur_node.right_node])


def post_order(cur_node):
    if cur_node.left_node != ".":
        post_order(tree[cur_node.left_node])
    if cur_node.right_node != ".":
        post_order(tree[cur_node.right_node])
    print(cur_node.data, end="")


n = int(input())
tree = {}

for _ in range(n):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node)

pre_order(tree["A"])
print()
in_order(tree["A"])
print()
post_order(tree["A"])
