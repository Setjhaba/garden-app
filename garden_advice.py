def get_user_input(prompt):
    """
    Get user input and convert it to lowercase.
    """
    return input(prompt).lower()


# Dictionary for advice on different seasons
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n",
    "spring": "Perfect time for planting and pruning.\n",
    "autumn": "Reduce watering and prepare plants for cooler weather.\n"
}

# Dictionary for advice on different plant types
PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "tree": "Ensure deep watering and mulch around the base.",
    "herb": "Harvest regularly to encourage growth."
}


def get_season_advice(season):
    """
    Return advice for the given season by user
    """
    return SEASON_ADVICE.get(season, "No advice for this season. \n")


def get_plant_advice(plant_type):
    """
    Return advive for the given plant type by user
    """
    return PLANT_ADVICE.get(plant_type, "No advice for this season.\n")


def generate_advice(season, plant_type):
    """
    Generate advice from given input
    """
    advice = ""
    advice += get_season_advice(season)
    advice += get_plant_advice(plant_type) + "\n"

    return advice


def recommend_plants(season):
    """
    Recommend other plants to user based on their season input
    """
    # Dictionary of recommended plants based on season
    PLANT_RECOMMENDATIONS = {
        "summer": "Recommended plants: sunflower, tomato, basil",
        "winter": "Recommended plants: cabbage, spinach, garlic",
        "spring": "Recommended plants: rose, lettuce, peas",
        "autumn": "Recommended plants: broccoli, kale, beetroot"
    }

    # Get recommended plants based on season
    return PLANT_RECOMMENDATIONS.get(
        season,
        "No plant recommendations for this season."
    )


def main():
    # Season variable that takes in user input
    # using get_user_ input function
    # and converts it to lower case.
    season = get_user_input("Enter the season that you are in: ")

    # Plant_type variable that takes in user input
    # using get_user_ input function
    # and converts it to lowercase.
    plant_type = get_user_input("Enter the plant type: ")

    # Store output of generate_advice function
    advice = generate_advice(season, plant_type)

    # Store output of recommend_plants function
    recommendations = recommend_plants(season)

    # Print the generated advice
    print(advice)

    # Print recommended plants
    print(recommendations)


if __name__ == "__main__":
    main()
