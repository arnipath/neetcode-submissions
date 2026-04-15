# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = list1
        lst2 = list2
        newList = ListNode()
        nlst = newList
        
        while lst1 and lst2:
            if lst1.val < lst2.val:
                nlst.next = lst1
                lst1 = lst1.next
            else:
                nlst.next = lst2
                lst2 = lst2.next
            nlst = nlst.next
        
        if lst1:
            nlst.next = lst1
        if lst2:
            nlst.next = lst2
        return newList.next

