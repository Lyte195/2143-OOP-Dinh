# Luong Dinh
Due: December 9.

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
