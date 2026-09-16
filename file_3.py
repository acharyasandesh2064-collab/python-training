number ={4,7,10,18,21}
even_count = 0
odd_count = 0
def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return  "odd"
    for i in number:
        result = check_even_odd(i)
        print(i, "is", result)
        if result == "even":
            even_count += 1
        else:
            odd_count += 1
print(" even numbers:",even_count)
print(" odd numbers:",odd_count)
