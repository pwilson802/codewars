# https://www.codewars.com/kata/can-you-get-the-loop/train/python

def loop_size(node):
    history = []
    for n in node


if __name__ == '__main__':
    # Make a short chain with a loop of 3
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print("Loop size of 3 expected")
    a = loop_size(node1)
    print(a)