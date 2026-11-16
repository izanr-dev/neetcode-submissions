class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        final = None
        actual = head

        while actual:
            
            final = ListNode(actual.val, final)
            actual = actual.next


        return final
            
            
        