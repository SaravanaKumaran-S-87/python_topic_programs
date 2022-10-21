#we can create a class like this

Test = type('Test',(),{"x":5})     #name of the class is should be spelled same for left side of equal sign and right side of equal sign here the name is inside of brackets 
t=Test()
t.wy="hello" #we can add the attributes or variables to the class  like this
print(t.wy)
print(t.x)



"""

def add_attribute(self):  #this is separate function we are going to define this funtion to a class test
        self.z=9
        print(self.z)
        
class foo :                  # this is a separate class we are going to inherit this class to a class test
    def show(self):
        print("hi")

test=type('test',(foo,),{'x':5 , 'y':4 ,"add_attribute":add_attribute})       #here we are inherited the class and added the name of the function to access the
t=test()                                                                                                                                       # function as own function
print(t.x)  
print(t.y)
t.add_attribute()             #calling the method of test class to assuming the value of z inside of method like we before added tim.addweight(10) and print z value
print(t.z)



"""
"""metaclass is class that is above the class  we are creating ourselves ,if we create a class
example like Dog all the information like syntax everything is passed to meta class
,it takes that and returns you the object that represents the class because normally in
python class is a object .


class Dog:
     pass
def func():
     pass


print(type(Test()))
print(type(Test))  
print(type(func))
print(type(3))

output:

<class'__main__.Test'> #this is a class object because class is a object in python
<class'type'>           # but here the class is a type, type is the  metaclass that defines the rules for everyclass to be constructed ,if not the rules follwed by
<class'function'>        the class ,the class cannot not be created. in above output the class is created as object , because  type is the main class i.e) metaclass
<class'int'>           it produced the Test() class as a object . we can create a metaclass with name like Test but we should extend or inherit the type class called
                        " type " like in the below program.

     """



"""class Meta(type):
    def __new__(self,class_name,bases,attrs):
        print(attrs)
        return type(class_name,bases,attrs)



class Dog(metaclass=Meta):
    x=5
    y=8


d=Dog()
"""

"""

"""
class Meta(type):
        def __new__(self,class_name,bases,attrs):
                print(attrs) # here we are printing the name of  variables and function of Dog class before it is going to be changed to upper case letter

                a={}
                for name, value in attrs.items():
                        if name.startswith("__"):
                                a[name]=value
                        else:
                                a[name.upper()]=value
                print(a)  # now the name of the variables  and function is changed here ,we are overiding the build in function of python             
                print(self) # printing the name of this class     
                return type(class_name,bases,a) #  here the attrs  dictionary is changed as " a "  because we changed the name of variables and function 
                                                        #to capital letters and put into a new dictionary called "a" and return to the dog class or whatever 
                                                           #class or everyclass we are creating here 

class Dog(metaclass=Meta):     # (metaclass=Meta) this will do that this class should be create with the rules of metaclass i.e) Meta . Meta is the metaclass for
                               # this dog class to create . in metaclass we are doing that all the attributes like variables , functions  and all the name should 
        x=5                    # be in capital letters if not it will automatically cahnged to capital letters. if we print a variables x in small letters it will not
        y=8                    # work ,it will work if we type a variable x in capital letter.

        def hello(self):
                print("hi")

d=Dog()
print(d.Y)
d.HELLO()     #if we small letters of hello here it won't work
                                
t=Meta("cat",(),{"r":0})  # this is the simplest form of creating a class by rules of Metaclass "Meta"
print(t.R)
""" by this type of creating a metaclasss we can do anything with the class ,we can eleminate the bases i.e) inheritance or anything we can do here we are
defining that every variable and function should be in capital letters"""
