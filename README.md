# Exercise 4.14 Multiplier

Create a class Multiplier that has a:

- Constructor `def __init__(self, number)`.
- Method `def multiply(self, number)` which returns the value `number` passed to it multiplied by the `number` provided to the constructor.

You also need to create an instance variable in this exercise.

An example of the class in use:

```python
multiply_by_three = Multiplier(3)

print("multiply_by_three.multiply(2): " + multiply_by_three.multiply(2))

Multiplier multiplyByFour = new Multiplier(4)

print("multiply_by_four.multiply(2): " + multiply_by_four.multiply(2))
print("multiply_by_three.multiply(1): " + multiply_by_three.multiply(1))
print("multiply_by_four.multiply(1): " + multiply_by_four.multiply(1))
```

Output:

```plaintext
multiplyByThree.multiply(2): 6
multiplyByFour.multiply(2): 8
multiplyByThree.multiply(1): 3
multiplyByFour.multiply(1): 4
```
