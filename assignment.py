# Exercise 1
Queue = []
HeadPointer = 0
TailPointer = -1

for i in range(8):
    Queue.append(-1)

def IsEmpty():
    global Queue,HeadPointer,TailPointer
    if HeadPointer>TailPointer:
        return True
    else:
        return False

def IsFull():
    global TailPointer
    if TailPointer == 7:
        return True
    else:
        return False


# Exercise 2
Queue = []
HeadPointer = 0
TailPointer = -1

for i in range(8):
    Queue.append(-1)

def Enqueue(Item):
    global Queue,HeadPointer,TailPointer
    if TailPointer==7:
        return False
    else:
        TailPointer=TailPointer+1
        Queue[TailPointer]=Item
        return True



# Exercise 3
Queue = []
HeadPointer = 0
TailPointer = -1

for i in range(8):
    Queue.append(-1)


def IsEmpty():
    global HeadPointer,TailPointer
    if HeadPointer>TailPointer:
        return True
    else:
        return False

def IsFull():
    global TailPointer
    if TailPointer == 7:
        return True
    else:
        return False

def Enqueue(Item):
    global Queue,HeadPointer,TailPointer
    if IsFull():
        return False
    TailPointer = TailPointer + 1
    Queue[TailPointer] = Item
    return True

def Dequeue():
    global Queue,HeadPointer,TailPointer
    if IsEmpty():
        return -1
    DataToReturn = Queue[HeadPointer]
    HeadPointer = HeadPointer+1
    return DataToReturn

# Exercise 4
def Peek():
    # Write your code here
    pass


def ShowQueue():
    # Write your code here
    pass


# Exercise 5
def Canteen(Commands):
    # Write your code here
    pass
