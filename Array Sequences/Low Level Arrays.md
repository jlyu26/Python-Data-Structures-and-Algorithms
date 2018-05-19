## Referential Arrays

Example: 

100 student names with ID numbers. Use an array of object references , where each element is a **reference** to the object.

<img width="367" alt="referential-arrays-example" src="https://user-images.githubusercontent.com/20265633/40263164-856011ce-5adc-11e8-8094-e45fbea0aebd.PNG">

Like above, we have a list of names where the index is referencing an object. So although the relative size of the individual elements may vary, the number of bits used to store the memory address of each element is fixed. And in this way Python can support O(1) to a list/tuple element based index.

### slice

- When computing the slice of a list, the result is a **new list instance**.
- New list has references to the same elements that are in the origional list. In case like this we don't create new object, we just referencing them.

`temp = primes[3:6]`:

<img width="330" alt="referential-arrays-temp" src="https://user-images.githubusercontent.com/20265633/40262802-a77a4a6c-5ad8-11e8-9bf2-a5ed2e00aabc.PNG">

## reassignment

Like in this case when the elements of the list are immutable objects and integers are immutable, the fact that two lists share elements isn't really significant as neither of them can cause a change to the shared object. So if we do the reassignment, like `temp[2] = 15`, what we're actually doing is just **changing the existing reference**, instead of changing the integer object.

<img width="338" alt="referential-arrays-reference" src="https://user-images.githubusercontent.com/20265633/40262880-6c3eef2e-5ad9-11e8-9996-4d05d7d0f41f.PNG">

## extend

- `primes.extend(extras)`

<img width="456" alt="referential-arrays-extend" src="https://user-images.githubusercontent.com/20265633/40263491-2134e878-5ae1-11e8-8394-5b1a208a3d5c.PNG">

The extend command is used to add all elements from one list to the end of another. The extended list does not receive copies of those elements. Instead it receives the **added references** to those elements.

## Copying Arrays

- `backup = list(primes)`
- This produces a new list that is a **shallow copy**, which **references** the same elements as in the first list.
- If the contents of the list were of a mutable type, a *deep copy* can be produced by using the deepcopy function from the copy module.

<img width="382" alt="python-mutable" src="https://user-images.githubusercontent.com/20265633/40263347-f9e791b4-5ade-11e8-96d7-4307f267fa86.PNG">

- `counter = [0] * 8`
- We're not making eight [0] because reference integer is immutable. So instead, all 8 cells reference the same object!

<img width="358" alt="counters" src="https://user-images.githubusercontent.com/20265633/40263382-8fa1d91c-5adf-11e8-9d5c-f2b152eae4bd.PNG">

- `counters[2] += 1`
- Does not technically change the value of the existing integer instance. This computes a new integer.

<img width="355" alt="counters-immutable" src="https://user-images.githubusercontent.com/20265633/40263436-35efb870-5ae0-11e8-90d6-5bf4547d9d6c.PNG">