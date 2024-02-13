# Install requests library if not already installed
# pip install requests

import requests

def get_movie_with_min_rating(username, min_rating=3):
    api_url = f'https://api.letterboxd.com/api/v0f1/members/{username}/films/'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        movies = response.json().get('items', [])
        filtered_movies = [movie for movie in movies if movie.get('rating') and movie['rating'] >= min_rating]
        
        if filtered_movies:
            return filtered_movies[0]['name']
        else:
            return "No movies with at least 3 stars found."
    else:
        return "Error accessing Letterboxd API."

# Replace 'your_username' with your Letterboxd username
result = get_movie_with_min_rating('your_username')
print(result)