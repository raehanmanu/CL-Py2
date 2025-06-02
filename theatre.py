class Showtime:
    def __init__(self, title, time):
        self.title = title
        self.time = time
        self.seat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    def assign(self):
        rows = len(self.seat)
        cols = len(self.seat[0])
        for i in range(rows):
            for j in range(cols):
                if self.seat[i][j] == 0:
                    self.seat[i][j] = 1
                    self.my_seat = f"Seat is row {i+1} and column {j+1}"
                    print("seat assigned")
                    return True        
        print("No seats available")
    def ticket(self):
        print("Here is the details of your screening:")
        print(self.title, " ", self.time)
        print("Your seating will be at row by column: ", self.my_seat)
        

john = Showtime("John Wick", "5:30")
int = Showtime("Intersteller", "10:00")
tangled = Showtime("Tangled", "12:00")

while(True):
    print("Hello. This is the movie selection system. Here is a list of films out right now and their showtimes: ")
    print(john.title, " ", john.time)
    print(int.title, " ", int.time)
    print(tangled.title, " ", tangled.time)
    choice = input("Which film would you like to see? ")
    if choice == "John Wick":
        john.assign()
        john.ticket()
    if choice == "Intersteller":
        int.assign()
        int.ticket()
    if choice == "Tangled":
        tangled.assign()
        tangled.ticket()
    


