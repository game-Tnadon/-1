w = [2, 5, 10 ,5]
v = [20, 30, 50, 10]
W = 16
RemainingCapacity = W
currentValue = 0

#for i in w:
#    print(i)
for i in range(len(w)) :
    print(w[i])
for j in range(len(v)):
    print(v[j])

for i1 in range(2):
    for i2 in range(2):
        for i3 in range(3):
            for i4 in range(4):
                #if (i1 != i2) and (i1 != i3) and (i1 != i4) and (i2 != i3) and (i2 != i4) and (i3 != i4):
                if i1 != 0:
                    currentValue += v[i1]
                if i2 != 0:
                    currentValue += v[i2]
                if i3 != 0:
                    currentValue += v[i3]
                if i4 != 0:
                    currentValue += v[i4]
                print(i1, " ", i2, " ", i3, " ", i4, " val = ", currentValue)
