import os
import json
import pytz 
import django
import datetime
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'db.settings')
django.setup()

from tables.models import Origins, Characters, Locations, Characters2Episodes

STATUS_MAPPING = {'Dead': 0, 'Alive': 1, 'Unknown': 2}
GENDER_MAPPING = {'Female': 0, 'Male': 1, 'Genderless': 2, 'Unknown': 3}
SPECIES_MAPPING = {'Human': 0, 'Alien': 1, 'Mythological': 2, 'Unknown': 3, 'Animal': 4, 'Disease': 5, 'Robot': 6, 'Croneberg': 7}

def populate_database_from_json_1(json_file_path1):
    with open(json_file_path1, 'r') as file:
        data = json.load(file)
        for item in data:
            created_str = item.get('created')
            created_datetime = datetime.datetime.strptime(created_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            created_datetime = pytz.utc.localize(created_datetime) 

            status = item.get('status', 'Unknown')  
            status_index = STATUS_MAPPING.get(status, 2)

            gender_index = GENDER_MAPPING.get(item.get('gender', 'Unknown'), 3)
            species_index = SPECIES_MAPPING.get(item.get('species', 'Unknown'), 3)
            origin_name = item.get('origins', {}).get('name')

            origin, _ = Origins.objects.get_or_create(name=origin_name)
            location_name = item.get('location', {}).get('name')

            try:
                location = Locations.objects.filter(name=location_name).first()
            except Locations.DoesNotExist:
                location = None  

            existing_character = Characters.objects.filter(name=item.get('name')).first()

            if existing_character:
                continue
            character = Characters.objects.create(
                name=item.get('name'),
                status=status_index,  
                species=species_index,
                type=item.get('type'),
                gender=gender_index,
                origin=origin,
                location=location,
                image=item.get('image'),
                url=item.get('url'),
                created=created_datetime
            )
            
 
def populate_database_from_json_2(json_file_path2):
    from tables.models import  Locations
    with open(json_file_path2, 'r') as file:
        data = json.load(file)
            
        for item in data:
            created_str = item.get('created')
            created_datetime = datetime.datetime.strptime(created_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            created_datetime = pytz.utc.localize(created_datetime) 

            location = Locations.objects.create(
                name=item.get('name'),
                type=item.get('type'),
                dimension=item.get('dimension'),
                residents=item.get('residents'),
                url = item.get('url'),
                created=created_datetime
                 )
            
def populate_database_from_json_3(json_file_path3):
    from tables.models import Episodes
    with open(json_file_path3, 'r') as file:
        data = json.load(file)

        for item in data:
            created_str = item.get('created')
            created_datetime = datetime.datetime.strptime(created_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            created_datetime = pytz.utc.localize(created_datetime) 

            air_date_str = item.get('air_date')
            air_date_datetime = datetime.datetime.strptime(air_date_str,  "%B %d, %Y")
            air_date_datetime = pytz.utc.localize(air_date_datetime) 

            episode = Episodes.objects.create(
                name=item.get('name'),
                air_date=air_date_datetime,
                episode=item.get('episode'),
                url=item.get('url'),
                created=created_datetime
            )
            characters_data = item.get('characters', [])
            for character_name in characters_data:
                character, _ = Characters.objects.get_or_create(name=character_name)
                Characters2Episodes.objects.get_or_create(character=character, episode=episode)
        
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'db.settings')
    django.setup()
    
    json_file_path1 = 'db/data/character_data.json'
    populate_database_from_json_1(json_file_path1)

    json_file_path2 = 'db/data/location_data.json'
    populate_database_from_json_2(json_file_path2)

    json_file_path3 = 'db/data/episode_data.json'
    populate_database_from_json_3(json_file_path3)
    
if __name__ == '__main__':
    main()