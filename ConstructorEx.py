class Hotel:
    """
    hotel_guests Class Level Variable
    """
    def __init__(self):
        self.hotel_guests = []

    def checkin(self, guest_name):
        self.hotel_guests.append(guest_name)
        return self.hotel_guests

    def checkout(self, guest_name):
        self.hotel_guests.pop(self.hotel_guests.index(guest_name))

    def showGuests(self):
        print self.hotel_guests



H = Hotel()
H.showGuests()
H.checkin('Shruthi')
H.checkin('ABC')
H.showGuests()
H.checkout('ABC')
H.showGuests()

print "\n"

H1 = Hotel()
H1.checkin('Shruthi1')
H1.showGuests()