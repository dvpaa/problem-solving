# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pal = [head.val]
        head = head.next
        while head != None:
            pal.append(head.val)
            head = head.next
        return True if pal == pal[::-1] else False