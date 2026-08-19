class DynamicArray:
    
    def __init__(self, capacity: int):
        # Manually build an array with exactly <capacity> amount of capacuty
        self.capacity = capacity
        self.array_wc = [None] * self.capacity
        # self.size = 0


    def get(self, i: int) -> int:
        return self.array_wc[i]

    def set(self, i: int, n: int) -> None:
        self.array_wc[i] = n


    def pushback(self, n: int) -> None:
        size = self.getSize()
        if size == len(self.array_wc):
            self.resize()
        self.array_wc[size] = n


    def popback(self) -> int:
        size = self.getSize()
        if size > 0:
            mssg = self.array_wc[size-1]
            self.array_wc[size-1] = None
            return mssg

    def resize(self) -> None:
        old_array = self.array_wc
        new_capacity = self.capacity * 2
        self.capacity = new_capacity
        self.array_wc = [None] * new_capacity
        for i in range(len(old_array)):
            self.array_wc[i] = old_array[i]



    def getSize(self) -> int:
        count = 0
        for i in self.array_wc:
            if i is not None:
                count += 1

        
        return count
    
    def getCapacity(self) -> int:
        return self.capacity