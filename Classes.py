from datetime import datetime

class Hotel:
    """
    Represents a Hotel which consists of multiple rooms and basic details.
    """
    def __init__(self, name, location, city, status, phoneNumber, rating, roomList):
        self._name = name
        self._location = location
        self._city = city
        self._status = status
        self._phoneNumber = phoneNumber
        self._rating = rating
        self._roomList = roomList  # List of Room objects

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getLocation(self):
        return self._location

    def setLocation(self, location):
        self._location = location

    def getCity(self):
        return self._city
    def setCity(self, city):
        self._city = city

    def getStatus(self):
        return self._status
    def setStatus(self, status):
        self._status = status
        
    def getPhoneNumber(self):
        return self._phoneNumber

    def setPhoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber
    def getRating(self):
        return self._rating

    def setRating(self, rating):
        self._rating = rating

    def getRoomList(self):
        return self._roomList
    def setRoomList(self, roomList):
        self._roomList = roomList

    def calculateAverageRating(self):
        # Placeholder for average rating calculation
        return self._rating

    def __str__(self):
        return (f"Hotel: {self._name}\n"
                f"Location: {self._location}, {self._city}\n"
                f"Status: {self._status}\n"
                f"Phone Number: {self._phoneNumber}\n"
                f"Rating: {self._rating}\n"
                f"Rooms Count: {len(self._roomList)}")

class Room:
    """
    Represents a Room in the Hotel.
    """
    def __init__(self, roomNumber, roomType, pricePerNight, amenities, availability, rate):
        self._roomNumber = roomNumber
        self._roomType = roomType
        self._pricePerNight = pricePerNight
        self._amenities = amenities  # List of amenities
        self._availability = availability
        self._rate = rate

    def getRoomNumber(self):
        return self._roomNumber
    def setRoomNumber(self, roomNumber):
        self._roomNumber = roomNumber

    def getRoomType(self):
        return self._roomType
    def setRoomType(self, roomType):
        self._roomType = roomType

    def getPricePerNight(self):
        return self._pricePerNight
    def setPricePerNight(self, pricePerNight):
        self._pricePerNight = pricePerNight

    def getAmenities(self):
        return self._amenities
    def setAmenities(self, amenities):
        self._amenities = amenities

    def getAvailability(self):
        return self._availability
    def setAvailability(self, availability):
        self._availability = availability

    def getRate(self):
        return self._rate

    def setRate(self, rate):
        self._rate = rate

    def checkAvailability(self):
        return self._availability

    def bookRoom(self):
        if self._availability:
            self._availability = False
            return f"Room {self._roomNumber} successfully booked."
        return f"Room {self._roomNumber} is not available."

    def __str__(self):
        return (
            f"Room Info:\n"
            f"Room Number: {self._roomNumber}\n"
            f"Room Type: {self._roomType}\n"
            f"Price/Night: {self._pricePerNight}\n"
            f"Rating: {self._rate}\n"
            f"Available: {self._availability}\n"
            f"Amenities: {', '.join(self._amenities)}")

class Booking:
    """Represents a Room Booking made by a Guest."""
    def __init__(self, bookingId, guest, rooms, checkInDate, checkOutDate, numberOfRooms, totalCharges, status):
        self._bookingId = bookingId
        self._guest = guest
        self._rooms = rooms  # List of Room objects
        self._checkInDate = checkInDate
        self._checkOutDate = checkOutDate
        self._numberOfRooms = numberOfRooms
        self._totalCharges = totalCharges
        self._status = status

    def getBookingId(self): 
        return self._bookingId
    def setBookingId(self, bookingId): 
        self._bookingId = bookingId

    def getGuest(self): 
        return self._guest
    def setGuest(self, guest): 
        self._guest = guest

    def getRooms(self): 
        return self._rooms
    def setRooms(self, rooms): 
        self._rooms = rooms

    def getCheckInDate(self): 
        return self._checkInDate
    def setCheckInDate(self, checkInDate): 
        self._checkInDate = checkInDate

    def getCheckOutDate(self): 
        return self._checkOutDate
    def setCheckOutDate(self, checkOutDate): 
        self._checkOutDate = checkOutDate

    def getNumberOfRooms(self): 
        return self._numberOfRooms
    def setNumberOfRooms(self, numberOfRooms): 
        self._numberOfRooms = numberOfRooms

    def getTotalCharges(self): 
        return self._totalCharges
    def setTotalCharges(self, totalCharges): 
        self._totalCharges = totalCharges

    def getStatus(self): 
        return self._status
    def setStatus(self, status): 
        self._status = status

    def confirmBooking(self): 
        return f"Booking {self._bookingId} confirmed."

    def calculateNumberOfNights(self):
        d1 = datetime.strptime(self._checkInDate, "%Y-%m-%d")
        d2 = datetime.strptime(self._checkOutDate, "%Y-%m-%d")
        return (d2 - d1).days

    def calculateCharges(self):
        nights = self.calculateNumberOfNights()
        total = sum(room.getPricePerNight() for room in self._rooms) * self._numberOfRooms
        self._totalCharges = total
        return total

    def receiveNotification(self): 
        return "Booking confirmation notification sent."

    def __str__(self):
        room_numbers = ", ".join(str(room.getRoomNumber()) for room in self._rooms)  # Join all room numbers
        
        return (
            f"Booking Id: {self._bookingId}\n"
            f"Guest: {self._guest.getName()}\n"
            f"Rooms: {room_numbers}\n"
            f"Number of Rooms: {self._numberOfRooms}\n"
            f"Check-in: {self._checkInDate} | Check-out: {self._checkOutDate}\n"
            f"Number of Nights: {self.calculateNumberOfNights()}\n"
            f"Total: {self._totalCharges}\n"
            f"Status: {self._status}"
        )



class User:
    """
    Base class for any user of the hotel system.
    """
    def __init__(self, userId, name, email, phoneNumber, nationality):
        self._userId = userId
        self._name = name
        self._email = email
        self._phoneNumber = phoneNumber
        self._nationality = nationality

    def getUserId(self):
        return self._userId
    def setUserId(self, userId):
        self._userId = userId

    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name

    def getEmail(self):
        return self._email
    def setEmail(self, email):
        self._email = email

    def getPhoneNumber(self):
        return self._phoneNumber
    def setPhoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber

    def getNationality(self):
        return self._nationality
    def setNationality(self, nationality):
        self._nationality = nationality

    def login(self):
        return f"User {self._userId} logged in."

    def __str__(self):
        return (
            f"User Info:\n"
            f"ID: {self._userId}\n"
            f"Name: {self._name}\n"
            f"Email: {self._email}\n"
            f"Phone Number: {self._phoneNumber}\n"
            f"Nationality: {self._nationality}")


class Guest(User):
    """
    Represents a Guest, inherits from User.
    """
    def __init__(self, userId, name, email, phoneNumber, nationality, loyaltyStatus, bookingsList, loyaltyList, feedbackList):
        super().__init__(userId, name, email, phoneNumber, nationality)
        self._loyaltyStatus = loyaltyStatus
        self._bookingsList = bookingsList  # List of Booking
        self._loyaltyList = loyaltyList    # List of LoyaltyProgram
        self._feedbackList = feedbackList  # List of Feedback

    def getLoyaltyStatus(self):
        return self._loyaltyStatus
    def setLoyaltyStatus(self, loyaltyStatus):
        self._loyaltyStatus = loyaltyStatus

    def getBookingsList(self):
        return self._bookingsList
    def setBookingsList(self, bookingsList):
        self._bookingsList = bookingsList

    def getloyaltyList(self):
        return self._loyaltyList
    def setloyaltyList(self, loyaltyList):
        self._loyaltyList = loyaltyList

    def getFeedbackList(self):
        return self._feedbackList
    def setFeedbackList(self, feedbackList):
        self._feedbackList = feedbackList

    def makeBookings(self, booking):
        self._bookingsList.append(booking)
        return f"Booking {booking} added."

    def viewRewards(self):
        return f"Rewards available: {len(self._loyaltyList)} entries."

    def searchRoomAvailability(self):
        return True

    def addService(self):
        return ["Wifi", "Room Service","Gym Access", "Laundry"]

    def createAccount(self):
        return f"Guest account created for {self._name}"

    def updateProfile(self):
        return f"Profile updated for {self._name}"

    def viewReservation(self):
        return f"You have {len(self._bookingsList)} reservations."
    def __str__(self):
        return (
        super().__str__() + "\n" +
            f"Loyalty Status: {self._loyaltyStatus}\n"
            f"Bookings: {len(self._bookingsList)}\n"
            f"Loyalty Programs: {len(self._loyaltyList)}\n"
        	f"Feedbacks: {len(self._feedbackList)}")

class Admin(User):
    """
    Represents an Admin, inherits from User.
    """
    def __init__(self, userId, name, email, phoneNumber, nationality, role, permissions):
        super().__init__(userId, name, email, phoneNumber, nationality)
        self._role = role
        self._permissions = permissions

    def getRole(self):
        return self._role
    def setRole(self, role):
        self._role = role

    def getPermission(self):
        return self._permissions
    def setPermission(self, permissions):
        self._permissions = permissions

    def manageRooms(self):
        return "Admin is managing rooms."

    def __str__(self):
        return (
            super().__str__() + "\n" +
            f"Admin Info: {self._name}\n"
            f"Role: {self._role}\n"
            f"Permissions: {self._permissions}")

class Payment:
    """Represents a payment made for a booking."""
    def __init__(self, paymentId, amount, paymentMethod, billingAddress, paymentDate, paymentStatus):
        self._paymentId = paymentId
        self._amount = amount
        self._paymentMethod = paymentMethod
        self._billingAddress = billingAddress
        self._paymentDate = paymentDate
        self._paymentStatus = paymentStatus
        self._discount = self._amount * 0.05
        self._additionalCharges = 25.0
        self._finalAmount = self._amount - self._discount + self._additionalCharges
        
    def getPaymentId(self):
        return self._paymentId
    def setPaymentId(self, paymentId):
        self._paymentId = paymentId

    def getAmount(self):
        return self._amount
    def setAmount(self, amount):
        self._amount = amount

    def getPaymentMethod(self):
        return self._paymentMethod
    def setPaymentMethod(self, paymentMethod):
        self._paymentMethod = paymentMethod

    def getBillingAddress(self):
        return self._billingAddress
    def setBillingAddress(self, billingAddress):
        self._billingAddress = billingAddress

    def getPaymentDate(self):
        return self._paymentDate
    def setPaymentDate(self, paymentDate):
        self._paymentDate = paymentDate

    def getPaymentStatus(self):
        return self._paymentStatus
    def setPaymentStatus(self, paymentStatus):
        self._paymentStatus = paymentStatus

    def processPayment(self):
        discount = self._amount * 0.05
        final_amount = self._amount - discount
        additional_charges = 25.0
        total_with_additional = self._amount + additional_charges
        after_discount_total = final_amount + additional_charges

        return (
            f"Total amount: {self._amount}\n"
            f"Total amount with additional charges: {total_with_additional}\n"
            f"After discount Total: {after_discount_total}\n"
            f"Payment {self._paymentId} of amount {after_discount_total} (after 5% discount) processed using {self._paymentMethod}."
        )

    def __str__(self):
        return (
            f"Payment Details:\n"
            f"Payment ID: {self._paymentId}\n"
            f"Original Amount: {self._amount}\n"
            f"Discount (5%): {self._discount}\n"
            f"Additional Charges: {self._additionalCharges}\n"
            f"Final Amount Paid: {self._finalAmount}\n"
            f"Method: {self._paymentMethod}\n"
            f"Billing Address: {self._billingAddress}\n"
            f"Date: {self._paymentDate}\n"
            f"Status: {self._paymentStatus}"
        )


class Invoice:
    """Represents an invoice generated for a booking."""
    def __init__(self, invoiceId, booking, totalAmount, rate, additionalCharges):
        self._invoiceId = invoiceId
        self._booking = booking
        self._totalAmount = totalAmount
        self._rate = rate
        self._additionalCharges = additionalCharges

    def getInvoiceId(self): 
        return self._invoiceId
    def setInvoiceId(self, invoiceId): 
        self._invoiceId = invoiceId

    def getBooking(self): 
        return self._booking
    def setBooking(self, booking): 
        self._booking = booking

    def getTotalAmount(self): 
        return self._totalAmount
    def setTotalAmount(self, totalAmount): 
        self._totalAmount = totalAmount

    def getRate(self): 
        return self._rate
    def setRate(self, rate): 
        self._rate = rate

    def getAdditionalCharges(self): 
        return self._additionalCharges
    def setAdditionalCharges(self, additionalCharges): 
        self._additionalCharges = additionalCharges

    def generateInvoice(self):
        discount = self._booking.getTotalCharges() * 0.05
        after_discount_total = self._booking.getTotalCharges() - discount + self._additionalCharges
        return (
            f"Invoice #{self._invoiceId} generated for booking #{self._booking.getBookingId()}.\n"
            f"Before Discount Total: {self._booking.getTotalCharges()}\n"
            f"Additional Charges: {self._additionalCharges}\n"
            f"Final Total: {after_discount_total}"
        )


    def __str__(self):
        discount = self._booking.getTotalCharges() * 0.05
        final_total = self._booking.getTotalCharges() - discount + self._additionalCharges
        
        return (
          f"Invoice:\n"
          f"Invoice ID: {self._invoiceId}\n"
          f"Booking ID: {self._booking.getBookingId()}\n"
          f"Before Discount Total: {self._booking.getTotalCharges()}\n"
          f"Discount (5%): {discount}\n"
          f"Additional Charges: {self._additionalCharges}\n"
          f"Final Total: {final_total}\n"
          f"Rate: {self._rate}%\n"
    )



class Feedback:
    """Represents guest feedback on the stay."""
    def __init__(self, feedbackId, rating, comments, feedbackDateTime):
        self._feedbackId = feedbackId
        self._rating = rating
        self._comments = comments
        self._feedbackDateTime = feedbackDateTime

    def getFeedbackId(self):
        return self._feedbackId
    def setFeedbackId(self, feedbackId):
        self._feedbackId = feedbackId

    def getRating(self):
        return self._rating
    def setRating(self, rating):
        self._rating = rating

    def getComments(self):
        return self._comments
    def setComments(self, comments):
        self._comments = comments

    def getFeedbackDateTime(self):
        return self._feedbackDateTime
    def setFeedbackDateTime(self, feedbackDateTime):
        self._feedbackDateTime = feedbackDateTime

    def submitFeedBack(self):
        return f"Feedback {self._feedbackId} submitted successfully."
    
    def __str__(self):
        return (
        f"Feedback Id:{self._feedbackId}\n"
        f"Rating: {self._rating}\n"
        f"Comments: {self._comments}\n"
        f"Date: {self._feedbackDateTime}")


class LoyaltyProgram:
    """Represents loyalty program membership for a guest."""
    def __init__(self, loyaltyId, guest, points):
        self._loyaltyId = loyaltyId
        self._guest = guest
        self._points = points

    def getLoyaltyId(self):
        return self._loyaltyId
    def setLoyaltyId(self, loyaltyId):
        self._loyaltyId = loyaltyId

    def getGuest(self):
        return self._guest
    def setGuest(self, guest):
        self._guest = guest

    def getPoints(self):
        return self._points
    def setPoints(self, points):
        self._points = points

    def updateRewards(self, points):
        self._points += points
        return "Rewards updated."

    def displayReward(self):
        return self._points
  
    def __str__(self):
        return (
            f"LoyaltyProgram:\n"
            f"ID: {self._loyaltyId}\n"
            f"Guest: {self._guest.getName()}\n"
            f"Points: {self._points}\n"
            f"Status: {self._guest.getLoyaltyStatus()}\n"
        )


def test_complete_guest_flow():
    print("\n========== Test: Complete Guest Flow ==========")

    # Create rooms and hotel
    room1 = Room(101, "Deluxe", 300.0, ["WiFi", "TV"], True, 4.5)
    room2 = Room(102, "Suite", 500.0, ["WiFi", "Jacuzzi"], True, 4.8)
    hotel = Hotel("Royal Stay", "Corniche", "Doha", "Open", "12345678", 4.7, [room1, room2])
    print(hotel)
    
    # Create admin
    admin = Admin("A001", "Admin Mohammed", "mohammed@royalstay.com", "55667788", "Qatar", "Manager", ["manage_rooms", "view_reports"])
    print("\n-- Admin Info --")
    print(admin)
    
    # Create a guest
    guest = Guest("G001", "Sara", "sara@gmail.com", "971503276556", "Emarati", True, [], [], [])
    print("\n-- Guest Account --")
    print(guest.createAccount())
    print(guest)
    
    # Print room info
    print("\n-- Rooms --")
    print(room1)
    print(room2)
    
    # Make a booking
    number_of_rooms = 2
    booking = Booking(1001, guest, [room1, room2], "2025-03-25", "2025-03-28", number_of_rooms, 0.0, True)
    total_charges = booking.calculateCharges()
    booking.setTotalCharges(total_charges)
    guest.makeBookings(booking)
    print("\n-- Booking --")
    print(booking.confirmBooking())
    for room in [room1, room2]:
        print(room.bookRoom()) #Book each room
    print(booking)

    # Submit feedback
    feedback = Feedback(501, 4.8, "Amazing suite and great service!", datetime.now())
    guest._feedbackList.append(feedback)
    print("\n-- Feedback --")
    print(feedback.submitFeedBack())
    print(feedback)

    # Join loyalty program
    loyalty = LoyaltyProgram(301, guest, 150)
    guest._loyaltyList.append(loyalty)
    print("\n-- Loyalty Program --")
    print(loyalty.displayReward())
    print(loyalty.updateRewards(50))
    print(loyalty)

    # Make a payment
    payment = Payment(9001, total_charges, "Credit Card", "Doha", "2025-03-24", "Completed")
    print("\n-- Payment --")
    print(payment.processPayment())
    print(payment)

    # Generate invoice
    invoice = Invoice(7001, booking, total_charges, 10, 25.0)
    print("\n-- Invoice --")
    print(invoice.generateInvoice())
    print(invoice)

def main():
    test_complete_guest_flow()

if __name__ == "__main__":
    main()
