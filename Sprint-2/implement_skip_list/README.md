A [Skip list](https://brilliant.org/wiki/skip-lists/) is a data structure. It is similar to a linked list, but is optimised for being able to quickly insert or find an element in a sorted list. This is a form of pre-computing - we _sort_ the data, and we keep _indexes_ to be able to quickly jump to different points within our data. Doing this pre-computing speeds up the run-time of other operations.

Implement your own skip list. It should support three operations:
* Inserting (which should be faster than O(n))
* Contains checks (which should be faster than O(n))
* Converting to a list (which should be O(n)).

There are some tests in `skip_list_test.py` for your implementation - feel free to write more.
