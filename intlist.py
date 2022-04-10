'''
a) [10 pts] Instantiate the Stat class with a constructor that accepts a list of integers.

Each instantiated object should have two attributes: length and items.

The length returns the number of elements of the object, and the items attribute returns the content of the list.

For example, if objStat = Stat([5, 3, 7, 3, 6, 4, 5, 8, 2, 9, 3, 4, 20, -10])
then the length should be 14 and the items [5, 3, 7, 3, 6, 4, 5, 8, 2, 9, 3, 4, 20, -10]

b) (10 Points) Define and implement a mutator method named sortStat as a member of the Stat class.
The sortStat method sorts the items attribute elements in ascending order. Use the insertion sort algorithm for this task.

For example, if objStat = Stat([5, 3, 7, 3, 6, 4, 5, 8, 2, 9, 3, 4, 20, -10]) then after invoking the sortStat method,
the items attribute will be [-10, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 20]


c)(10 Points)** Define and implement an accessor method named *belongStat* method as a member of the **Stat** class.
The *belongStat* method accepts an integer and returns True if the number exists in the `items` list;
otherwise, the method should return False. Use the binary search algorithm for this task.

For example, if `objStat = Stat([5, 3, 7, 3, 6, 4, 5, 8, 2, 9, 3, 4, 20, -10])` and the user invoked the the
`belongStat()` method with `8`, then the method will return `True`.
'''
