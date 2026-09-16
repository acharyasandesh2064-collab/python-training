grades = [85, 92, 78]
grades.append(95)
grades.remove(78)
if 92 in grades:
    print("92 is in the list of grades.")
    total_count = len(grades)
    total_sum = sum(grades)
    lowest = min(grades)
    highest = max(grades)
    print("sum=",total_sum)
    print("count=",total_count)
    print("lowest=",lowest)
    print("highest=",highest)
