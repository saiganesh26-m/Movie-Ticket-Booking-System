from booking import BookingSystem

def main():

    system = BookingSystem()

    while True:

        print("\n===== Movie Ticket Booking System =====")
        print("1. View Seats")
        print("2. Book Seat")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.show_seats()

        elif choice == "2":
            seat = input("Enter Seat Number: ")
            system.book_seat(seat)

        elif choice == "3":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()