def bus_seat_checker(passenger_name,seat_number):
    if seat_number > 50:
        return f" sorry {passenger_name} seat is full."
    else:
        return f" {passenger_name} is sit in the {seat_number} "
    
passenger1 = bus_seat_checker("kritika",12)
print(passenger1)

passenger2 = bus_seat_checker("manvi",65)
print(passenger2)