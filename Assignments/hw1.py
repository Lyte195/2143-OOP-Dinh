""""
Name: Luong Dinh
Email: ldinh195@gmail.com
Assignment: Homework 1 - List and Dictionaries
Due: 19 Sep @ 1:00 p.m.
""""
""" A """
a = [1, 5, 4, 2, 3]
print(a[0], a[-1])
# Prints: 1, 3.

a[4] = a[2] + a[-2]
print(a)
# Prints: 1, 5, 4, 2, 9

print(len(a))
# Prints: 5

print(4 in a)
# Prints: 1

a[1] = [a[1], a[0]]
print(a)
# Prints: 6

""" B """
def remove_all(el, lst):
    # for el in lst
    for(n = 0, n < len(lst), n++)
        if (lst[n] == el)
            remove(lst[n])

""" C """
def add_this_many(x, y, lst):
    b = 0    
    for(m = 0, m < len(lst), m++)
        if (list[m] == x)
            b++
    for(v = 0, v < b, v++)
        lst.append(y)


""" D """
a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: 3, 1, 4, 2

print(a[1::2])
# Prints: 1, 2, 3

print(a[4:2])
# Prints: 4

print(a[1:-2])
# Prints: 1, 4, 2, 5, 3, 3

print(a[::-1])
# Prints: 3, 3, 5, 2, 4, 1

""" E """
# Why is the "in place" solution preferred?
# Because u can just swith the first item with the last,
# then the next first and last and so on,
# so it is easier and faster.


""" H """
print('colin kaepernick' in superbowls)
# Prints: Error

print(len(superbowls))
# Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
# Prints: 4

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
# Prints: { 'giants', 'eli mannning': 2,'peyton manning': 4, 'tom brady': 3, 'joe flacco': 1, 'joe montana': 4}

superbowls[3] = 'cat'
print(superbowls)
# Prints: { 'giants', 'eli mannning': 2,'peyton manning': 4, 'cat': 3, 'joe flacco': 1, 'joe montana': 4}

superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
# Prints: { 'giants','eli mannning': 2,'peyton manning': 8, 'cat': 3, 'joe flacco': 1, 'joe montana': 4}

superbowls[['steelers', '49ers']] = 11
print(superbowls)
# Prints: { 'steelers', '49ers': 11,'giants','eli mannning': 2,'peyton manning': 8, 'cat': 3, 'joe flacco': 1, 'joe montana': 4}

""" I """
def replace_all(d, x, y):
    for k in d.keys():
        if( k == x)
            k = y

""" J """
#http://stackoverflow.com/questions/29639852/delete-all-instances-of-an-element-in-a-python-dictionary-values
c = [x]
for q,v in d.items():
    for i n c:
        v.remove(i)