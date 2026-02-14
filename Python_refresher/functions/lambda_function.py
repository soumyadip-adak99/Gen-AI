# print odd or even number
even_or_odd = lambda n: n % 2 == 0
print(f"{'Even' if even_or_odd(3) is True else 'Odd'}")

# different way
even_or_odd2 = lambda n: "Even" if n % 2 == 0 else "Odd"
print(even_or_odd2(2))

# Using with List Comprehension
func = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in func:
    print(i(), end=" ")
