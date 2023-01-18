class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pal = [head.val]
        head = head.next
        while head != None:
            pal.append(head.val)
            head = head.next
        return True if pal == pal[::-1] else False