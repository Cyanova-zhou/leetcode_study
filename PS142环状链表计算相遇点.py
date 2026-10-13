# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


##使用哈希表
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cash=set()
        now=head
        while now!=None and now.next!=None:
            if now in cash:
                return now
            else:
                cash.add(now)
                now=now.next
        return None


##使用快慢指针
##当发现 slow 与 fast 相遇时，我们再额外使用一个指针 ptr。起始，它指向链表头部；随后，它和 slow 每次向后移动一个位置。最终，它们会在入环点相遇。
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                pre=head
                while True:
                    if pre==slow:
                        return pre
                    pre=pre.next
                    slow=slow.next
        return None