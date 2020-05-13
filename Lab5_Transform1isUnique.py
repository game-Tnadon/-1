def bruteForce(d):
    size = len(d)
    for pos in range(size):
        val = d[pos]
        col = pos + 1
        while (col < size):
            if d[pos] == d[col]:
                return False
            col += 1
    return True

def pythonInOperator(d):
    i = 0
    for val in d:
        i += 1
        if val in d[i:]:
            return False
    return True

def pythonSet(d):
    if len(set(d)) == len(d):
        return True
    return False

def transformAndConquer(d):
    e = d[:]    #break e from d
    e.sort()
    #print(e)
    #print(d)
    i = 0
    



    return True

data1 = [3, 6, 7, 4, 4, 8, 1, 3, 4]
data2 = [3, 6, 7, 4, 5, 8, 1, 9, 2]
    
if bruteForce(data1):
    print("BF Data1 --> Unique")
else:
    print("BF data1")
if bruteForce(data2):
    print("BF Data2 --> Unique")
else:
    print("BF data2")

if pythonInOperator(data1):
    print("InOp Data1 --> Unique")
else:
    print("InOp data1")
if pythonInOperator(data2):
    print("InOp Data2 --> Unique")
else:
    print("InOp data2")

if pythonSet(data1):
    print("Set Data1 --> Unique")
else:
    print("Set data1")
if pythonSet(data2):
    print("Set Data2 --> Unique")
else:
    print("Set data2")

if transformAndConquer(data1):
    print("Transform Data1 --> Unique")
else:
    print("Transform data1")
if transformAndConquer(data2):
    print("Transform Data2 --> Unique")
else:
    print("Transform data2")

print(data1)
print(data2)