class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return None
        curr = head
        hmap = {}
        while curr:
            node = Node(curr.val)
            hmap[curr] = node
            curr = curr.next
        curr = head
        while curr:
            new_node = hmap[curr]
            new_node.next = hmap[curr.next] if curr.next else None
            new_node.random = hmap[curr.random] if curr.random else None
            curr = curr.next
        return hmap[head]
