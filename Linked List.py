class LinkedList:
    class Node:
        def __init__(self):
            self.val = None
            self.next = None

    def __init__(self):
        self.Head = None
        self.tail = None
        self.size = 0

    def addFirst(self, item):
        new_node = self.Node()
        new_node.val = item

        if self.size == 0:
            self.Head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.next = self.Head
            self.Head = new_node
            self.size += 1

    def addLast(self, item):
        if self.size == 0:
            self.addFirst(item)
        else:
            new_node = self.Node()
            new_node.val = item
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def getFirst(self):
        if self.size == 0:
            raise Exception("Nothing is there so can't return any value ")
        return self.Head.val

    def getLast(self):
        if self.size == 0:
            raise Exception("Nothing is there so can't return any value ")
        return self.tail.val

    def getNode(self, k):
        if k < 0 or k >= self.size:
            raise Exception("Index Valid dedo bklol")
        temp = self.Head
        for i in range(1, k+1):
            temp = temp.next
        return temp

    def removeFirst(self):
        if self.size == 0:
            raise Exception("BkLol is Linked empty hai")
        temp = self.Head
        self.Head = self.Head.next
        if self.size == 1:
            self.tail = None
        self.size -= 1
        temp.next = None
        return temp.val

    def removeLast(self):   
        if self.size == 0:
            raise Exception("BkLol is Linked empty hai")
        if self.size == 1:
            return self.removeFirst()
        else:
            n = self.getNode(self.size - 2)
            temp = self.tail
            self.tail = n
            self.tail.next = None
            self.size -= 1
            return temp.val

    def display(self):
        temp = self.Head
        while temp is not None:
            print(temp.val, "->", end=" ")
            temp = temp.next
        print(".")
