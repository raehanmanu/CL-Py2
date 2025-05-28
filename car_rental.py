import datetime

class CarRentalSystem:
    def __init__(self):
        self.cars = {
            1: {"name": "Toyota Corolla", "rate_per_hour": 10, "available": True},
            2: {"name": "Honda Civic", "rate_per_hour": 12, "available": True},
            3: {"name": "Ford Focus", "rate_per_hour": 8, "available": True},
        }
        self.rental_history = []

    def list_available_cars(self):
        print("\nAvailable Cars:")
        for car_id, details in self.cars.items():
            if details["available"]:
                print(f"{car_id}: {details['name']} - ${details['rate_per_hour']}/hour")

    def book_car(self):
        self.list_available_cars()
        car_id = int(input("Enter the ID of the car you want to book: "))
        if car_id in self.cars and self.cars[car_id]["available"]:
            customer_name = input("Enter your name: ")
            start_time = datetime.datetime.now()
            self.cars[car_id]["available"] = False
            self.rental_history.append({
                "customer_name": customer_name,
                "car_id": car_id,
                "car_name": self.cars[car_id]["name"],
                "start_time": start_time,
                "end_time": None,
                "charges": None,
            })
            print(f"\n{self.cars[car_id]['name']} has been booked successfully!")
        else:
            print("\nInvalid car ID or car is not available.")

    def return_car(self):
        customer_name = input("Enter your name: ")
        for record in self.rental_history:
            if record["customer_name"] == customer_name and record["end_time"] is None:
                car_id = record["car_id"]
                end_time = datetime.datetime.now()
                rental_duration = (end_time - record["start_time"]).total_seconds() / 3600
                charges = round(rental_duration * self.cars[car_id]["rate_per_hour"], 2)

                record["end_time"] = end_time
                record["charges"] = charges
                self.cars[car_id]["available"] = True

                print(f"\nThank you for returning the {record['car_name']}.")
                print(f"Total charges: ${charges}")
                return
        print("\nNo active rental found for the given name.")

    def display_rental_history(self):
        print("\nRental History:")
        for record in self.rental_history:
            print(
                f"Customer: {record['customer_name']}, Car: {record['car_name']}, "
                f"Start: {record['start_time']}, End: {record['end_time']}, Charges: {record['charges']}"
            )

    def save_data(self, filename):
        with open(filename, "w") as file:
            for record in self.rental_history:
                file.write(
                    f"{record['customer_name']},{record['car_name']},{record['start_time']},"
                    f"{record['end_time']},{record['charges']}\n"
                )

    def load_data(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    customer_name, car_name, start_time, end_time, charges = line.strip().split(",")
                    self.rental_history.append({
                        "customer_name": customer_name,
                        "car_name": car_name,
                        "start_time": datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S"),
                        "end_time": datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S") if end_time != "None" else None,
                        "charges": float(charges) if charges != "None" else None,
                    })
        except FileNotFoundError:
            print("No rental history file found, starting fresh.")


def main():
    system = CarRentalSystem()
    system.load_data("rental_history.txt")

    while True:
        print("\nCar Rental System")
        print("1. List available cars")
        print("2. Book a car")
        print("3. Return a car")
        print("4. Display rental history")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.list_available_cars()
        elif choice == "2":
            system.book_car()
        elif choice == "3":
            system.return_car()
        elif choice == "4":
            system.display_rental_history()
        elif choice == "5":
            system.save_data("rental_history.txt")
            print("\nData saved. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()