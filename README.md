# Intro to OOP  

What is OOP,
Why OOP. 

How to OOP

### Learning outcomes: 
- 

### Class
What is a class? A class is like a cookie cutter or blue print for objects but not the object itself. 

What can you do with a cookie? 
    -   eat it!
    
### methods 
The actions or how an object behaves. 

So in the above example, .eat_cookie() could be a method inside the class Cookie


### Instance
What is an instance? 

### syntax
```python
class Dog():

    def __init__(self, attri1, attri2, optional_attri='default'):
        self.attribute_1 = attri1,
        self.attribute_2 = attri2,
        self.attribute_3 = optional_attri,

    def method_name(self, arg1):
        # complex block
        arg1 += arg1 + 1 
        return  arg1 
```

### Convention


## OOP 4 Pillars

### Inheritance
The ability of a subclass to inherit all the behaviour and method from parent class. 
One of the core reasons to use OOP, because it means you write less code. In reality this is debatable, has you end-up having to adapt a lot of methods. It also depends how good of a coder you are and ability to abstract effectivly. 

### Abstration 
- good naming
- good documentation - mention what methods and how to use them
- use of inheritance 


#### Polymorthism
- what is class polymorthism?
- what is method polymorthism?


#### Encapsulation 
The ability to limit access from the exterior to method and or attributes.
Hence, making them 'private'. 

```python
class Dog():

    def __init__(self, dog_name, attri2):
        self.name = attri1,
        self.attribute_2 = attri2,
        self.dog_years = 0,
        self.human_years = 0

    def dog_birthday_incrementer(self):
        # complex block
        #  celebrate the dog's bithday 
        # update human year
        # update dog years
        print(f'happy birthday! You are a GOOD BOY! GOOD BOY {self.name}!')
        return self.dog_years 
```
