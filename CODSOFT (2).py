# Define some movies with their genres
movies = {
    "The Shawshank Redemption": ["Drama", "Crime","drama","crime"],
    "The Godfather": ["Drama", "Crime","drama","crime"],
    "The Dark Knight": ["Action", "Crime", "Drama","action","drama","crime"],
    "Pulp Fiction": ["Crime", "Drama","crime","drama"],
    "Forrest Gump": ["Drama", "Romance","drama","romance"],
    "Inception": ["Action", "Adventure", "Sci-Fi","action","adventure","sci-fi"],
    "The Matrix": ["Action", "Sci-Fi","action","sci-fi"],
    "Schindler's List": ["Biography", "Drama", "History","biogrsspthy","drama","history"],
    "Fight Club": ["Drama","drama"],
    "Goodfellas": ["Biography", "Crime", "Drama","biography","drama","crime"],
}

# Function to recommend movies based on user preferences
def recommend_movies(user_preferences, movies):
    recommended_movies = []
    for movie, genres in movies.items():
        if any(genre in user_preferences for genre in genres):
            recommended_movies.append(movie)
    return recommended_movies

# Main
if __name__ == "__main__":
    print("Welcome to the Movie Recommendation System!")
    print("Enter your movie preferences separated by commas (e.g., Action, Drama):")
    user_input = input("Your Preferences: ").split(", ")
    
    recommended_movies = recommend_movies(user_input, movies)
    
    if recommended_movies:
        print("Recommended Movies:")
        for movie in recommended_movies:
            print("-", movie)
    else:
        print("Sorry, no movies match your preferences.")
