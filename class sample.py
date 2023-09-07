class friends:
    year=2023
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def add_age(self):
        self.age+=1
    def relocate(self,place):
        self.place=place
    def display(self):
        print('year: '+str(friends.year))
        print('name: '+self.name)
        print('age: '+str(self.age))
        print('place: '+self.place)

    @classmethod
    def add_year(cls):
        cls.year+=1


x=friends("Tony",22,"malappuram")
y=friends("x",23,"erenakulam")

friends.year+=1


x.display()
y.display()

print('-----------------------------------')

x.add_age()
y.add_age()
x.display()
y.display()

print('----------------------------------------------------------')

friends.add_year()
x.add_age()
y.add_age()
x.relocate('kozhikode')
x.display()
y.display()


