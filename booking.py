class BookingSystem:

    def __init__(self):

        self.seats = {
            "A1": False,
            "A2": False,
            "A3": False,
            "A4": False
        }

    def show_seats(self):

        print("\nSeat Status")

        for seat, booked in self.seats.items():

            if booked:
                print(seat, "-> Booked")
            else:
                print(seat, "-> Available")

    def book_seat(self, seat):

        if seat not in self.seats:
            print("Invalid Seat")
            return

        if self.seats[seat]:
            print("Seat Already Booked")
            return

        self.seats[seat] = True
        print("Booking Successful")