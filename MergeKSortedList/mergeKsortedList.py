import heapq

def prnt_lst(lst):
    while lst != None:
        print(lst.val, " ")
        lst = lst.next


class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeKLists(lists):
    if lists == []:
        return None
    H = [] #min heap
    
    for lst in lists: # adding first element of every list.
        if lst != None:
            heapq.heappush(H,(lst.val,lst))
    sortedList = None
    if H != []: # getting the first(smallest) element
        val, lst = heapq.heappop(H)
        sortedList = lst
        if lst.next != None:
            heapq.heappush(H,(lst.next.val,lst.next))
  
    current = sortedList
    while H != []: 
        val, lst = heapq.heappop(H)
        current.next = lst
        current = current.next
        lst = lst.next
        if lst != None:
            heapq.heappush(H,(lst.val,lst))

    return sortedList

mergeKLists([[]])
mergeKLists([])
mergeKLists([[]])

def test():
    l = ListNode(5, None)
    l1 = ListNode(1, l)
    l2 = ListNode(0, l1)
    
    
    l4 = ListNode(8, None)
    l5 = ListNode(4, l4)
    l6 = ListNode(2, l5)
    l7 = ListNode(-1, l6)

    lst = [l7,l2]
    
    mergedLst = mergeKLists(lst)
    prnt_lst(mergedLst)


test()

    
