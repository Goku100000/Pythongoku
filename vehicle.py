class vehicle:
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model

    def power(self):
        raise NotImplemented("Child classes must implement this method")


class Subaru(vehicle):
    def power(self):
        return "vruum!"


class Mercedes(vehicle):
    def power(self):
        return "geegee!"


class Chevroulet(vehicle):
    def power(self):
        return "boom!"


subaru = Subaru("Legacy", "Vice-675")
print(subaru.Brand)
print(subaru.Model)
print(subaru.power())

mercedes = Mercedes("Benz-bank", "Maybach")
print(mercedes.Brand)
print(mercedes.Model)
print(mercedes.power())

chevroulet = Chevroulet("Bolt EUV", "Colorado")
print(chevroulet.Brand)
print(chevroulet.Model)
print(chevroulet.power())
