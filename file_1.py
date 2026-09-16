number = [4, 7, 10, 18, 21]
total_even = 0
total_odd = 0
def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
for i in number:
    result = check_even_odd(i)
    print(f"{i} is {result}")
    if check_even_odd(i) == "even":
        total_even += 1
    else:
        total_odd += 1
print("Total even numbers:", total_even)
print("Total odd numbers:", total_odd)