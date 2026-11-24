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
Queue = []
HeadPointer = 0
TailPointer = -1

for i in range(8):
    Queue.append(-1)


def IsEmpty():
    global HeadPointer,TailPointer
    if HeadPointer > TailPointer:
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
  global Queue, HeadPointer, TailPointer
  if IsFull():
    return False
  TailPointer += 1
  Queue[TailPointer] = Item
  return True


def Dequeue():
  global Queue, HeadPointer, TailPointer
  if IsEmpty():
    return -1
  DataToReturn = Queue[HeadPointer]
  HeadPointer += 1
  return DataToReturn


def Peek():
    if IsEmpty():
        return -1
    return Queue[HeadPointer]

def ShowQueue():
    if IsEmpty():
        return ""
    items = []
    for i in range(HeadPointer, TailPointer + 1):
        items.append(str(Queue[i]))
    return " ".join(items)


# Exercise 5
def Canteen(Commands):
  global Queue, HeadPointer, TailPointer
  Queue = [-1] * 8
  HeadPointer = 0
  TailPointer = -1
  served = []

  for command in Commands:
    if command == "serve":
      student = Dequeue()
      if student != -1:
        served.append(student)
    else:
      name = command.split(" ")
      Enqueue(name)

return served
