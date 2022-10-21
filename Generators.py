#what are the problems can be solved by generators
""" we have a finite amoaunt of memory a finite amount of RAM when we run a program we are storing
things manipulating variables lists all of that . we can store in harddisk but it is slow to operate
the program most of the time we are giong with RAM , if we run the program like this all the amount of memory RAM will
will be full and it shows memory error , we can't do this the numbers are too big

x=[i**2 for i in range(10000000000)]

for el in x:
        print(el)

output :
 memory error



"""
# how do we fix the above problem  we can fix this by using generators
""" generators allow us to essentially to look at one value at a time and not store the
entire sequence of numbers

"""# below program is only a concept of a generator how the generator works ,  python has a in built generator that program is below this program 
"""



class gen:
        def __init__(self,n):
                self.n=n
                self.last=0     # the last number is the first number we are starting with progam in below next() method the self.last is updated and incremented
                                    # so that everytime the program not starts with zero it starts with updated number so that the memory will not get full

        def __next__(self):
                return self.next()
        def next(self):
                if self.last ==self.n:
                        raise StopIteration()  
                rv = self.last**2
             #   print(self.last)   we can do this to note that the number will be updated and in next iteration of the loop comes with a updated value and 
                                     # start squaring the next number of updated value , so it will not start from zero the memory will not get full   
                self.last+=1
                
                return rv
g = gen(1000000000000000000000000000)

while True :
        try:
                print(next(g))
        except:
                break           
#while g.last != g.n :    this also wil be working concept , the next directly calls the dunder method ___next__() not a next() method ,inside of  the dunder method 
     #   print(next(g))              the there is call of next() method so it is called then program is running , every method  and every call will run one time but
                                   #we need sequence of numbers and we can't call the function manually for every number to print so we put the next() call in a while
                                 # loop to call the  __next__ dunder method till the end of the sequence .



"""
"""
In the problem program or error program we are storing all the numbers in a list but now ,
In the above program we are not storing all the numbers in a list , we
don't need to store every  single value ,what we can do is just store you know
almost the last value that we generated  and then using that we can generate the
the next one . we  are restoring all
of the previous values all we are keeping track of the internal state of the next
number we need to generate and this is the idea behind the generators .

Iterator in Python uses the two methods, i.e. iter() and next(). The next() method raises an StopIteration exception
when the next() method is called manually. The best way to avoid this exception in Python is to use normal looping or
use it as a normal iterator instead of writing the next() method again and again.


What does StopIteration mean in Python?
In Python, StopIteration is an exception which occurred by built-in next() and __next__() method in iterator
 to signal that iteration is done for all items and no more to left to iterate.

 What is ITER in Python?
The Python iter() function returns an iterator for the given object. The iter() function creates an object which can be iterated one
element at a time. These objects are useful when coupled with loops like for loop, while loop. The syntax of the
iter() function is: iter(object, sentinel)
"""



"""# MAIN PROGRAM :
# Generator operations:
     #we close  a generator,
     #we can stop a generator ,
     #we can set a values to a ganerator
 
def gen(n):
        for i in range(n):
               # print(i) #we can do this to note that the number will be updated and in next iteration of the loop comes with a updated value and 
                                     # start squaring the next number of updated value , so it will not start from zero the memory will not get full 
                yield i**2 # instead of using the crazy pattern of program like the above program to use generator
                            # concpt , just use this yield keyword it is built in generator in python
               

g=gen(100)

for i in g:
       print(i)

"""


""" we create this generator by creating the function called gen and in the call
function of gen  there is a number whatever number and  what we can do is loop
through the g and what happens when we loop through this it runs the for loop until
it sees this yield keyword so it sees this  yield (i**2) then as soon as it sees that
what it does is it pauses the functions os okay we don't need to run ths anymore
and then it waits until it's called again .so we loop through it again with
this for loop the built in next method of generator is called and then it returns to
us the next yield value and because it's pausing rathan than stopping execution 
. so using the for loop in g , first the zero is called then yield squares and
returns the values then pauses the function then 1 is called called then yield squares and return the value and then pauses
the function like this it will run . we should can again and  again to run the
so we are using the for loop in  g to call again and again till end number .
"""       
"""                
what the yield keyword does is as soon as we hit the yield keyword it returns the value
until wherever this was called from or wherever we looping through and then it pauses
this function so rather stopping the execution of this function which is what a
regular function would do when we hit the return keyword it which means we actually
keep track of what i was so we still know what that number is we still know you know
what n is we still have all of the internal information of this function to store it
in memory we haven't gotten rid of that but we are just pausing when we hit this yield
keyword that's what that means think of yield as like as pause whereas for example
return would be stop of execution 


 for example like we printed the squares till 9 in the top of the package  then  in bottom of package  we call the gen () function and print till 24 square it can start
 using the updated value of 9 square and start from that place to print the 24 square this is how the memory storage consumption is reduced . this is simple numbers but
 if billion number enters it will be hard and the memory storage will get full by this generator we can solve this . YIELD keyword is also return keyword and
 the difference between return keyword and yield keyword is return keyword return the value and stop the execution whereas yield keyword returns the value and pause
 the function and we can call the function to run until it reaches the end value . 
"""
"""
 MAIN PROGRAM UNDERSTANDING :


# here is  the best example for understanding the generator concept using below program , first if we print the call statement it squares and  prints the first value
of 100 i.e)0 then paused and then if we want next number to be squared we  called in second print statement then it goes to next number by using previous number
and likethis we want total 100 numbers to be squared but we need  some values to be printed now afterwards balance values we can print by this . if we want all the
100 numbers to be squared now put the call statement in a for loop or any loop to print.
def gen(n):
        for i in range(n):
                yield i**2 
               

g=gen(100)
print(next(g))
print(next(g))
print(next(g))
print(next(g))


output:
        0
        1
        4
        9

 here is  the best example for understanding the generator concept using below program , first if we print the call statement it squares and  prints the first value
of 100 i.e)0 then paused and then if we want next number to be squared we  called in second print statement then it goes to next number by using previous number
as a first number stored in memory  i.e ) we printed a square of 10 if we call to print 11 square now the program has the memory of last number it printed is 10 square
now it starts from next number of 10 , not starting from 0 and likethis we want total 100 numbers to be squared but we need  some values to be printed now afterwards
balance values we can print by this . if we want all the 100 numbers to be squared now put the call statement in a for loop or any loop to print.

        
"""
"""
def gen(n):
        yield 1
        yield 10
        yield 100
        yield 1000
        yield 10000
               

g=gen(1000000)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


OUTPUT:
1
10
100
1000
10000
eror stopiteration comes here 
"""
"""# same above program we do with for loop 
def gen(n):
        for i in range(n):
                yield 1
                yield 10
                yield 100
                yield 1000
                yield 10000
               

g=gen(1000000)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

Output:
1
10
100
1000
10000
1
10
100
"""
"""here  we should rectify by our own, why the break can't be used inside of a if statement .
class gen:
        def __init__(self,n):
                self.n=n
                self.last=0

        def __next__(self):
                return self.next()
        def next(self):
                if self.last ==self.n:
                        break
                rv = self.last**2
                self.last+=1
                return rv
g = gen(10)
while True :
        try:
                print(next(g))
        except:
             print("stopped")   
print(g.last)              
#while g.last != g.n :
       # print(next(g))
       """



"""
def gen(n):
        for i in range(n):
                yield i**2

g=gen(100)
for i in g :
        if i < 30:
                print(i)
0
1
4
9
16
25

"""# we can see the storage consumption of a list x and generator function variable g
import sys
def gen(n):
        for i in range(n):
                yield i**2

x=[i**2 for i in range(10000)]
g =gen (10000)
print(sys.getsizeof(x))
print(sys.getsizeof(g))

output:
        85176    # this much amount of bytes consumed by list 
         104      #this much amount of bytes consumed by generator  variable g
"""
we can see that this is really optimized way to be able to generate say infinitely
length sequences and when we don't need every single value in the sequence at once
we just need it one at a time which is what we are doing when we say loop through
something then its much better to use a generator to generate this sequence for us  

when you are programming think about say if you are gonna make a massive list like
this with bunch of values do i need all of these values  am i using one value at
a time am i looping through my printing it am i adding it to something or do i only
need say the last value and this value or few values and obviously  you can make
your generators more complicated than a simple for loop you can do some more complex
computation you can start variables inside of here because remember this yield keyword
just  pauses the execution  until when this generator is called and what that means
is that i can loop through this first generator say you five times and then
somewhere later in my program continue looping through it and it will resume where
it left off .

"""

"""

# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

# Output: 4
print(next(my_iter))

# Output: 7
print(next(my_iter))

# next(obj) is same as obj.__next__()

# Output: 0
print(my_iter.__next__())

# Output: 3
print(my_iter.__next__())

# This will raise error, no items left
next(my_iter)
"""
