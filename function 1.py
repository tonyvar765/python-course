val = 10 #global variable
def sample():
    val=30
    print(val) #local variable
sample()
print(val)

def gy(name,age=67):
    print(name,age)

gy(name='hi')
gy(age=12,name='Tony')