# Match Case Statements


def check_light(color):
    """Prints the action based on the traffic light color."""

    # The 'match' statement evaluates the 'color' variable.
    match color:

        # Case 1: Matches the exact string "red".
        case "red":
            print("Action: STOP!")

        # Case 2: Matches the exact string "yellow".
        case "yellow":
            print("Action: Prepare to stop.")

        # Case 3: Matches the exact string "green".
        case "green":
            print("Action: GO.")

        # Default Case: Matches anything else (like "blue" or "broken").
        case _:
            print("Action: Unrecognized or flashing light.")


# --- Demonstration ---
check_light("green")
check_light("red")
check_light("blue")