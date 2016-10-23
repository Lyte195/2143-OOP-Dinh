# Luong Dinh
# Ineritance
Due: Oct 24<sup>th</sup> by class time.

### Questions

***1.*** Implement the `Cat` class by inheriting from the `Pet` class. Make sure to use superclass
methods wherever possible. In addition, add a `lose_life` method to the `Cat` class.

### Answer
```python
class Cat(Pet):
	def __init__(self, name, owner, lives=9):
		Pet.__init__(self, name, owner)
		self.lives = lives
	
	def talk(self):
		print('meow')
		
    	def lose_life(self):
         	if self.lives < 1:
            	is_alive =  false
		else:
		    self.lives-=1
    
```

***2.*** Assume these commands are entered in order. What would Python output?

### Answer
```python
class Foo(object):
    def __init__(self, a):
        self.a = a
    def garply(self):
        return self.baz(self.a)
        
class Bar(Foo):
    a = 1
    def baz(self, val):
        return val
        
f = Foo(4)
b = Bar(3)
print(f.a)
# 4

print(b.a)
# 3

print(f.garply())
# 'Foo' object has no attribute 'baz'

print(b.garply())
# 3

b.a = 9
print(b.garply())
# 9

f.baz = lambda val: val * val
print(f.garply())
# 16
```
