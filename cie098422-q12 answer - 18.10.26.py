rooms = []
dimensions = []

# position of the smallest and largest rooms in both arrays
smallest_room = 0
largest_room = 0

total_area = 0

number_of_rooms = 0
while number_of_rooms < 3 or number_of_rooms > 20:
    if number_of_rooms != 0:
        print("Number of rooms must be between 3 & 20!\n")
    number_of_rooms = int(input("Please enter the number of rooms to be added: "))

for i in range(number_of_rooms):
    room_name = input("\nRoom name: ")
    room_width = int(input("Room width: "))
    room_length = int(input("Room length: "))

    rooms.append(room_name)
    dimensions.append([room_length, room_width])

    room_area = round(room_length * room_width, 2)
    print(f"\nName: {room_name} | Area: {room_area} | Width: {room_width} | Length: {room_length}\n")

    if i == 0:
        largest_room = 0
        smallest_room = 0
    elif room_area > (dimensions[largest_room][0] * dimensions[largest_room][1]):
        largest_room = i
    elif room_area < (dimensions[smallest_room][0] * dimensions[smallest_room][1]):
        smallest_room = i

    total_area += room_area

average = total_area / number_of_rooms
print(f"Largest room: {rooms[largest_room]}")
print(f"Smallest room: {rooms[smallest_room]}")
print(f"Total area: {total_area} | Average per room: {average}")