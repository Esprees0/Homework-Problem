class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.is_reserved = False
        self.booked_by = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, seat):
        new_seat = Node(seat)
        if not self.head:
            self.head = new_seat
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_seat

class Theater:
    def __init__(self):
        self.seat_list = LinkedList()
        for i in range(1, 16):
            self.seat_list.append(Seat(i))

    def display_seats(self):
        current = self.seat_list.head
        while current:
            print(f"Seat {current.data.seat_number}: Reserved - {current.data.is_reserved}")
            if current.data.is_reserved:
                print(f"Booked by: {current.data.booked_by}")
            current = current.next

    def reserve_seat(self, seat_number, booked_by):
        current = self.seat_list.head
        while current:
            if current.data.seat_number == seat_number and not current.data.is_reserved:
                current.data.is_reserved = True
                current.data.booked_by = booked_by
                print(f"Seat {seat_number} reserved by {booked_by}")
                return
            current = current.next
        print(f"Seat {seat_number} is not available for reservation.")

    def cancel_reservation(self, seat_number):
        current = self.seat_list.head
        while current:
            if current.data.seat_number == seat_number and current.data.is_reserved:
                current.data.is_reserved = False
                current.data.booked_by = None
                print(f"Reservation for seat {seat_number} canceled.")
                return
            current = current.next
        print(f"Seat {seat_number} is not reserved.")

    def get_available_seats(self):
        available_seats = []
        current = self.seat_list.head
        while current:
            if not current.data.is_reserved:
                available_seats.append(current.data.seat_number)
            current = current.next
        return available_seats

    def get_reserved_seats(self):
        reserved_seats = []
        current = self.seat_list.head
        while current:
            if current.data.is_reserved:
                reserved_seats.append({
                    'seat_number': current.data.seat_number,
                    'booked_by': current.data.booked_by
                })
            current = current.next
        return reserved_seats

# Main Program
theater = Theater()
while True:
    print("\n===== Theater Reservation System =====:")
    print("1: Display avaliable seats")
    print("2: Display reserved seats")
    print("3: Reserve a seat")
    print("4: Cancel reservation")
    print("5: Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        theater.display_seats()
    elif choice == 2:
        reserved_seats = theater.get_reserved_seats()
        if reserved_seats:
            print("Reserved seats:")
            for seat in reserved_seats:
                print(f"Seat {seat['seat_number']}: Booked by {seat['booked_by']}")
        else:
            print("No seats are currently reserved.")
    elif choice == 3:
        seat_number = int(input("Enter seat number to reserve: "))
        booked_by = input("Enter your name: ")
        theater.reserve_seat(seat_number, booked_by)
    elif choice == 4:
        seat_number = int(input("Enter seat number to cancel reservation: "))
        theater.cancel_reservation(seat_number)
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5")