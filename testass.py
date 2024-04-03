def add_distance(distances, from_location, to_location, distance):
    if from_location not in distances:
        distances[from_location] = {}
    distances[from_location][to_location] = distance

def get_distance(distances, from_location, to_location):
    if from_location in distances and to_location in distances[from_location]:
        return distances[from_location][to_location]
    else:
        return None

def show_distances(distances, from_location):
    print(f"Distances from {from_location}:")
    if from_location in distances:
        for to_location, distance in distances[from_location].items():
            print(f"{to_location}: {distance} meters")
    else:
        print("No distances available for the given location.")

def select_location(locations, prompt):
    print("Available locations:")
    for i, location in enumerate(locations, start=1):
        print(f"{i}. {location}")
    while True:
        choice = input(prompt)
        if choice.isdigit() and 1 <= int(choice) <= len(locations):
            return locations[int(choice) - 1]
        else:
            print("Invalid choice. Please enter a number between 1 and", len(locations))

def main():
    print("You are now in front of the university. \nWhere do you want to go in university?")
    distances = {}

    # Add distances between locations
    add_distance(distances, "Main Entrance", "Grand Palace", 175)
    add_distance(distances, "Grand Palace", "Villa Vichalai Hotel", 300)
    add_distance(distances, "Villa Vichalai Hotel", "Faculty of Management", 54)
    add_distance(distances, "Faculty of Management", "Roundabout", 1500)
    add_distance(distances, "Faculty of Management", "Male Dormitory", 2200)
    add_distance(distances, "Male Dormitory", "Female Dormitory1", 130)
    add_distance(distances, "Male Dormitory", "Female Dormitory2", 180)
    add_distance(distances, "Female Dormitory1", "Female Dormitory2", 110)
    add_distance(distances, "Male Dormitory", "Sport Complex Building", 40)
    add_distance(distances, "Female Dormitory1", "Sport Complex Building", 100)
    add_distance(distances, "Roundabout", "Sport Complex Building", 750)
    add_distance(distances, "Roundabout", "Faculty of Agricultural Industry", 600)
    add_distance(distances, "Faculty of Agricultural Industry", "Administration Building", 160)
    add_distance(distances, "Roundabout", "Faculty of Industrial Technology and Management", 900)
    add_distance(distances, "Faculty of Industrial Technology and Management", "Faculty of Engineering", 900)
    add_distance(distances, "Faculty of Industrial Technology and Management", "Sport Complex Building", 2000)

    # List of available locations
    locations = list(distances.keys())

    print("Welcome to the Travel Planner!")

    # Select starting location
    start_location = select_location(locations, "Choose your starting location (1-{}): ".format(len(locations)))

    # Select destination location
    end_location = select_location(locations, "Choose your destination (1-{}): ".format(len(locations)))

    # Calculate and display the distance between the selected locations
    distance = get_distance(distances, start_location, end_location)
    if distance is not None:
        print("The distance from", start_location, "to", end_location, "is", distance, "meters.")
    else:
        print("Sorry, the distance between the selected locations is not available.")

if __name__ == "__main__":
    main()
