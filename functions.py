def mitmorn():
    print("This is MIT Morning class")


mitmorn()
mitmorn()


def calculate():
    x = 7
    y = 10
    print(x * y)
    print(x + y)
    print(x - y)
    print(x / y)


calculate()


def majinas(myfirstname, mylastname, age):
    print(myfirstname + " " + mylastname , age)


majinas("MY NAME IS GEORGE", "JUNGLE", " AND I AM 30YRS OLD")
majinas("My name is Rimuru", "Tempest", "and my age is 200yrs")
majinas("My name is Donald", "Duck", "and my age is 15yrs")
majinas("My mame is Philip", "Kamau", "am 50 yrs old")
majinas("My name is Benimaru", "Yoshiba", "and my age is 25 yrs")

#create  a function tha t will  create the average of a list

#[2,5,6,3,5]
def calculation(numbers):
    total=sum(numbers)
    count=len(numbers)
    average=total/count
    return average

data=[3,6,8,9,2,1,8]
result =calculation(data)
print("calculation",result)











#create a function that give s you the longest stream in  list{palindrome}