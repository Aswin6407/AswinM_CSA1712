def vacuum_cleaner():
    rooms = {"A": "Dirty", "B": "Dirty"}
    location = "A"

    while "Dirty" in rooms.values():
        print("Vacuum is in Room", location)

        if rooms[location] == "Dirty":
            rooms[location] = "Clean"
            print("Room", location, "cleaned")

        if location == "A":
            location = "B"
        else:
            location = "A"

    print("All rooms are clean!")
    print(rooms)


vacuum_cleaner()