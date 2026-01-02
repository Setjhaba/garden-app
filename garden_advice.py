def get_user_input(prompt):
    return input(prompt).lower()


def get_season_advice(season):
    # Determine advice based on user input of  the season
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    # Determine advice based on user input of the plant type
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."    


def generate_advice(season, plant_type):
    # Variable to hold gardening advice
    advice = ""
    advice += get_season_advice(season)
    advice += get_plant_advice(plant_type)
    return advice


def main():
    # Season variable that takes in user input
    # and converts it to lower case.
    season = get_user_input("Enter the season that you are in: ")

    # Plant_type variable that takes in user input
    # and converts it to lowercase.
    plant_type = get_user_input("Enter the plant type: ")

    advice = generate_advice(season, plant_type)

    # Print the generated advice
    print(advice)


if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
