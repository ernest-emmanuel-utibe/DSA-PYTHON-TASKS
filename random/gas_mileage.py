if __name__ == "__main__":
    several_trips = 0
    average = 0

    miles_driven_per_trip = input("Enter miles driven: ")
    gallon_used_per_trip = input("Enter gallon used: ")

    if several_trips != miles_driven_per_trip and several_trips != gallon_used_per_trip:
        average = miles_driven_per_trip / gallon_used_per_trip

    print(f'Miles driven per gallon is: %.2f%n', miles_driven_per_trip)
    print(f'Gallons used per trip is: %.2f%n', average)
