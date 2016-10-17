# Luong Dinh
# OOP Repeat
Due: Oct 17<sup>th</sup> by class time.

### Questions

**1)** What does Python print for each of the following:

```python 
johns_bag = Bag()
johns_bag.print_bag()
# what prints?

for color in [’blue’, ’red’, ’green’, ’red’]:
    johns_bag.add_skittle(Skittle(color))
johns_bag.print_bag()
# what prints?

s = johns_bag.take_skittle()
print(s.color)
# what prints?

print(johns_bag.number_sold)
# what prints?

print(Bag.number_sold)
# what prints?

soumyas_bag = Bag()
soumyas_bag.print_bag()

print(johns_bag.print_bag())
# what prints?

print(Bag.number_sold)
# what prints?

print(soumyas_bag.number_sold)
# what prints?
```

### Answer 1

```python
johns_bag = Bag()
johns_bag.print_bag()
# []

for color in [’blue’, ’red’, ’green’, ’red’]:
    johns_bag.add_skittle(Skittle(color))
johns_bag.print_bag()
# ['blue', 'red', 'green', 'red']

s = johns_bag.take_skittle()
print(s.color)
# blue

print(johns_bag.number_sold)
# 1

print(Bag.number_sold)
# 1

soumyas_bag = Bag()
soumyas_bag.print_bag()

print(johns_bag.print_bag())
# ['red', 'green', 'red']

print(Bag.number_sold)
# 2

print(soumyas_bag.number_sold)
# 2

```

**2)**  Write a new method for the Bag class called take color, which takes a color and
removes (and returns) a Skittle of that color from the bag. If there is no Skittle
of that color, then it returns `None`.

```python
def take_color(self, color):



```


### Answer 2

```python
    def take_color(self,color):
    	for s in range (len(self.skittles)):
    		if self.skittles[s] == color:
    			return self.skittles.pop(s)
    		else:
    			return(None)

```

**3.** Write a new method for the Bag class called take all, which takes all the Skittles
in the current bag and prints the color of the each Skittle taken from the bag.

```python
def take_all(self):




```

### Answer 3

```python
    def take_all(self):
    	nl = []
    	nl.extend(self.skittles)
    	print(list(set(nl) - set(self.skittles)))

```
