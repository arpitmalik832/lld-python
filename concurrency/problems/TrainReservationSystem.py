import random
import threading


class TrainReservationSystem:
    def __init__(self, initial_seats: dict[str, int]):
        self.available_seats = initial_seats
        self.lock = threading.RLock()  # Reentrant Lock

    # TODO: Implement the reserve_seats method to reserve the seats of the desired seat_type
    def reserve_seats(self, seat_type, num_seats):
        with self.lock:
            if num_seats <= self.available_seats[seat_type]:
                self.available_seats[seat_type] -= num_seats
                return True
            else:
                return False

    # TODO: Implement the function below to get the total number of unreserved seats of the given seat_type
    def get_available_seats(self, seat_type):
        return self.available_seats[seat_type]


def concurrent_booking(reservation_system, num_threads, seats_per_thread):
    threads = []

    # Create and start multiple threads for concurrent booking
    for _ in range(num_threads):
        seat_type = random.choice(list(reservation_system.available_seats.keys()))
        thread = threading.Thread(
            target=book_seats, args=(reservation_system, seat_type, seats_per_thread)
        )
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


# Function for each thread to attempt booking seats
def book_seats(reservation_system, seat_type, num_seats):
    success = reservation_system.reserve_seats(seat_type, num_seats)
    if success:
        print(f"Successfully booked {num_seats} {seat_type} seats")
    else:
        print(f"Failed to book {num_seats} {seat_type} seats")


def main():
    initial_seats = {"1AC": 50, "2AC": 100, "3AC": 150, "Sleeper": 200}
    reservation_system = TrainReservationSystem(initial_seats)

    num_threads = 10  # Number of concurrent threads
    seats_per_thread = 5  # Number of seats each thread attempts to book
    concurrent_booking(reservation_system, num_threads, seats_per_thread)

    # Check available seats after concurrent bookings
    print("Available 1AC seats:", reservation_system.get_available_seats("1AC"))
    print("Available 2AC seats:", reservation_system.get_available_seats("2AC"))
    print("Available 3AC seats:", reservation_system.get_available_seats("3AC"))
    print("Available Sleeper seats:", reservation_system.get_available_seats("Sleeper"))


main()
