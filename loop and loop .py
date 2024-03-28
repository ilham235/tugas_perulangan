# 1 1 1 1
# 2 2 2 2
# 3 3 3 3

print ("no 1")
row = 3
col = 4

for i in range (row):
    for f in range (col):
        print (i+1, end=" ")
    print ()
    
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

print ("no 2")
row = 3
col = 4

for i in range (row):
    for f in range (col):
        print (f+1, end=" ")
    print ()
    
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6

print("no 3")
row = 3
col = 4

for i in range (row):
    for f in range (col):
        print (f+1+i, end=" ")
    print ()
    
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15 
# 4 8 12 16 20
# 5 10 15 20 25 

print ("no 4")
row = 6
col = 6

for i in range (1 , row):
    for f in range (1 ,col):
        print (f * i, end=" ")
    print ()

# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5

print ("no 5")

n = 5

for i in range(n, 0, -1):
    for f in range(i, n + 1):
        print(f, end=" ")
    print()

# 1 2 3 4 5 
# 2 3 4 5 
# 3 4 5
# 4 5
# 5

print ("no 6")
n = 5

for i in range(1, n + 1):
    for f in range(i, n + 1):
        print(f, end=" ")
    print()
    
# 1
# 2 3
# 3 4 5
# 4 5 6 7
# 5 6 7 8 9

print ("no 7")

for i in range (1,6):
    for f in range (i, i+i):
        print (f, end=" ")
    print ()
