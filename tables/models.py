from django.db import models

class Origin(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField()

    class Meta:
        db_table = 'origin'
        
class Location(models.Model):
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=255)
    dimension = models.CharField(max_length=255)
    residents = models.TextField()
    url = models.URLField()
    created = models.DateTimeField()

    class Meta:
        db_table = 'location'

class Episode(models.Model):
    name = models.CharField(max_length=255, unique=True)
    air_date = models.DateTimeField()
    episode = models.CharField(max_length=255)
    characters = models.ManyToManyField('Character', through='Character2Episode', related_name='character_reverse')
    url = models.URLField()
    created = models.DateTimeField()

    class Meta:
        db_table = 'episode'

class Character(models.Model):
    STATUS_CHOICES = (
        (1, 'Dead'),
        (2, 'Alive'),
        (3, 'Unknown'),
    )
    GENDER_CHOICES = (
        (1, 'Female'),
        (2, 'Male'),
        (3, 'Genderless'),
        (4, 'Unknown'),
    )
    SPECIES_CHOICES = (
        (1, 'Human'),
        (2, 'Alien'),
        (3, 'Mythological'),
        (4, 'Unknown'),
        (5, 'Animal'),
        (6, 'Disease'),
        (7, 'Robot'),
        (8, 'Croneberg'),
    )
    
    name = models.CharField(max_length=255, unique=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    species = models.IntegerField(choices=SPECIES_CHOICES)
    type = models.CharField(max_length=255)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    episodes = models.ManyToManyField('Episode', through='Character2Episode', related_name='episode_reverse')
    image = models.CharField(max_length=255)
    url = models.URLField()
    created = models.DateTimeField() 

    class Meta:
        db_table = 'character'

class Character2Episode(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)

    class Meta:
        db_table = 'character2episode'
