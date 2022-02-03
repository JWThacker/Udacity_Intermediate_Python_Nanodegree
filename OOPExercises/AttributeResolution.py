class MySecondClass:
    favorite_number = 41
    def print_number(number):
        print(number)

### Attribute Resolution on class objects
print(MySecondClass.favorite_number) # This prints out the favorite_number attribute
print(MySecondClass.__dict__['favorite_number']) # This prints out the favorite_number attribute
MySecondClass.print_number(41)

### Attribute resolution on instance objects
class Home:
    layout = 'square'
    def paint(self, color):
        self.color = color

home = Home()
home.size = 3500
### Try to access the size attribute

print(home.size) ### This is valid
# print(home['size']) ### This is invalid, reference types are not subscriptable
# print(home.get('size')) There is no attribute "get"

print(home.__dict__['size'])

# Methods and functions

class House:
    def __init__(self, size, color='white'):
        self.size = size
        self.color = color
    def build_expansion(self, number):
        self.size = self.size + number

home = House(2000)
print(home.size)
home.build_expansion(500)
print(home.size)

# Nuances of attribute resoltution
#class Dog:
#    def __init__(self, name):
#        self.name = name
#        self.tricks = set()
#    def teach(self, trick):
#        self.tricks.add(trick)

#buddy = Dog('Buddy')
#pascal = Dog('Pascal')
#buddy.teach('sit')
#pascal.teach('fetch')
#buddy.teach('fetch')
#print(buddy.tricks)
#print(pascal.tricks)

class Dog:
    def __init__(self, name, tricks = None):
        self.name = name
        self.tricks = set()
        if tricks:
            self.tricks = tricks
    def teach(self, trick):
        self.tricks.add(trick)

buddy = Dog('Buddy')
pascal = Dog('Pascal')
kimber = Dog('Kimber', tricks = {'lie down', 'shake'})
buddy.teach('sit')
pascal.teach('fetch')
buddy.teach('roll over')
kimber.teach('fetch')
print(buddy.tricks)
print(pascal.tricks)
print(kimber.tricks)

class User:
    # An (intentionally shared) collection storing users who sign up for some hypothetical service.
    # There's only one set of members, so it lives at the class level!
    members = []
    def __init__(self, name):
        self.name = name
        self.members = set()  # Not signed up to begin with.
    def sign_up(self):
        User.members.append(self.name)
# Change the code above so that the following lines work:
#
sarah = User('sarah')
heather = User('heather')
cristina = User('cristina')
mark = User('mark')
print(User.members)  # {}
heather.sign_up()
cristina.sign_up()
mark.sign_up()
print(User.members)  # {'heather', 'cristina'}
print(type(User.members))