class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next


if __name__=='__main__':
    singlyList=LinkedList()

    singlyList.head=Node(1)

    second=Node(2)
    third=Node(3)
    singlyList.head.next=second
    second.next=third

    singlyList.printList()






