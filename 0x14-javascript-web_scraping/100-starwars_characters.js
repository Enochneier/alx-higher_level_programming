#!/usr/bin/node
import sys
import requests

def get_movie_characters(movie_id):
    url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(url)

    if response.status_code == 200:
        film_data = response.json()
        characters = film_data['characters']
        for character_url in characters:
            character_response = requests.get(character_url)
            if character_response.status_code == 200:
                character_data = character_response.json()
                print(character_data['name'])
            else:
                print(f"Failed to retrieve character data for {character_url}")
    else:
        print(f"Failed to retrieve movie data for movie ID {movie_id}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <movie_id>")
        sys.exit(1)

    movie_id = sys.argv[1]
    get_movie_characters(movie_id)

