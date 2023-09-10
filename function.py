def trialfunction():
    print('hello')

trialfunction()

def x_function(x):
    print(x+"hello")

x_function("poora ")

a="8"
b="9"
print(a+b)

def xy_function(x,y):
    print(x+" "+y)
xy_function("nayinte","mone")

def tony(name,age):
    print('my name is '+name+ ' age:'+str(age))
tony('Tony',22)

def hey(*val): # you can add infinite arguements by uding *
    print('a:'+val[0]+' b:'+val[1]+' c:'+val[2])

hey('dad','tony','mom')