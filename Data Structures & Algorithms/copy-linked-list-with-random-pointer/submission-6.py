"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if not head:
        #     return None

        nodes = {}
        curr = head

        while curr is not None:
            nodes[curr] = Node(curr.val)
            curr = curr.next

        for og, copy in nodes.items():
            next = og.next
            random = og.random
            if next:
                copy.next = nodes[next]
            if random: 
                copy.random = nodes[random]
        if not head:
            return None
        return nodes[head]

#Node(,Node(),Node())

# Node(3,Node(7),None) : Node(3)
# Node(7,Node(4),Node(5)) : Node(7)
# Node(4,Node(5),Node(3)) : Node(4)
# Node(5,None,Node(7)) : Node(5)

# Node(3,Node(7),None) : Node(3, Node(7),None)
# Node(7,Node(4),Node(5)) : Node(7)
# Node(4,Node(5),Node(3)) : Node(4)
# Node(5,None,Node(7)) : Node(5)


            

       







