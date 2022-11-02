class CircularQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = list()
        self.size = 0
        self.front = -1             #index

    def enqueue(self, d):
        if self.size < self.capacity:
            self.data.append(d)
            self.size += 1
            self.front = 0
        
    def dequeue(self):
        if self.size > 0:
            h = self.data[self.front]
            self.data.pop(self.front)
            self.size -= 1
        return h

    def __len__(self):
        return self.size

    def display(self):
        
        if self.size < self.capacity:
            antrian = list()
            for d in self.data:
                antrian.append(d)
            
            print("Yang ada pada antrian adalah: ", end="")
            for d in antrian:
                print(d, end=" ")
            print("")
        
        else:
            print("Yang ada pada antrian circular adalah: ", end="")
            for d in self.data:
                print(d, " ", end="")
            print("")
            print("Antrian penuh")

circularQueue = CircularQueue(5)
circularQueue.enqueue(14)
circularQueue.enqueue(22)
circularQueue.enqueue(13)
circularQueue.enqueue(-6)
circularQueue.display()
print("Data yang dihapus adalah = ", circularQueue.dequeue())
print("Data yang dihapus adalah = ", circularQueue.dequeue())
circularQueue.display()
circularQueue.enqueue(9)
circularQueue.enqueue(20)
circularQueue.enqueue(5)
circularQueue.display()
