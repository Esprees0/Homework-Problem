def create_distance_dict(*args):
    distances = {}
    for arg in args:
        for key, value in arg.items():
            if key[0] not in distances:
                distances[key[0]] = {}
            distances[key[0]][key[1]] = value
    return distances


def display_destinations(location, distances):
    print(f"\nAvailable destinations from {location}:")
    destinations = distances[location]
    for i, (destination, distance) in enumerate(destinations.items(), start=1):
        print(f"{i}. {destination} (Distance: {distance} meters)")


def main():
    Guardhouse = {
    ("Guardhouse", "Grand Palace"):175,
	("Guardhouse", "Villa Vichalai Hotel"):480,
	("Guardhouse", "Faculty of Business Administration and Service Industry"):550,
	("Guardhouse", "Roundabout"):2000,
	("Guardhouse", "Faculty of Agro-industry"):2650,
	("Guardhouse", "Male Dormitory"):2700,
	("Guardhouse", "FeMale Dormitory1"):2800,
	("Guardhouse", "FeMale Dormitory2"):2850,
	("Guardhouse", "Sport Complex Building2"):2800,
	("Guardhouse", "Faculty of Industrial Technology and Management"):2550,
	("Guardhouse", "Faculty of Engineering"):3300,
	("Guardhouse", "Administration Building"):2800,
	("Guardhouse", "Central Library Office"):2600	
    }
                            
    GrandPalace = {
        ("Grand Palace", "Guardhouse"):175,
        ("Grand Palace", "Villa Vichalai Hotel"):300,
        ("Grand Palace", "Faculty of Business Administration and Service Industry"):350,
        ("Grand Palace", "Roundabout"):1900,
        ("Grand Palace", "Faculty of Agro-industry"):2500,
        ("Grand Palace", "Male Dormitory"):2500,
        ("Grand Palace", "FeMale Dormitory1"):2600,
        ("Grand Palace", "FeMale Dormitory2"):2700,
        ("Grand Palace", "Sport Complex Building2"):2700,
        ("Grand Palace", "Faculty of Industrial Technology and Management"):2400,
        ("Grand Palace", "Faculty of Engineering"):3100,
        ("Grand Palace", "Administration Building"):2300,
        }
                            
    Library = {
        ("Central Library Office", "Guardhouse"):2600,
        ("Central Library Office", "Villa Vichalai Hotel"):2400,
        ("Central Library Office", "Faculty of Business Administration and Service Industry"):2100,
        ("Central Library Office", "Roundabout"):550,
        ("Central Library Office", "Faculty of Agro-industry"):500,
        ("Central Library Office", "Male Dormitory"):1800,
        ("Central Library Office", "FeMale Dormitory1"):1900,
        ("Central Library Office", "FeMale Dormitory2"):2000,
        ("Central Library Office", "Sport Complex Building2"):2000,
        ("Central Library Office", "Faculty of Industrial Technology and Management"):500,
        ("Central Library Office", "Faculty of Engineering"):1200,
        ("Central Library Office", "Administration Building"):350,
        }
                            
    Hotel = {
        ("Villa Vichalai Hotel","Guardhouse"): 500,		
        ("Villa Vichalai Hotel", "Grand Palace"):300,
        ("Villa Vichalai Hotel", "Faculty of Business Administration and Service Industry"):54,
        ("Villa Vichalai Hotel", "Roundabout"):2000,
        ("Villa Vichalai Hotel", "Faculty of Agro-industry"):2200,
        ("Villa Vichalai Hotel", "Male Dormitory"):2200,
        ("Villa Vichalai Hotel", "FeMale Dormitory1"):2300,
        ("Villa Vichalai Hotel", "FeMale Dormitory2"):2400,
        ("Villa Vichalai Hotel", "Sport Complex Building2"):2400,
        ("Villa Vichalai Hotel", "Faculty of Industrial Technology and Management"):2100,
        ("Villa Vichalai Hotel", "Faculty of Engineering"):2800,
        ("Villa Vichalai Hotel", "Central Library Office"):2100,
        ("Villa Vichalai Hotel", "Administration Building"):2000	
        }

    BAS = {
        ("Faculty of Business Administration and Service Industry", "Guardhouse"):550,
        ("Faculty of Business Administration and Service Industry", "Grand Palace"):350,
        ("Faculty of Business Administration and Service Industry", "Villa Vichalai Hotel"):54,
        ("Faculty of Business Administration and Service Industry", "Roundabout"):1900,
        ("Faculty of Business Administration and Service Industry", "Faculty of Agro-industry"):2200,
        ("Faculty of Business Administration and Service Industry", "Male Dormitory"):2200,
        ("Faculty of Business Administration and Service Industry", "FeMale Dormitory1"):2400,
        ("Faculty of Business Administration and Service Industry", "FeMale Dormitory2"):2400,
        ("Faculty of Business Administration and Service Industry", "Sport Complex Building2"):2400,
        ("Faculty of Business Administration and Service Industry", "Faculty of Industrial Technology and Management"):2100,
        ("Faculty of Business Administration and Service Industry", "Faculty of Engineering"):2900,
        ("Faculty of Business Administration and Service Industry", "Administration Building"):2000,
        ("Faculty of Business Administration and Service Industry", "Central Library Office"):2200	
        }
                            
    Round_about = {
        ("Roundabout", "Guardhouse"):2000,
        ("Roundabout", "Grand Palace"):1900,
        ("Roundabout", "Villa Vichalai Hotel"):2000,
        ("Roundabout", "Faculty of Business Administration and Service Industry"):1900,
        ("Roundabout", "Faculty of Agro-industry"):600,
        ("Roundabout", "Male Dormitory"):1500,
        ("Roundabout", "FeMale Dormitory1"):1600,
        ("Roundabout", "FeMale Dormitory2"):1700,
        ("Roundabout", "Sport Complex Building2"):1600,
        ("Roundabout", "Faculty of Industrial Technology and Management"):600,
        ("Roundabout", "Faculty of Engineering"):1200,
        ("Roundabout", "Administration Building"):400,
        ("Roundabout", "Central Library Office"):550	
        }

    AI = {
        ("Faculty of Agro-industry", "Guardhouse"):2800,
        ("Faculty of Agro-industry", "Grand Palace"):2600,
        ("Faculty of Agro-industry", "Villa Vichalai Hotel"):2300,
        ("Faculty of Agro-industry", "Faculty of Business Administration and Service Industry"):2300,
        ("Faculty of Agro-industry", "Roundabout"):600,
        ("Faculty of Agro-industry", "Male Dormitory"):2000,
        ("Faculty of Agro-industry", "FeMale Dormitory1"):2100,
        ("Faculty of Agro-industry", "FeMale Dormitory2"):2200,
        ("Faculty of Agro-industry", "Sport Complex Building2"):2200,
        ("Faculty of Agro-industry", "Faculty of Industrial Technology and Management"):1000,
        ("Faculty of Agro-industry", "Faculty of Engineering"):1700,
        ("Faculty of Agro-industry", "Administration Building"):140,
        ("Faculty of Agro-industry", "Central Library Office"):500	
        }
                            
                            
    Male_dor = {
        ("Male Dormitory", "Guardhouse"):2700,
        ("Male Dormitory", "Grand Palace"):2500,
        ("Male Dormitory", "Villa Vichalai Hotel"):2200,
        ("Male Dormitory", "Faculty of Business Administration and Service Industry"):2200,
        ("Male Dormitory", "Roundabout"):1500,
        ("Male Dormitory", "Faculty of Agro-industry"):1900,
        ("Male Dormitory", "FeMale Dormitory1"):130,
        ("Male Dormitory", "FeMale Dormitory2"):190,
        ("Male Dormitory", "Sport Complex Building2"):220,
        ("Male Dormitory", "Faculty of Industrial Technology and Management"):1800,
        ("Male Dormitory", "Faculty of Engineering"):2500,
        ("Male Dormitory", "Administration Building"):1700,
        ("Male Dormitory", "Central Library Office"):1800	
        }

    Female_dor1 = {
        ("FeMale Dormitory1", "Guardhouse"):2800,
        ("FeMale Dormitory1", "Grand Palace"):2600,
        ("FeMale Dormitory1", "Villa Vichalai Hotel"):2400,
        ("FeMale Dormitory1", "Faculty of Business Administration and Service Industry"):2300,
        ("FeMale Dormitory1", "Roundabout"):1600,
        ("FeMale Dormitory1", "Faculty of Agro-industry"):2000,
        ("FeMale Dormitory1", "Male Dormitory"):130,
        ("FeMale Dormitory1", "FeMale Dormitory2"):75,
        ("FeMale Dormitory1", "Sport Complex Building2"):200,
        ("FeMale Dormitory1", "Faculty of Industrial Technology and Management"):1900,
        ("FeMale Dormitory1", "Faculty of Engineering"):2600,
        ("FeMale Dormitory1", "Administration Building"):1800,
        ("FeMale Dormitory2", "Central Library Office"):1900	
        }					
                            
    Female_dor2 = {
        ("FeMale Dormitory2", "Guardhouse"):2900,
        ("FeMale Dormitory2", "Grand Palace"):2700,
        ("FeMale Dormitory2", "Villa Vichalai Hotel"):2400,
        ("FeMale Dormitory2", "Faculty of Business Administration and Service Industry"):2400,
        ("FeMale Dormitory2", "Roundabout"):1700,
        ("FeMale Dormitory2", "Faculty of Agro-industry"):2000,
        ("FeMale Dormitory2", "Male Dormitory"):190,
        ("FeMale Dormitory2", "FeMale Dormitory1"):75,
        ("FeMale Dormitory2", "Sport Complex Building2"):270,
        ("FeMale Dormitory2", "Faculty of Industrial Technology and Management"):2000,
        ("FeMale Dormitory2", "Faculty of Engineering"):2700,
        ("FeMale Dormitory2", "Administration Building"):1900,
        ("FeMale Dormitory2", "Central Library Office"):2000	
        }				

    Sport_build = {
        ("Sport Complex Building2", "Guardhouse"):2900,
        ("Sport Complex Building2", "Grand Palace"):2700,
        ("Sport Complex Building2", "Villa Vichalai Hotel"):2400,
        ("Sport Complex Building2", "Faculty of Business Administration and Service Industry"):2400,
        ("Sport Complex Building2", "Roundabout"):1600,
        ("Sport Complex Building2", "Faculty of Agro-industry"):2100,
        ("Sport Complex Building2", "Male Dormitory"):220,
        ("Sport Complex Building2", "FeMale Dormitory1"):200,
        ("Sport Complex Building2", "FeMale Dormitory2"):270,
        ("Sport Complex Building2", "Faculty of Industrial Technology and Management"):2000,
        ("Sport Complex Building2", "Faculty of Engineering"):2700,
        ("Sport Complex Building2", "Administration Building"):1900,
        ("Sport Complex Building2", "Central Library Office"):2000	
        }
                            
    FITM = {
        ("Faculty of Industrial Technology and Management", "Guardhouse"):2600,
        ("Faculty of Industrial Technology and Management", "Grand Palace"):2400,
        ("Faculty of Industrial Technology and Management", "Villa Vichalai Hotel"):2100,
        ("Faculty of Industrial Technology and Management", "Faculty of Business Administration and Service Industry"):2100,
        ("Faculty of Industrial Technology and Management", "Roundabout"):600,
        ("Faculty of Industrial Technology and Management", "Faculty of Agro-industry"):850,
        ("Faculty of Industrial Technology and Management", "Male Dormitory"):1700,
        ("Faculty of Industrial Technology and Management", "FeMale Dormitory1"):1900,
        ("Faculty of Industrial Technology and Management", "FeMale Dormitory2"):1900,
        ("Faculty of Industrial Technology and Management", "Sport Complex Building2"):2000,
        ("Faculty of Industrial Technology and Management", "Faculty of Engineering"):900,
        ("Faculty of Industrial Technology and Management", "Administration Building"):700,
        ("Faculty of Industrial Technology and Management", "Central Library Office"):500	
        }		

    BNG = {
        ("Faculty of Engineering", "Guardhouse"):3200,
        ("Faculty of Engineering", "Grand Palace"):3000,
        ("Faculty of Engineering", "Villa Vichalai Hotel"):2700,
        ("Faculty of Engineering", "Faculty of Business Administration and Service Industry"):2700,
        ("Faculty of Engineering", "Roundabout"):1200,
        ("Faculty of Engineering", "Faculty of Agro-industry"):1700,
        ("Faculty of Engineering", "Male Dormitory"):2400,
        ("Faculty of Engineering", "FeMale Dormitory1"):2500,
        ("Faculty of Engineering", "FeMale Dormitory2"):2600,
        ("Faculty of Engineering", "Faculty of Industrial Technology and Management"):900,
        ("Faculty of Engineering", "Sport Complex Building2"):2600,
        ("Faculty of Engineering", "Administration Building"):1500,
        ("Faculty of Engineering", "Central Library Office"):1200	
        }

    Admin_build = {
        ("Administration Building", "Guardhouse"):2500,
        ("Administration Building", "Grand Palace"):2300,
        ("Administration Building", "Villa Vichalai Hotel"):2000,
        ("Administration Building", "Faculty of Business Administration and Service Industry"):2100,
        ("Administration Building", "Roundabout"):400,
        ("Administration Building", "Faculty of Agro-industry"):140,
        ("Administration Building", "Male Dormitory"):1700,
        ("Administration Building", "FeMale Dormitory1"):1800,
        ("Administration Building", "FeMale Dormitory2"):1900,
        ("Administration Building", "Faculty of Industrial Technology and Management"):700,
        ("Administration Building", "Sport Complex Building2"):1900,
        ("Administration Building", "Faculty of Engineering"):1500,
        ("Administration Building", "Central Library Office"):350	
        }

    # Define other locations similarly

    distances = create_distance_dict(Guardhouse)

    print("Welcome to the Travel Planner!")
    
    current_location = None  # Track the current location

    while True:
        if current_location is None:
            print("\nAvailable starting locations:")
            for i, location in enumerate(distances.keys(), start=1):
                print(f"{i}. {location}")
        else:
            print(f"\nYou are currently at {current_location}.")
            display_destinations(current_location, distances)

        start_choice = input("\nEnter the number of your starting location, 'back' to choose a different starting location, or 'exit' to quit: ").strip()

        if start_choice.lower() == 'exit':
            print("Exiting program...")
            break

        if start_choice.lower() == 'back':
            current_location = None
            continue

        try:
            start_index = int(start_choice)
            if 1 <= start_index <= len(distances):
                current_location = list(distances.keys())[start_index - 1]

                while True:
                    display_destinations(current_location, distances)

                    destination_choice = input("\nEnter the number of the destination you want to travel to or 'back' to choose a different starting location: ").strip()

                    if destination_choice.lower() == 'back':
                        break

                    try:
                        destination_index = int(destination_choice)
                        destinations = list(distances[current_location].keys())
                        if 1 <= destination_index <= len(destinations):
                            destination = destinations[destination_index - 1]
                            print(f"\nYou have chosen to travel from {current_location} to {destination}.")
                            print(f"The distance between {current_location} and {destination} is {distances[current_location][destination]} meters.")
                            current_location = destination  # Update current location
                        else:
                            print("Invalid number. Please choose a number from the list.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_destinations(location, distances):
    print(f"\nAvailable destinations from {location}:")
    destinations = distances[location]
    for i, destination in enumerate(destinations.keys(), start=1):
        print(f"{i}. {destination}")

if __name__ == "__main__":
    main()