### Day 2 QA (Questions and Answers)

**1. Lists**

**Q1: How do you create a list in Python and access its elements?**
- **A1:** You create a list using square brackets `[]`. Elements are accessed using their index.
  ```python
  my_list = [1, 2, 3, "hello"]
  first_element = my_list[0]  # --> 1
  last_element = my_list[-1]  # --> 'hello'
  ```

**Q2: How do you add and remove elements from a list?**
- **A2:** Use `append()` to add elements and `remove()` or `pop()` to remove elements.
  ```python
  my_list = [1, 2, 3]
  my_list.append("new item")  # Adds 'new item' to the end
  my_list.remove("new item")  # Removes 'new item'
  item = my_list.pop()  # Removes and returns the last element
  ```

**Q3: How can you sort a list in ascending and descending order?**
- **A3:** Use the `sort()` method to sort the list in place. Use `reverse=True` for descending order.
  ```python
  my_list = [3, 1, 4, 1, 5]
  my_list.sort()  # Sorts in ascending order
  my_list.sort(reverse=True)  # Sorts in descending order
  ```

**4. Tuples**

**Q4: What is the difference between a list and a tuple in Python?**
- **A4:** Lists are mutable (can be changed), while tuples are immutable (cannot be changed once created).

**Q5: How do you concatenate and repeat tuples?**
- **A5:** Use the `+` operator to concatenate and `*` operator to repeat.
  ```python
  tuple1 = (1, 2, 3)
  tuple2 = (4, 5)
  concatenated_tuple = tuple1 + tuple2  # --> (1, 2, 3, 4, 5)
  repeated_tuple = tuple1 * 2  # --> (1, 2, 3, 1, 2, 3)
  ```

**5. Dictionaries**

**Q6: How do you create and access elements in a dictionary?**
- **A6:** Create a dictionary using curly braces `{}`. Access elements using their keys.
  ```python
  my_dict = {"name": "Alice", "age": 30}
  name = my_dict["name"]  # --> Alice
  ```

**Q7: How can you add, update, and remove elements in a dictionary?**
- **A7:** Use assignment to add or update elements. Use `pop()` to remove elements.
  ```python
  my_dict = {"name": "Alice"}
  my_dict["age"] = 30  # Add or update key 'age'
  my_dict.pop("age")  # Remove key 'age'
  ```

**6. Control Flow**

**Q8: How do you use `if` statements to execute code based on a condition?**
- **A8:** Use `if`, `elif`, and `else` statements to conditionally execute code blocks.
  ```python
  age = 20
  if age >= 18:
      print("Adult")
  else:
      print("Minor")
  ```

**Q9: What is the difference between a `for` loop and a `while` loop in Python?**
- **A9:** A `for` loop iterates over a sequence (e.g., list, range), while a `while` loop runs as long as a condition is `True`.
  ```python
  # For loop
  for i in range(5):
      print(i)  # Outputs 0 to 4

  # While loop
  count = 0
  while count < 5:
      print(count)  # Outputs 0 to 4
      count += 1
  ```

Feel free to ask if you need more questions or further clarification!