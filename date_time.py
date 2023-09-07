import datetime
now=datetime.datetime.now()
print(datetime.datetime.now())
print(datetime.date.today())

print(datetime.datetime.now().strftime("%d-%m-%Y"))
print(datetime.date.today().month)

x=datetime.datetime(2023,4,12)
y=datetime.datetime(2023,4,13)
dif= y-x
print(dif)
end = datetime.datetime.now()
diffe = end-now
print(diffe)
