"""  # main program is #6)
# 1)


def func(string):
        def wrapper():
                print("started")
                print(string)
                print("ended")


        return wrapper()

x=func("hello")


def func(string):
        def wrapper():
                print("started")
                print(string)
                print("ended")


        return wrapper

x=func("hello") #in this the function wrapper is stored in a variable x so now on the name of wrapper funtion is x 
print(x) #in this line we can get the output and note that funtion is stored in variable x ,because functions in python are objects sowe can pass them around 
                                                                                                                            # and  we can store that in variable
x()      # now we can call the wrapper  function like this by the name of x , if we call the wrapper function with the name wrapper() it won't work
t=x()   # like this also we can call wrapper function by assuming the variable t  to x , before that we should call the main function func  and assign any variable
             # and should pass the arguments through the function 
output:
started
hello
ended
<function func.<locals>.wrapper at 0x000002360C6865F0>
started
hello
ended
started
hello
ended
"""




"""
#2)
def func(s):
        def wrapper(x,d):
                print("started")
                s(x,d)
                print("ended")


        return wrapper
def func1(x,d):
        print("i am func1")
        d()

def func2():
        print("iam func2")

x=func(func1)   
x(3,func2)

output:
started
i am func1
iam func2
ended
"""



"""

#3)

here we are passing the function to the wrapper function to print the function ret
return values inside of the wrapper . if we give the funtion name with brackets inside of
a call function "func(func1())" the print statement in func1 is printed first then the wrapper
print statement " started " will be printed.

def func(s):
        def wrapper(x):
                print("started")
                s(x)
                print("ended")


        return wrapper
def func1(x):
        print("i am func1")
        x()

def func2():
        print("iam func2")

x=func(func1)
x(func2)

output:
started
i am func1
iam func2
ended

"""

"""
#4)
def func(s):
        def wrapper():
                print("started")
                s()
                print("ended")


        return wrapper
def func1():
        print("i am func1")
        

def func2():
        print("iam func2")

func1()
func2()
func1=func(func1)
func1()
func2=func(func2)
func2()

output:
i am func1
iam func2
started
i am func1
ended
started
iam func2
ended

"""
"""
#5)
def func(f):
        def wrapper(x):
                print('started')
                f(x)
                print("ended")
        return wrapper
@func
def func1(x):
        print(x)

@func
def func2():
        print("iam func2")

func1(3)   #this is  works like , func1 = func(func1)  
                                # func1(3) like #3 program we are passing arguments
#func2()  here func2() will get error  because it has no arguments ,in wrapper there is a argument for this we come with a solution in below program called
                                             (*args,**kwargs) this is like optional arguments the program works if the call function has with arguments or without
                                             arguments . kwargs is called keyword arguments.

 """       
"""
#6)
def func(f):
        def wrapper(*args,**kwargs):
                print('started')
                rv=f(*args,**kwargs) # here we are asssigning the variable rv to the functions and  return the rv value to the calling function g because in calling 
                print("ended")        #function there is x and y, x is printed  inside the wrapper because x is in print statement but y is a return value 
                                        # if we doesn't assign the value and return value print(g) below the calling function g=func1(5,6) will give output "none"
                return rv               #in below #7 program we are not assigning rv so it gives none .
        return wrapper
@func
def func1(x,y):
        print(x)
        return y
@func
def func2():
        print("iam func2")



func1(5,6)              #this is enough to run but if we want return values we should assign variables like in below line then print that to get return output
g=func1(5,6)
print(g)
func2()   #this is running like this , func2 = func(func2)  
                                     # func2() .



output:
started
5
ended
started
5
ended
6
started
iam func2
ended
"""
"""
               the idea behind the decorators is that we create the main function or decorator function  and check the other function or validating the other
               function or  can adding functionality to that without changing the line of coding with help of decorator function or main function we can also
               add one more decorators over the top of a decorator.
               
"""

def func(f):
        def wrapper(*args,**kwargs):
                print('started')
                f(*args,**kwargs) # here we are not asssigning the variable rv to the functions and  return the rv value to the calling function g because in calling 
                print("ended")        #function there is x and y, x is printed  inside the wrapper because x is in print statement but y is a return value 
                                        # if we doesn't assign the value and return value print(g) below the calling function g=func1(5,6) will give output "none"

        return wrapper
@func
def func1(x,y):
        print(x)
        return y
@func
def func2():
        print("iam func2")




g=func1(5,6)
print(g)

"""
output:
started
5
ended
None

#this is concept example application program , here we are importing time and checking every functions run time by  passing every function to a wrapper function 
#and checking the run time with changing or modifying the test() function just passing and checking like wise we can change the checking rules and passing all 
#the functions to check
import time

def timer(func):
        def wrapper(*args,**kwargs):
                start=time.time()
                rv=func(*args,**kwargs)               
                total=time.time()-start
                print("time:",total)
                return rv
        return wrapper
@timer
def test():
        for _ in range (10000):
                pass

@timer
def test2():
        time.sleep(2)


test()
test2()


#output:
#time: 0.001001119613647461
#time: 2.0145928859710693

"""
         
