class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')

print(s1.flavor)
for one_scoop in [s1, s2, s3]:
    print(one_scoop.flavor)

class Person(object):
    def __init__(self, name, email, number):
        self.name = name
        self.email = email
        self.number = number
p1 = Person('John', 'dsd@gmail.com', '1489812452')
p2 = Person('May', 'dgse@live.com', '7543457423')

print(p1.name)


