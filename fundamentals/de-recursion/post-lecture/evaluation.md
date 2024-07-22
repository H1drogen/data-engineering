# Recursion 101

## Post lecture evaluation

Below are a series of tasks designed to make you _think_ and _engage_ more actively with the content you have just seen in your lecture. An essential prerequisite to writing any good code is being able to learn well and thoroughly - to do this you need to interrogate what you are learning properly. Thinking critically is something we are going to encourage you to do from the very beginning and these questions are designed to help you with the process of rigorous analytical thinking.

​
These questions are _not_ part of an assessment and nor are they an attempt to catch you out. A well posed question ( we hope ) is one that is designed to make you think. And if you are struggling to answer the questions below - well, that's good, it means you are on the verge of learning something new!
​

---

### Task 1

```py
def print_sequence(n):
    if n == 1:
        print(f'The current value in the sequence is {n}! End of sequence')
        return

    print(f'The current value in the sequence is {n}')

    if n % 2 == 0:
        print_sequence(n / 2)
    else:
        print_sequence(3 * n + 1)

```

a: Work out what will be printed to the `console` when `print_sequence` is invoked with `10`, e.g. `print_sequence(10)`</br>

b: Work out what will be printed to the `console` when `print_sequence` is invoked with `8`, e.g. `print_sequence(8)`</br>

c: What is the **base case** in the function above ?</br>

d: How is `print_sequence` moving towards the **base case** ?

---

### Task 2

```py
def recursive_double_list(input_list, new_list):
    if len(input_list) == 0:
        return new_list

    first_item = input_list[0]
    new_list.append(first_item * 2)
    left_over_list = input_list[1:]
    return recursive_double_list(left_over_list, new_list)
```

a: What will `recursive_double_list([1,2,3],[])` evaluate to ?</br>

b: What is the **base case** for `recursive_double_list` ?</br>

c: How does `recursive_double_list` move towards the base case ?
