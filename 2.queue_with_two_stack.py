class OurQueue:
    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def enQueue(self,obj):
        self.in_stack.append(obj)

    def deQueue(self):
        if not self.out_stack:

            self.out_stack=self.in_stack[::-1]
            self.in_stack=[]

        return self.out_stack.pop()


if __name__ == '__main__':
    q = OurQueue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())