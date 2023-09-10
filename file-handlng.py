f=open("main.py","r")
print(f.read())

print(f.readline(1))#its to print a particular lines of a code
print(f.readline(5))#printts the first s lines

for x in f:
    print(x)

f.close()




