from typing import Optional
from math import inf

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    clean_lists = [i for i in lists if i is not None]
    if clean_lists == []:
        return None
    linky_first = [head.val for head in clean_lists]
    linky_sorted = ListNode()
    linky_head = linky_sorted
    while linky_first != []:
        smallest = 0
        for i in range(1, len(linky_first)):
            if linky_first[i] < linky_first[smallest]:
                smallest = i
        linky_head.val = linky_first[smallest]
        update_linky(linky_first, clean_lists, smallest)
        if linky_first != []:
            linky_head.next = ListNode()
            linky_head = linky_head.next
    return linky_sorted



def update_linky(linky_first: list[int], lists: list[Optional[ListNode]], smallest: int):
    if lists[smallest].next is None:
        lists.pop(smallest)
        linky_first.pop(smallest)
    else:
        lists[smallest] = lists[smallest].next
        linky_first[smallest] = lists[smallest].val



if __name__ == "__main__":
    def create_linked_list(lst: list[int]) -> ListNode:
        if len(lst) == 1:
            return ListNode(lst[0])
        else:
            return ListNode(lst[0], create_linked_list(lst[1:]))

    def create_collection(lst: list[list[int]]) -> list[ListNode]:
        return [create_linked_list(i) for i in lst]

    def display_linked_list(lst: ListNode) -> list[int]:
        if lst is None:
            return []
        else:
            return [lst.val] + display_linked_list(lst.next)

    collection = create_collection([])
    merged = mergeKLists(collection)
    answer = display_linked_list(merged)
# linky_first = [lst.val for lst in lists]
# linky_sort = ListNode()
# linky_head = linky_sort
# while linky_first != []:
#     # find the index of the smallest element in linky_first
#     smallest = linky_first[0]
#     for val in range(1, len(linky_first)):
#         if linky_first[val] < smallest:
#             smallest = val
#
#     # set the head value as the smallest element
#     linky_head.val = linky_first[smallest]
#
#     # update the linky_first list
#     if (lists[smallest]).next is None:
#         # remove the corresponding ListNode object
#         lists.pop(smallest)
#         linky_first.pop(smallest)
#     else:
#         # access the ListNode object, and find the next one
#         lists[smallest] = lists[smallest].next
#         linky_first[smallest] = lists[smallest].val
#
#     linky_head.next = ListNode()
#     linky_head = linky_head.next
# return linky_sort



