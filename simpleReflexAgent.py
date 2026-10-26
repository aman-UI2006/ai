
def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"


# Environment
room = {"A": "Dirty", "B": "Dirty"}
location = "A"

print("Initial Environment:", room)

for i in range(5):
    status = room[location]
    action = vacuum_agent(location, status)

    print("Location:", location, "| Status:", status, "| Action:", action)

    if action == "Suck":
        room[location] = "Clean"
    elif action == "Right":
        location = "B"
    elif action == "Left":
        location = "A"

    if all(status == "Clean" for status in room.values()):
        print("Both rooms are clean!")
        break

print("Final Environment:", room)
