class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Difficult - Medium
        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
        reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a
        linked list.
        EXAMPLE: Input: l1 = [2,4,3], l2 = [5,6,4]
                Output: [7,0,8]
                Explanation: 342 + 465 = 807.
        :type l1: ListNode
        :type l2: ListNode
        :return: ListNode
        """

        # Solution

        temp_int = 0

        def print_nodes(node):
            while node:
                print(node.val, end=' ' if node.next else '\n')
                node = node.next

        def reverse_list(head, tail=None):  # если это важно, то подглядел я только эту функцию =)
            while head:
                head.next, tail, head = tail, head, head.next
            return tail

        def node_to_int(node):
            number = ''
            while node:
                number += str(node.val)
                node = node.next
            return int(number)

        def append(node, val):
            end = ListNode(val)
            n = node
            while (n.next):
                n = n.next
            n.next = end

        def int_to_listnode(node, number):
            for i in str(number):
                append(node, int(i))
            return node

        def drop(node):
            n = node
            while n.next.next is not None:
                n = n.next
            n.next = None

        temp_int = node_to_int(reverse_list(l1)) + node_to_int(reverse_list(l2))
        temp_node = ListNode()
        int_to_listnode(temp_node, temp_int)
        temp_node = reverse_list(temp_node)
        drop(temp_node)

        return temp_node


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

a = Solution()
a.addTwoNumbers(l1, l2)

