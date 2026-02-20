#  what is oop
# OOP is abject oriented programming, where in place of writing functions and variables we use classes and objects.
# it help to have our code DRY: DONT REPEAT YOURSELF.

# what is class,object,properties and methods, inheritance, 
# Class is like a blueprint, and object is an instance of the class
# properties -> attributes -> variables inside class
# methods -> behaviour -> functions inside class
# self -> self is a reference to the current instance of the class.
# what is constructor? -> it is a special method that is called (by itself) when an object is created.

# class MyClass:
#     x = 5
# p = MyClass()
# print(p.x)


class Students:
    s_list = ['ram','shyam','hari']

    def show(self):
        for name in self.s_list:
            print(self,name)

    def add(self,name):
        self.s_list.append(name)

    def delete(self, index):
        pass

    def update(self, index,name):
        pass

s = Students()
s.add('kusum')
s.show()


# setter and getter -> private ko value lina cha vane setter and getter garera lina sakincha.


# what is inheritance? -> 
# database = mysql, postgrel, sqlite
# import jason