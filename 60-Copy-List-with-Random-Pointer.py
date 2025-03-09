class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        node_map = {}
        temp = head

        while temp:
            node_map[temp] = Node(temp.val)
            temp = temp.next

        temp = head
        while temp:
            node_map[temp].next = node_map.get(temp.next)
            node_map[temp].random = node_map.get(temp.random)
            temp = temp.next

        return node_map[head]