Apple = set()
#print(Apple)

Fruits = {"Apple", "Banana", "Orange", "Pear"}

numbers = [1, 5, 700000, 3, 5]
Number = set(numbers)
print (Number)
#you can make a set from a list, a tuple or a string

#print(Number[3]) #sets CANNOT have index

#check if an element exists in the set
if 3 in Number:
    print("yes")
else:
    print("no")

#adding element to the set
Apple.add(15)
Apple.add(578)
Apple.add(1)
print(Apple)

#removing element from the set
Apple.remove(578)
Apple.discard(1)
print(Apple)
#if 'remove' gets rid of something that isn't there, it causes an error but if 'discard' does the same, nothing happens
#'pop' function removes a random element
#'clear' function removes all elements

#set operations - union, intersection, difference, symmetric difference
#union is adding sets
#intersection is the common elemets between 2 sets
#difference of set 'a' and set 'b' is the eleents that exist in 'a' but not 'b'
#symmetric difference is the union of sets minus the intersection of sets

seta = {1, 2, 3, 4}
setb = {3, 4, 5, 6}
print(seta|setb)
print(seta&setb)
print(seta-setb)
print(seta^setb)
