ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') # Split the string on a space delimiter
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # Pops first item in the list
    print("Adding: ", next_one) 
    stuff.append(next_one) # add poppped item from more_stuff to stuff
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) # gets item at index 1
print(stuff[-1]) # whoa! fancy # gets second item from the end of hte list
print(stuff.pop()) # prints all of the items in the list
print(' '.join(stuff)) #what? super cool
print('#'.join(stuff[3:5])) # Joins items at index 3 - 5 in the list