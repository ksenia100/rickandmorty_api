import requests
import json

def download_character_data():
    base_url = "https://rickandmortyapi.com/api/character"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        total_pages = data["info"]["pages"]
        
        all_characters = []
        for page_num in range(1, total_pages + 1):
            page_url = f"{base_url}?page={page_num}"
            page_response = requests.get(page_url)
            if page_response.status_code == 200:
                page_data = page_response.json()
                all_characters.extend(page_data["results"])
            else:
                print(f"Failed to download data for page {page_num}.")
        
        with open("data/character_data.json", "w") as file:
            json.dump(all_characters, file)
        
        print("Character data downloaded successfully!")
    else:
        print("Failed to download character data.")

if __name__ == "__main__":
    download_character_data()

def download_episode_data():
    base_url = "https://rickandmortyapi.com/api/episode"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        total_pages = data["info"]["pages"]
        
        all_episodes = []
        for page_num in range(1, total_pages + 1):
            page_url = f"{base_url}?page={page_num}"
            page_response = requests.get(page_url)
            if page_response.status_code == 200:
                page_data = page_response.json()
                all_episodes.extend(page_data["results"])
            else:
                print(f"Failed to download data for page {page_num}.")
        
        with open("data/episode_data.json", "w") as file:
            json.dump(all_episodes, file)
        
        print("Episode data downloaded successfully!")
    else:
        print("Failed to download episode data.")

if __name__ == "__main__":
    download_episode_data()

def download_location_data():
    base_url = "https://rickandmortyapi.com/api/location"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        total_pages = data["info"]["pages"]
        
        all_locations = []
        for page_num in range(1, total_pages + 1):
            page_url = f"{base_url}?page={page_num}"
            page_response = requests.get(page_url)
            if page_response.status_code == 200:
                page_data = page_response.json()
                all_locations.extend(page_data["results"])
            else:
                print(f"Failed to download data for page {page_num}.")
        
        with open("data/location_data.json", "w") as file:
            json.dump(all_locations, file)
        
        print("Location data downloaded successfully!")
    else:
        print("Failed to download location data.")

if __name__ == "__main__":
    download_location_data()