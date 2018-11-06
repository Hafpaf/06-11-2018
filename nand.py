'''
a = float(input("a: " , ))
b = float(input("b: " , ))
c = float(input("c: " , ))
'''

table = [[1,1,1], # table with all current posiblilites
        [1,1,0],
        [1,0,1],
        [0,1,1],
        [1,0,0],
        [0,0,0],
        [0,0,1],
        [0,1,0]]

#print(tabel[2])

for row in table: #for loop that runs n amount of times until tables stop
    a = row[0]
    b = row[1]
    c = row[2]
#    print(a,b,c)

    def polsk(): #AND operator
        if b*c == 1:
            return 1
        else:
            return 0

    def or_inv(): #Inverse operator
        if polsk() == 0 and a == 0:
            return 1
        else:
            return 0

    def polak(): #NAND operator
        if b == 1:
            return 0
        else:
            return 1

    def vodka():
        if (a + polak()) == 1: #Inverse OR operator
            return 0
        else:
             return 1

    def pv(): #Inverse OR operator
        if vodka() and or_inv() == 0:
            return 1
        else:
            return 0

    q = pv() #rename variable to q, as the assignment states
    print(row,"=",q) #print which row are used and output
