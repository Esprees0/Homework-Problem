class CampusMap:
    def __init__(self):
        self.distances = {}

    def add_distance(self, from_location, to_location, distance):
        if from_location not in self.distances:
            self.distances[from_location] = {}
        self.distances[from_location][to_location] = distance

    def get_distance(self, from_location, to_location):
        Place_in_uni = {
             "Guardhouse",
            "Grand Palace",
            "Villa Vichalai Hotel",
            "Faculty of Management",
            "Roundabout",
            "Faculty of Agricultural Industry",
            "Male Dormitory",
            "Female Dormitory1",
            "Female Dormitory2",
            "Sport Complex Building",
            "Faculty of Industrial Technology and Management",
            "Faculty of Engineering",
            "Administration Building"
        }
        if from_location in self.distances and to_location in self.distances[from_location]:
            return self.distances[from_location][to_location]
        else:
            return None

def main():
    print("You are now in front of the university. \nWhere do you want to go in university?")
    campus_map = CampusMap()
 
    campus_map.add_distance("Main Entrance", "Grand Palace", 175)
    campus_map.add_distance("Grand Palace", "Villa Vichalai Hotel", 300)
    campus_map.add_distance("Villa Vichalai Hotel", "Faculty of Management", 54)
    campus_map.add_distance("Faculty of Management", "Roundabout", 1500)
    campus_map.add_distance("Faculty of Management", "Male Dormitory", 2200)
    campus_map.add_distance("Male Dormitory", "Female Dormitory1", 130)
    campus_map.add_distance("Male Dormitory", "Female Dormitory2", 180)
    campus_map.add_distance("Female Dormitory1", "Female Dormitory2", 110)
    campus_map.add_distance("Male Dormitory", "Sport Complex Building", 40)
    campus_map.add_distance("Female Dormitory1", "Sport Complex Building", 100)
    campus_map.add_distance("Roundabout", "Sport Complex Building", 750)
    campus_map.add_distance("Roundabout", "Faculty of Agricultural Industry", 600)
    campus_map.add_distance("Faculty of Agricultural Industry", "Administration Building", 160)
    campus_map.add_distance("Roundabout", "Faculty of Industrial Technology and Management", 900)
    campus_map.add_distance("Faculty of Industrial Technology and Management", "Faculty of Engineering", 900)
    campus_map.add_distance("Faculty of Industrial Technology and Management", "Sport Complex Building", 2000)

    from_location = input("Enter starting location: ")
    to_location = input("Enter destination location: ")
    distance = campus_map.get_distance(from_location, to_location)
    if distance is not None:
        print(f"The distance from {from_location} to {to_location} is {distance} meters.")
    else:
        print("Sorry, the distance between the given locations is not available.")

if __name__ == "__main__":
    main()
