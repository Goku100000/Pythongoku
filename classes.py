class fruits:
    def __init__(self, type, color, price):
        self.fruittype = type
        self.fruitcolor = color
        self.fruitprice = price

    def display(self):
        print(self.fruittype, self.fruitcolor, self.fruitprice)


myobj = fruits("banana", "green", 20)
myobj.display()

class cars:
    def __init__(self,type,color):
        self.type=type
        self.color=color
    def display(self):
        print(self.type,self.color)

myobj=cars("mercedes","blue")
myobj.display()
