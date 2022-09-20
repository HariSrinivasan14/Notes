
################### Node ###################
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class treeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


################### Max-Heap ###################
maxHeap = []

def bubbleDownMax(maxHeapSize, parent_index):
    global maxHeap
    largestIndex = parent_index  
    leftChild = 2 * parent_index + 1	  
    rightChild = 2 * parent_index + 2
    
    # need to check if the right child exist, the parent could be a leaf node or
    # may not have a rigth child.
    if rightChild < maxHeapSize and maxHeap[parent_index] < maxHeap[rightChild]: 
        largestIndex = rightChild
    # need to check if the left child exist, the parent could be a leaf node
    if leftChild < maxHeapSize and maxHeap[largestIndex] < maxHeap[leftChild]: 
        largestIndex = leftChild 
    if parent_index != largestIndex: 
        maxHeap[parent_index], maxHeap[largestIndex] = maxHeap[largestIndex], maxHeap[parent_index] # swap 
        bubbleDownMax(maxHeapSize, largestIndex)

def bubbleUpMax(childIndex):
    global maxHeap
    parentIndex = (childIndex - 1) // 2
    if parentIndex >= 0 and childIndex > 0 and maxHeap[parentIndex] < maxHeap[childIndex]:
        maxHeap[parentIndex], maxHeap[childIndex] = maxHeap[childIndex], maxHeap[parentIndex]
        bubbleUpMax(parentIndex)
    else:
        return

def insertMaxHeap(num, maxHeapSize):
    global maxHeap
    maxHeap.append(num)
    maxHeapSize += 1
    bubbleUpMax(maxHeapSize - 1)

def buildMaxHeap(maxHeapSize):
    global maxHeap
    for index in range(maxHeapSize // 2, -1, -1):
        bubbleDownMax(maxHeapSize, index)

def extractMax(maxHeapSize):
    global maxheap
    if maxHeapSize > 1:
        maxheap[0], maxheap[-1] = maxheap[-1], maxheap[0]
        maxValue = maxheap.pop()
        maxHeapSize -= 1
        bubbleDownMax(maxHeapSize, 0)
        return maxValue
    else:
        maxHeapSize = 0
        return maxheap.pop()

################### Min Heap ###################
minHeap = []

def buildMinHeap(minHeapSize):
    global minHeap
    for index in range(minHeapSize // 2, -1, -1):
        bubbleDownMin(minHeapSize,index)

def insertMinHeap(num, minHeapSize):
    global minHeap
    minHeap.append(num)
    minHeapSize += 1
    bubbleUpMin(minHeapSize - 1)


def bubbleDownMin(minHeapSize, parentIndex):
    global minHeap
    smallestIndex = parentIndex  
    leftChild = 2 * parentIndex + 1	  
    rightChild = 2 * parentIndex + 2
    
    if rightChild < minHeapSize and minHeap[parentIndex] > minHeap[rightChild]: 
        smallestIndex = rightChild 
    if leftChild < minHeapSize and minHeap[smallestIndex] > minHeap[leftChild]: 
        smallestIndex = leftChild
    if parentIndex != smallestIndex: 
        minHeap[parentIndex], minHeap[smallestIndex] = minHeap[smallestIndex], minHeap[parentIndex] # swap 
        bubbleDownMin(minHeapSize, smallestIndex)


def bubbleUpMin(childIndex):
    global minHeap
    parent = (childIndex - 1)//2
    if parent >= 0 and childIndex > 0 and minHeap[parent] > minHeap[childIndex]:
        minHeap[parent], minHeap[childIndex] = minHeap[childIndex], minHeap[parent]
        bubbleUpMin(parent)

def extractMin(minHeapSize):
    global minHeap
    if minHeapSize > 1:
        minHeap[0], minHeap[-1] = minHeap[-1], minHeap[0]
        minValue = minHeap.pop()
        minHeapSize -= 1
        bubbleDownMin(minHeapSize, 0)
        return minValue
    else:
        minHeapSize = 0
        return minHeap.pop()


################### Stack ###################
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

 
    # Get the current size of the stack
    def getSize(self):
        return self.size
 
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
 
    # Get the top item of the stack
    def peek(self):
 
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            return None
        return self.head
 
    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1
    def pop(self):
        if self.size == 0:
            return None
        returnNode = self.head
        self.head = self.head.next
        self.size -= 1
        return returnNode.value

################### Queue ###################
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

 
    # Get the current size of the Queue
    def getSize(self):
        return self.size
 
    # Check if the Queue is empty
    def isEmpty(self):
        return self.size == 0
 
    # Get the top item of the Queue
    def peek(self):
 
        # Sanitary check to see if we
        # are peeking an empty Queue.
        if self.isEmpty():
            return None
        return self.head
 
    # Push a value into the Queue.
    def Enqueue(self, value):
        node = Node(value)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:   
            self.tail.next = node
            self.tail = node
        self.size += 1


    def Dequeue(self):
        if self.size == 0:
            return None
        returnNode = self.head
        self.size -= 1
        if self.size == 0:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return returnNode.value


################### Test Functions ###################
def testStack():
    print("~~~~~~~~~~~~ testing Stack ~~~~~~~~~~~~")
    stack = Stack()
    for i in range(10):
        stack.push(i)
    while(not stack.isEmpty()):
        print(stack.pop())


def testQueue():
    print("~~~~~~~~~~~~ testing Queue ~~~~~~~~~~~~")
    queue = Queue()
    for i in range(10):
        queue.Enqueue(i)
    while(not queue.isEmpty()):
        print(queue.Dequeue())

def testMaxHeap():
    print("~~~~~~~~~~~~ testing Max-Heap ~~~~~~~~~~~~")
    global maxHeap
    maxHeap = [17, 5, 13, 1, 4, 2 ,6]
    buildMaxHeap(len(maxHeap))
    print(maxHeap)

    maxHeap = [2, 6 ,5 , 7, 9, 10]
    buildMaxHeap(len(maxHeap))
    print(maxHeap)


def testMinHeap():
    print("~~~~~~~~~~~~ testing Min-Heap ~~~~~~~~~~~~")
    global minHeap
    minHeap = [8, 6, 9, 3, 5 , 1]
    buildMinHeap(len(minHeap))
    print(minHeap)

    minHeap = [20, 10, 50, 30, 60, 70, 80]
    buildMinHeap(len(minHeap))
    print(minHeap)
    print(extractMin(len(minHeap)))
    print(minHeap)


def main():
    # testStack()
    # testQueue()
    # testMaxHeap()
    testMinHeap()




main()