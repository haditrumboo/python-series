class Train:
    def __init__(self, name):
        self.name = name
        self.total_seats = 100
        self.fare = 500

    def book(self):
        choice = input("Want to book ticket? y/n: ")

        if choice.lower() == "yes" or choice.lower() == "y":
            if self.total_seats > 0:
                self.total_seats -= 1
                print(f"{self.name}, your seat is booked.")
            else:
                print("No seats available.")
        else:
            print("Thank you.")

    def status(self):
        print(f"Available seats: {self.total_seats}")

    def get_fare(self):
        print(f"Ticket fare: ₹{self.fare}")


t = Train("Hadi")
t.book()
t.status()
t.get_fare()