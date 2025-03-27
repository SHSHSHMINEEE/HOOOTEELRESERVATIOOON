from datetime import datetime # Import datetime module for handling date operations

class Hotel:
    """
    Represents a Hotel which consists of multiple rooms and basic details.
    """
    def __init__(self, name, location, city, status, phoneNumber, rating, roomList):
        self._name = name # Hotel name
        self._location = location # Specific location or street
        self._city = city # City where the hotel is located
        self._status = status # Operational status of the hotel (e.g., Open, Closed)
        self._phoneNumber = phoneNumber # Contact phone number for the hotel
        self._rating = rating # Overall rating of the hotel
        self._roomList = roomList  # List of Room objects

    def getName(self):
        return self._name # Return the hotel name

    def setName(self, name):
        self._name = name # Set a new name for the hotel

    def getLocation(self):
        return self._location # Return the hotel's location

    def setLocation(self, location):
        self._location = location # Set a new location for the hotel

    def getCity(self):
        return self._city # Return the hotel's city
    def setCity(self, city):
        self._city = city # Set a new city for the hotel

    def getStatus(self):
        return self._status # Return the hotel's status
    def setStatus(self, status):
        self._status = status # Set a new operational status for the hotel
        
    def getPhoneNumber(self):
        return self._phoneNumber # Return the hotel's phone number 
    def setPhoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber # Set a new phone number
        
    def getRating(self):
        return self._rating # Return the hotel rating
    def setRating(self, rating):
        self._rating = rating # Set a new rating for the hotel

    def getRoomList(self):
        return self._roomList # Return list of rooms in the hotel
    def setRoomList(self, roomList):
        self._roomList = roomList # Set a new list of rooms

    def calculateAverageRating(self):
        # Placeholder for average rating calculation
        return self._rating # Return average rating (placeholder, not actually calculated)

    def __str__(self):
        # Return string representation of the hotel object
        return (f"Hotel: {self._name}\n" #Show Hotel name
                f"Location: {self._location}, {self._city}\n" #Show location and the City
                f"Status: {self._status}\n" #Show status
                f"Phone Number: {self._phoneNumber}\n" #Show phone number
                f"Rating: {self._rating}\n" #Show rating
                f"Rooms Count: {len(self._roomList)}") #Show which room is booked 

class Room:
    """
    Represents a Room in the Hotel.
    """
    def __init__(self, roomNumber, roomType, pricePerNight, amenities, availability, rate):
        # Constructor initializes all room attributes
        self._roomNumber = roomNumber # Room number identifier
        self._roomType = roomType # Type of room (e.g., Deluxe, Suite)
        self._pricePerNight = pricePerNight # Cost per night for the room
        self._amenities = amenities  # List of amenities
        self._availability = availability # Boolean indicating if the room is available
        self._rate = rate # Customer rating of the room

    def getRoomNumber(self): # Getter for room number
        return self._roomNumber 
    def setRoomNumber(self, roomNumber): # Setter for room number
        self._roomNumber = roomNumber

    def getRoomType(self): # Getter for room type
        return self._roomType
    def setRoomType(self, roomType): # Setter for room type
        self._roomType = roomType

    def getPricePerNight(self): # Getter for price per night
        return self._pricePerNight
    def setPricePerNight(self, pricePerNight): # Setter for price per night
        self._pricePerNight = pricePerNight

    def getAmenities(self): # Getter for room amenities
        return self._amenities
    def setAmenities(self, amenities): # Setter for room amenities
        self._amenities = amenities

    def getAvailability(self): # Getter for room availability status
        return self._availability
    def setAvailability(self, availability): # Getter for room availability status
        self._availability = availability

    def getRate(self): # Getter for room rating
        return self._rate
    def setRate(self, rate): # Setter for room rating
        self._rate = rate

    def checkAvailability(self):
        return self._availability # Returns the current availability status

    def bookRoom(self): # Method to book the room if available
        if self._availability:
            self._availability = False # Mark as unavailable
            return f"Room {self._roomNumber} successfully booked."
        return f"Room {self._roomNumber} is not available."

    def __str__(self):
        # String representation of the Room object
        return (
            f"Room Info:\n"
            f"Room Number: {self._roomNumber}\n" # Show room number
            f"Room Type: {self._roomType}\n" # Show room type
            f"Price/Night: {self._pricePerNight}\n" # Show price per night
            f"Rating: {self._rate}\n" # Show rating
            f"Available: {self._availability}\n" # Show availability status
            f"Amenities: {', '.join(self._amenities)}") # Join list of amenities as comma-separated string

class Booking:
    """Represents a Room Booking made by a Guest."""
    def __init__(self, bookingId, guest, rooms, checkInDate, checkOutDate, numberOfRooms, totalCharges, status):
        self._bookingId = bookingId # Unique ID for the booking
        self._guest = guest # Guest object who made the booking
        self._rooms = rooms  # List of Room objects booked
        self._checkInDate = checkInDate # Check-in date as a string
        self._checkOutDate = checkOutDate # Check-out date as a string
        self._numberOfRooms = numberOfRooms # Total number of rooms booked
        self._totalCharges = totalCharges # Total cost of the booking
        self._status = status # Booking status (e.g., confirmed, pending)

    def getBookingId(self): 
        return self._bookingId # Return booking ID
    def setBookingId(self, bookingId): 
        self._bookingId = bookingId # Set booking ID

    def getGuest(self): 
        return self._guest # Return Guest object
    def setGuest(self, guest): 
        self._guest = guest # Set Guest object

    def getRooms(self): 
        return self._rooms # Return list of booked rooms
    def setRooms(self, rooms): 
        self._rooms = rooms # Set list of booked rooms

    def getCheckInDate(self): 
        return self._checkInDate #return check-in date
    def setCheckInDate(self, checkInDate): 
        self._checkInDate = checkInDate # Set check-in date

    def getCheckOutDate(self): 
        return self._checkOutDate # Return check-out date
    def setCheckOutDate(self, checkOutDate): 
        self._checkOutDate = checkOutDate # Set check-out date

    def getNumberOfRooms(self): 
        return self._numberOfRooms # Return number of rooms booked
    def setNumberOfRooms(self, numberOfRooms): 
        self._numberOfRooms = numberOfRooms # Set number of rooms booked

    def getTotalCharges(self): 
        return self._totalCharges # Return total charges for the booking
    def setTotalCharges(self, totalCharges): 
        self._totalCharges = totalCharges # Set total charges

    def getStatus(self): 
        return self._status # Return booking status
    def setStatus(self, status): 
        self._status = status # Set booking status

    def confirmBooking(self): 
        return f"Booking {self._bookingId} confirmed." # Return confirmation message

    def calculateNumberOfNights(self):
        d1 = datetime.strptime(self._checkInDate, "%Y-%m-%d") # Parse check-in date
        d2 = datetime.strptime(self._checkOutDate, "%Y-%m-%d") # Parse check-out date
        return (d2 - d1).days # Return number of nights between dates

    def calculateCharges(self):
        # Calculate total charge: sum of nightly prices of rooms × number of rooms
        total = sum(room.getPricePerNight() for room in self._rooms) * self._numberOfRooms
        self._totalCharges = total # Update internal total charges
        return total # Update internal total charges

    def receiveNotification(self): 
        return "Booking confirmation notification sent." # Simulate sending a notification

    def __str__(self):
        # Create a string with comma-separated room numbers
        room_numbers = ", ".join(str(room.getRoomNumber()) for room in self._rooms)  # Join all room numbers
        
        # Return nicely formatted string describing the booking
        return (
            f"Booking Id: {self._bookingId}\n" # Show booking ID
            f"Guest: {self._guest.getName()}\n" # Show guest name
            f"Rooms: {room_numbers}\n" # Show all booked room numbers
            f"Number of Rooms: {self._numberOfRooms}\n" # Show how many rooms were booked
            f"Check-in: {self._checkInDate} | Check-out: {self._checkOutDate}\n" # Show dates
            f"Number of Nights: {self.calculateNumberOfNights()}\n" # Show duration of stay
            f"Total: {self._totalCharges}\n" # Show total charges
            f"Status: {self._status}" # Show booking status
        )



class User:
    """
    Base class for any user of the hotel system.
    """
    def __init__(self, userId, name, email, phoneNumber, nationality):
        self._userId = userId # Unique ID for the user
        self._name = name # User's name
        self._email = email # User's email address
        self._phoneNumber = phoneNumber # User's phone number
        self._nationality = nationality # User's nationality

    def getUserId(self):
        return self._userId # Return the user ID
    def setUserId(self, userId):
        self._userId = userId # Set the user ID

    def getName(self):
        return self._name # Return the user's name
    def setName(self, name):
        self._name = name # Set the user's name

    def getEmail(self):
        return self._email # Return the user's email
    def setEmail(self, email):
        self._email = email # Set the user's email
 
    def getPhoneNumber(self):
        return self._phoneNumber # Return the user's phone number
    def setPhoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber # Set the user's phone number

    def getNationality(self):
        return self._nationality # Return the user's nationality
    def setNationality(self, nationality):
        self._nationality = nationality # Set the user's nationality

    def login(self):
        return f"User {self._userId} logged in." # Simulate login message

    def __str__(self):
        # Return a string representation of the User object
        return (
            f"User Info:\n"
            f"ID: {self._userId}\n" #Show user Id
            f"Name: {self._name}\n" #Show User name
            f"Email: {self._email}\n" #Show user's email 
            f"Phone Number: {self._phoneNumber}\n" #Show user's phone number
            f"Nationality: {self._nationality}") #Show user's nationality


class Guest(User):
    """
    Represents a Guest, inherits from User.
    """
    def __init__(self, userId, name, email, phoneNumber, nationality, loyaltyStatus, bookingsList, loyaltyList, feedbackList):
        super().__init__(userId, name, email, phoneNumber, nationality) # Initialize inherited User fields
        self._loyaltyStatus = loyaltyStatus # Boolean indicating if guest is in the loyalty program
        self._bookingsList = bookingsList  # List of Booking objects
        self._loyaltyList = loyaltyList    # List of LoyaltyProgram objects
        self._feedbackList = feedbackList  # List of Feedback objects

    def getLoyaltyStatus(self):
        return self._loyaltyStatus # Return guest's loyalty status
    def setLoyaltyStatus(self, loyaltyStatus):
        self._loyaltyStatus = loyaltyStatus # Set guest's loyalty status

    def getBookingsList(self):
        return self._bookingsList # Return list of bookings
    def setBookingsList(self, bookingsList):
        self._bookingsList = bookingsList # Set list of bookings

    def getloyaltyList(self):
        return self._loyaltyList # Return list of loyalty programs
    def setloyaltyList(self, loyaltyList):
        self._loyaltyList = loyaltyList # Set list of loyalty programs

    def getFeedbackList(self):
        return self._feedbackList # Return list of feedbacks
    def setFeedbackList(self, feedbackList):
        self._feedbackList = feedbackList # Set list of feedbacks

    def makeBookings(self, booking):
        self._bookingsList.append(booking) # Add a booking to the list
        return f"Booking {booking} added." # Return confirmation message

    def viewRewards(self):
        return f"Rewards available: {len(self._loyaltyList)} entries." # Return reward info

    def searchRoomAvailability(self):
        return True # Simulate room availability (for demo purposes)

    def addService(self):
        return ["Wifi", "Room Service","Gym Access", "Laundry"]  # Return list of extra services
 
    def createAccount(self):
        return f"Guest account created for {self._name}" # Simulate account creation

    def updateProfile(self):
        return f"Profile updated for {self._name}" # Simulate profile update

    def viewReservation(self):
        return f"You have {len(self._bookingsList)} reservations." # Show number of bookings
    
    def __str__(self):
    # Return string with full guest details including inherited user details and additional guest-specific info
        return (
        super().__str__() + "\n" + # Call the base class (User) __str__ to include user info
            f"Loyalty Status: {self._loyaltyStatus}\n" # Show if the guest is part of the loyalty program (True/False)
            f"Bookings: {len(self._bookingsList)}\n" # Show how many bookings the guest has made
            f"Loyalty Programs: {len(self._loyaltyList)}\n" # Show how many loyalty program entries the guest is in
            f"Feedbacks: {len(self._feedbackList)}") # Show how many feedback submissions the guest has made

class Admin(User):
    """
    Represents an Admin, inherits from User.
    """
    def __init__(self, userId, name, email, phoneNumber, nationality, role, permissions):
        super().__init__(userId, name, email, phoneNumber, nationality) # Initialize User base class
        self._role = role # Admin's job title/role
        self._permissions = permissions # List of admin permissions

    def getRole(self):
        return self._role # Return role
    def setRole(self, role):
        self._role = role # Set role

    def getPermission(self):
        return self._permissions # Return permissions list
    def setPermission(self, permissions):
        self._permissions = permissions # Set permissions list

    def manageRooms(self):
        return "Admin is managing rooms." # Simulate room management action

    def __str__(self):
        # Return admin's details including inherited user info
        return (
            super().__str__() + "\n" + # Call the base User class __str__ method to include basic user information
            f"Admin Info: {self._name}\n" # Show the admin's name specifically labeled as Admin Info
            f"Role: {self._role}\n" # Show the admin's role (e.g., Manager, Supervisor)
            f"Permissions: {self._permissions}") # Show the list of permissions assigned to the admin

class Payment:
    """Represents a payment made for a booking."""
    def __init__(self, paymentId, amount, paymentMethod, billingAddress, paymentDate, paymentStatus):
        self._paymentId = paymentId # Unique payment ID
        self._amount = amount # Original amount before discounts
        self._paymentMethod = paymentMethod # Payment method (e.g., card, PayPal)
        self._billingAddress = billingAddress # Billing address
        self._paymentDate = paymentDate # Date of payment
        self._paymentStatus = paymentStatus # Status (e.g., completed, pending)
        self._discount = self._amount * 0.05 # Calculate 5% discount
        self._additionalCharges = 25.0 # Add fixed additional charge
        self._finalAmount = self._amount - self._discount + self._additionalCharges # Final total
        
    def getPaymentId(self):
        return self._paymentId # Return payment ID
    def setPaymentId(self, paymentId):
        self._paymentId = paymentId # Set payment ID

    def getAmount(self):
        return self._amount # Return original amount
    def setAmount(self, amount):
        self._amount = amount # Set original amount

    def getPaymentMethod(self):
        return self._paymentMethod # Return payment method
    def setPaymentMethod(self, paymentMethod):
        self._paymentMethod = paymentMethod # Set payment method

    def getBillingAddress(self):
        return self._billingAddress # Return billing address
    def setBillingAddress(self, billingAddress):
        self._billingAddress = billingAddress # Set billing address

    def getPaymentDate(self):
        return self._paymentDate # Return payment date
    def setPaymentDate(self, paymentDate):
        self._paymentDate = paymentDate # Set payment date

    def getPaymentStatus(self):
        return self._paymentStatus # Return payment status
    def setPaymentStatus(self, paymentStatus):
        self._paymentStatus = paymentStatus # Set payment status

    def processPayment(self):
        discount = self._amount * 0.05 # Calculate discount
        final_amount = self._amount - discount # Deduct discount
        additional_charges = 25.0 # Add fixed extra fee
        total_with_additional = self._amount + additional_charges # Add fee to base
        after_discount_total = final_amount + additional_charges # Final amount after all changes

        # Return full summary of processed payment
        return (
            f"Total amount: {self._amount}\n" # Shows the original amount before any discount or additional charges
            f"Total amount with additional charges: {total_with_additional}\n" # Shows the amount plus any fixed additional charges (e.g., service fee)
            f"After discount Total: {after_discount_total}\n" # Shows the final total after applying the discount and adding additional charges
            f"Payment {self._paymentId} of amount {after_discount_total} (after 5% discount) processed using {self._paymentMethod}."
            # Shows a summary of the payment with ID, amount paid after discount, and the method used (e.g., credit card)
        )

    def __str__(self):
        # Return string summary of the payment
        return ( 
            f"Payment Details:\n" # Header for the payment summary
            f"Payment ID: {self._paymentId}\n" # Shows the unique payment identifier
            f"Original Amount: {self._amount}\n" # Displays the initial amount before any deductions or charges
            f"Discount (5%): {self._discount}\n" # Shows the calculated discount (5% of original amount)
            f"Additional Charges: {self._additionalCharges}\n" # Displays any extra fixed charges (e.g., service fee)
            f"Final Amount Paid: {self._finalAmount}\n" # Shows the actual amount paid after applying discount and adding charges
            f"Method: {self._paymentMethod}\n" # Indicates the payment method used (e.g., Credit Card, Apple Pay)
            f"Billing Address: {self._billingAddress}\n" # Indicates the payment method used (e.g., Credit Card, Apple Pay)
            f"Date: {self._paymentDate}\n" # Displays the date the payment was made
            f"Status: {self._paymentStatus}" # Shows the status of the payment (e.g., Completed, Pending)
        )


class Invoice:
    """Represents an invoice generated for a booking."""
    def __init__(self, invoiceId, booking, totalAmount, rate, additionalCharges):
        self._invoiceId = invoiceId # Store the unique ID for this invoice
        self._booking = booking # Associate this invoice with a specific booking object
        self._totalAmount = totalAmount # Store the total amount before any discounts or additional charges
        self._rate = rate # Store the rate (e.g., tax or service charge percentage)
        self._additionalCharges = additionalCharges # Store any additional fixed charges (e.g., service fee)

    def getInvoiceId(self): 
        return self._invoiceId # Return invoice ID
    def setInvoiceId(self, invoiceId): 
        self._invoiceId = invoiceId # Set invoice ID

    def getBooking(self): 
        return self._booking # Return associated booking object
    def setBooking(self, booking): 
        self._booking = booking # Set booking object

    def getTotalAmount(self): 
        return self._totalAmount # Return total amount
    def setTotalAmount(self, totalAmount): 
        self._totalAmount = totalAmount # Set total amount

    def getRate(self): 
        return self._rate # Return rate
    def setRate(self, rate): 
        self._rate = rate # Set rate

    def getAdditionalCharges(self): 
        return self._additionalCharges # Return additional charges
    def setAdditionalCharges(self, additionalCharges): 
        self._additionalCharges = additionalCharges # Set additional charges

    def generateInvoice(self): # Generate invoice summary with applied discount and extra charges
        discount = self._booking.getTotalCharges() * 0.05 # Calculate 5% discount
        after_discount_total = self._booking.getTotalCharges() - discount + self._additionalCharges # Final total after discount and charges
        # Return formatted invoice string with calculated totals
        return (
            f"Invoice #{self._invoiceId} generated for booking #{self._booking.getBookingId()}.\n" # Show invoice and booking ID
            f"Before Discount Total: {self._booking.getTotalCharges()}\n" # Show original total before any discount
            f"Additional Charges: {self._additionalCharges}\n" # Show added charges like service fees
            f"Final Total: {after_discount_total}" # Show final amount after applying discount and adding additional charges
        )


    def __str__(self):
         # String representation of invoice details
        discount = self._booking.getTotalCharges() * 0.05 # Calculate 5% discount
        final_total = self._booking.getTotalCharges() - discount + self._additionalCharges # Compute final amount
        
        return (
          f"Invoice:\n" # Header for the invoice section
          f"Invoice ID: {self._invoiceId}\n" # Displays the unique ID of the invoice
          f"Booking ID: {self._booking.getBookingId()}\n" # Displays the ID of the booking associated with this invoice
          f"Before Discount Total: {self._booking.getTotalCharges()}\n" # Shows the total cost before any discounts
          f"Discount (5%): {discount}\n" # Shows the discount amount calculated as 5% of the total
          f"Additional Charges: {self._additionalCharges}\n" # Displays any extra fees added (e.g., service fees)
          f"Final Total: {final_total}\n" # Shows the final amount after applying discount and adding additional charges
          f"Rate: {self._rate}%\n" # Shows the applicable tax or service rate percentage
    )



class Feedback:
    """Represents guest feedback on the stay."""
    def __init__(self, feedbackId, rating, comments, feedbackDateTime):
        self._feedbackId = feedbackId # Unique identifier for the feedback
        self._rating = rating # Numeric rating given by the guest (e.g., out of 5)
        self._comments = comments # Textual comments provided by the guest
        self._feedbackDateTime = feedbackDateTime # Date and time when the feedback was submitted

    def getFeedbackId(self):
        return self._feedbackId # Return feedback ID
    def setFeedbackId(self, feedbackId):
        self._feedbackId = feedbackId # Set feedback ID

    def getRating(self):
        return self._rating # Return rating
    def setRating(self, rating):
        self._rating = rating # Set rating

    def getComments(self):
        return self._comments # Return comments
    def setComments(self, comments):
        self._comments = comments # Set comments

    def getFeedbackDateTime(self):
        return self._feedbackDateTime # Return date and time of feedback
    def setFeedbackDateTime(self, feedbackDateTime):
        self._feedbackDateTime = feedbackDateTime  # Set feedback timestamp

    def submitFeedBack(self):
        return f"Feedback {self._feedbackId} submitted successfully." # Simulated submission response
    
    def __str__(self):
        # Return string representation of feedback details
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
