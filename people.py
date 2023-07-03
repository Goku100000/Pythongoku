class people:
    def __init__(self,name,age,gender):
        self.peoplename=name
        self.peopleage=age
        self.peoplegender=gender

    def display(self):
        print(self.peoplename,self.peopleage,self.peoplegender)


myobj=people("David Kamau","14","male")
mylist=people("Kipchoge Chege","20","male")
myobj2=people("Rimuru Tempest","40","female")
myobj.display()
mylist.display()
myobj2.display()