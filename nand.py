a = float(input("a: " , ))
b = float(input("b: " , ))
c = float(input("c: " , ))

def polsk(): #
    if b+c == 0 and a == 0:
        return 1
    else:
        return 0

def polak():
    if b == 1:
        return 0
    if b == 0:
        return 1

def vodka():
    if (a + polak()) == 1:
        return 0
    else:
         return 1

def pv():
    if vodka() + polak() == 1:
        return 1
    else:
        return 0

q = pv()
print(q)
