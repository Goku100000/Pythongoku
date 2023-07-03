# list datastructure
# a list enables you to change data
myclassmate = ["Eric", "Joan", "Susan", "Purity", "Daniel"]
mynos = [4, 9, 20, 3, 1, 50, -9]
myclassmate[0] = "Goku"
mynos.sort()
myclassmate.append("Christine")
myclassmate.insert(2, "Michael")
myclassmate.pop(1)
print(myclassmate)
print(mynos)

# loops
for name in myclassmate:
    print(name)

for numbers in mynos:
    print(numbers)

# this is a tuple
countries = ("Kenya", "Uganda", "Tanzania", "Burundi")
print(countries)

# sets datastructures

cars = {"Toyota", "Nissan", "Mercedes", "Subaru", "Rangerover"}
print(cars)

for models in cars:
    print(models)
for states in countries:
    print(states)

# dictionaries data structure

matunda = {
    "price": 50,
    "color": "Green",
    "Name": "banana"
}
x=matunda["price"]
x=matunda["color"]
x=matunda["Name"]
matunda["shape"]="oval"
matunda["color"]="red"
print(x)
print(matunda)
for fruits in matunda:
    print(fruits)

