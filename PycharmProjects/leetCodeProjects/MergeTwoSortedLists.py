# Bağlı liste düğüm sınıfı
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Yardımcı fonksiyon: Listeyi bağlı listeye çevir
def build_linked_list(values):
    dummy = ListNode(-1)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Yardımcı fonksiyon: Bağlı listeyi yazdır
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# Çözüm sınıfı
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next

# Test değerleri
list1 = build_linked_list([1, 3, 5])
list2 = build_linked_list([2, 4, 6])

# Fonksiyonu çağır
sol = Solution()
merged = sol.mergeTwoLists(list1, list2)

# Sonucu yazdır
print("Birleştirilmiş bağlı liste:")
print_linked_list(merged)
