'''
a = float(input("a: " , ))
b = float(input("b: " , ))
c = float(input("c: " , ))
'''

table = [[1,1,1],
        [1,1,0],
        [1,0,1],
        [0,1,1],
        [1,0,0],
        [0,0,0],
        [0,0,1],
        [0,1,0]]

#print(tabel[2])

for row in table:
    a = row[0]
    b = row[1]
    c = row[2]
#    print(a,b,c)

    def polsk(): #
        if b*c == 1:
            return 1
        else:
            return 0

    def or_inv():
        if polsk() == 0 and a == 0:
            return 1
        else:
            return 0

    def polak():
        if b == 1:
            return 0
        else:
            return 1

    def vodka():
        if (a + polak()) == 1:
            return 0
        else:
             return 1

    def pv():
        if vodka() and or_inv() == 0:
            return 1
        else:
            return 0

    q = pv()
    print(row,"=",q)
