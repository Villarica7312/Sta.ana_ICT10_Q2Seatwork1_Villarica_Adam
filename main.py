from pyscript import document

# list of club members (based on famous singers)
club_members = [
    "Taylor Swift",
    "Bruno Mars",
    "Ariana Grande",
    "Ed Sheeran",
    "Billie Eilish",
    "Drake",
    "Rihanna"
]

# the two possible messages, True is for on the list and False is for not on the list
messages = {
    True: "Congratulations {name}! You are now part of the ICT club.",
    False: "Sorry {name}, your name is not on the list."
}

def check_name(event):
    # get what the user typed in the two boxes
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value

    # combine first and last name into one full name
    # strip removes extra spaces and title makes it like "Taylor Swift"
    full_name = (first.strip() + " " + last.strip()).title()

    # check if the full name is in the list and save the answer (True or False)
    is_member = full_name in club_members

    # pick the right message using the answer, then put the name in it
    message = messages[is_member].format(name=full_name)

    # show the message in the result area
    document.getElementById("result").innerText = message
