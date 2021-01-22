"""OOP examples for module 2"""

import pandas as pd

class MyDataFrame(pd.DataFrame): #inheritance notation, from the pandas library
    def num_cells(self):
        return self.shape[0] * self.shape[1] #this is a method, so we don't need a constructor
        """returns number of cells in a dataframe"""

class BareMinimumClass: #Capitalize first letter of each word for every class
    pass #we're not doing anything now, don't return any errors

class Complex:
    def __init__(self, realpart, imagpart):#init = constructor
        """
        Constructor for complex numbers.
        Complex numbers have a real part and imaginary part.
        """
        self.r = realpart #object created from class template has attribute r. Self referencing the object.
        self.i = imagpart #these are attributes that you can now call

    def add(self, other_complex): #create a method
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return '({}, {})'.format(self.r, self.i) #brackets will fill in self.r and self.i, respectively
        """
        shows values of self.r and self.i class
        """

class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def receive_upvotes(self, num_upvotes=1)
        self.upvotes += num_upvotes

    def is_popular(self): #boolean true/false, so used 'is'
        return self.upvotes > 100


class Animal:
    """General Representation of Animals"""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type

    def run(self):
        return "Vroom, Vroom, I go quick"

    def eat(self, food):
        return "Huge fan of that " + str(food)

class Sloth(Animal): #inheriting Animal to the Sloth class
    def __init__(self, name, weight, diet_type, num_naps_):
        super().__init__(name, weight, diet_type) #super refers to the parent class
        self.num_naps = int(num_naps)

    def say_somthing(self):
        return "This is a sloth of typing"

    def run(self):
        return "I am a slow sloth guy" #this will override the Animal class run()

if __name__ == '__main__': #tells python the code inside here should only be executed if we run this module oop_example.py"
    num1 = Complex(3, 5) #created two objects
    num2 = Complex(4, 2)
    num1.add(num2)
    print(num1.r, num1.i)

    user1 = SocialMediaUser('Justin','Provo')
    user2 = SocialMediaUser('Nick','Logan',200)
    user3 = SocialMediaUser('Carl','Costa Rica',upvotes=100000)
    user4 = SocialMediaUser('George Washington','Djibouti', 2)
    print('name: {}, is popular: {}, num upvotes: {}'.format(user4.name, user4.ispopular(), user4.upvotes))
    #.is_popular() needs parentheses, .upvotes doesn't need it.
    #diff between method() and attribute.
    print('name: {}, is popular: {}, num upvotes: {}'.format(user3.name, user3.is_popular(), user3.upvotes))