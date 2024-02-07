'''
Write a Python program that prompts the user for a positive integer `n`, and then calculates the sum of all even numbers between 1 and `n`, inclusive.

Your program should use a loop (either a `for` loop or a `while` loop) to iterate over the numbers between 1 and `n`, and only add the even numbers to the sum.

For example:

```
Enter a positive integer: 10
The sum of even numbers between 1 and 10 is 30.
```

In this example, the even numbers between 1 and 10 are 2, 4, 6, 8, and 10, and their sum is 30.

'''

user_num:int = int(input('Enter a positive integer: '))
even:int = 0
for num in range(1, user_num+1):
    if num % 2 == 0:
        even = even + num

print(f'the sum of even numbers between 1 and {user_num} is {even}')