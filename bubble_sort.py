import time

number_of_items = 0
while number_of_items <= 0:
    number_of_items = int(input("Number of list items: "))

list = []
for i in range(number_of_items):
    item = float(input(f"Input list item ({i}/{number_of_items}): "))
    list.append(item)

list_length = len(list)

comparisons = list_length - 1
swap_made = True

start_time = time.perf_counter()

while comparisons > 0 and swap_made:
    swap_made = False
    for i in range(comparisons):
        if list[i] > list[i + 1]:
            temp = list[i]
            list[i] = list[i + 1]
            list[i + 1] = temp
            swap_made = True
            continue

    comparisons -= 1

end_time = time.perf_counter()
time_taken = end_time - start_time

print(f"Sorted list: {list}")
print(f"Time taken: {time_taken:.6f}s")