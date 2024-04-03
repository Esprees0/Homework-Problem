def calculate_travel_time(origin, destination):
    flight_durations = {
        ("Thailand", "France"): 12.05,
        ("Thailand", "England"): 12.20,
        ("Thailand", "Italy"): 13.30,
        ("Thailand", "Switzerland"): 11.45,
        ("Thailand", "Germany"): 11.30,
        ("France", "England"): 1.10,
        ("France", "Italy"): 2.10,
        ("France", "Switzerland"): 1.15,
        ("France", "Germany"): 1.15,
        ("England", "France"): 1.10,
        ("England", "Italy"): 2.20,
        ("England", "Switzerland"): 1.25,
        ("England", "Germany"): 1.20,
        ("Italy", "France"): 2.10,
        ("Italy", "England"): 2.35,
        ("Italy", "Switzerland"): 1.30,
        ("Italy", "Germany"): 2.00,
        ("Switzerland", "France"): 1.15,
        ("Switzerland", "England"): 1.45,
        ("Switzerland", "Italy"): 1.30,
        ("Switzerland", "Germany"): 1.00,
        ("Germany", "France"): 1.15,
        ("Germany", "England"): 1.20,
        ("Germany", "Italy"): 2.00,
        ("Germany", "Switzerland"): 1.00
    }

    place_durations = {
        "France": {
            "Eiffel Tower": 1.2,
            "Palace of Versailles": 1.8,
            "Louvre Museum": 1.5,
            "Notre Dame Cathedral": 1.03,
            "Arc de Triomphe": 0.58
        },
        "England": {
            "Big Ben": 0.9,
            "Tower Bridge": 1.18,
            "Westminster Abbey": 0.82,
            "Buckingham Palace": 0.73,
            "Stonehenge": 1.33
        },
        "Italy": {
            "Venice": 6.0,
            "Milan Cathedral": 6.3,
            "Vatican City": 0.75,
            "Trevi Fountain": 0.8,
            "Galleria Vittorio Emanuele II": 4.27
        },
        "Switzerland": {
            "Jungfrau": 2.05,
            "Lausanne Cathedral": 2.47,
            "The Flower Clock": 3.07,
            "Lauterbrunnen": 2.0,
            "Lucerne": 0.97
        },
        "Germany": {
            "Brandenburg Gate": 5.67,
            "Kehlsteinhaus/Eagle’s Nest": 5.6,
            "Luneburg": 4.92,
            "Marienplatz": 3.51,
            "Beilstein": 1.32
        }
    }

    if (origin, destination) in flight_durations:
        return flight_durations[(origin, destination)]
    elif (destination, origin) in flight_durations:
        return flight_durations[(destination, origin)]
    elif origin in place_durations and destination in place_durations[origin]:
        return place_durations[origin][destination]
    elif destination in place_durations and origin in place_durations[destination]:
        return place_durations[destination][origin]
    else:
        return "Unknown duration"

def get_airport(country):
    airports = {
        "Thailand": "Suvarnabhumi Airport",
        "France": "Charles de Gaulle Airport",
        "England": "London Heathrow Airport",
        "Italy": "Leonardo Da Vinci International Airport",
        "Switzerland": "Zurich Airport",
        "Germany": "Frankfurt International Airport"
    }

    return airports.get(country, "Unknown Airport")

def main():
    print("Welcome to the Suvarnabhumi Airport Travel Planner!")
    print("Your starting country is Thailand.")

    destinations = ["France", "England", "Italy", "Switzerland", "Germany"]
    current_country = "Thailand"

    while True:
        print(f"\nYou are currently in {current_country}. Choose your next destination:")
        for i, country in enumerate(destinations, start=1):
            if country != current_country:
                print(f"{i}. {country}")

        next_destination_choice = input("Enter the number corresponding to your next destination country (1-5), or 'exit' to end the journey: ")
        if next_destination_choice.lower() == "exit":
            print("Thank you for using the Suvarnabhumi Airport Travel Planner. Have a great day!")
            break

        try:
            next_destination_country = destinations[int(next_destination_choice) - 1]
            travel_time = calculate_travel_time(current_country, next_destination_country)

            if travel_time != "Unknown duration":
                print(f"\nThe estimated travel time from {current_country} to {next_destination_country} is approximately {travel_time} hours.")
                print(f"You'll depart from {get_airport(current_country)} and arrive at {get_airport(next_destination_country)}.")
                current_country = next_destination_country
            else:
                print("Sorry, the travel time to the selected destination is unknown.")

            within_country_choice = input("Would you like to travel within the current country? (yes/no): ")

            while within_country_choice.lower() not in ['yes', 'no']:
                print("Invalid choice. Please enter 'yes' or 'no'.")
                within_country_choice = input("Would you like to travel within the current country? (yes/no): ")

            if within_country_choice.lower() == "yes":
                places = {
                    "France": {
                        "Eiffel Tower": 1.2,
                        "Palace of Versailles": 1.8,
                        "Louvre Museum": 1.5,
                        "Notre Dame Cathedral": 1.03,
                        "Arc de Triomphe": 0.58
                    },
                    "England": {
                        "Big Ben": 0.9,
                        "Tower Bridge": 1.18,
                        "Westminster Abbey": 0.82,
                        "Buckingham Palace": 0.73,
                        "Stonehenge": 1.33
                    },
                    "Italy": {
                        "Venice": 6.0,
                        "Milan Cathedral": 6.3,
                        "Vatican City": 0.75,
                        "Trevi Fountain": 0.8,
                        "Galleria Vittorio Emanuele II": 4.27
                    },
                    "Switzerland": {
                        "Jungfrau": 2.05,
                        "Lausanne Cathedral": 2.47,
                        "The Flower Clock": 3.07,
                        "Lauterbrunnen": 2.0,
                        "Lucerne": 0.97
                    },
                    "Germany": {
                        "Brandenburg Gate": 5.67,
                        "Kehlsteinhaus/Eagle’s Nest": 5.6,
                        "Luneburg": 4.92,
                        "Marienplatz": 3.51,
                        "Beilstein": 1.32
                    }
                }

                while True:
                    print(f"\nAvailable places to visit in {current_country}:")
                    for i, place in enumerate(places[current_country], start=1):
                        print(f"{i}. {place}")

                    place_choice = input("Enter the number corresponding to the place you want to visit, or 'exit' to go back: ")

                    if place_choice.lower() == "exit":
                        break
                    elif place_choice.isdigit() and 1 <= int(place_choice) <= len(places[current_country]):
                        selected_place = list(places[current_country].keys())[int(place_choice) - 1]
                        travel_time = places[current_country][selected_place]
                        print(f"\nThe estimated travel time from {get_airport(current_country)} to {selected_place} is approximately {travel_time} hours.")
                    else:
                        print("Invalid choice. Please enter a valid number.")

        except (IndexError, ValueError):
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()