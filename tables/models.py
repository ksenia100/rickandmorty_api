from django.db import models

class Origins(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        db_table = 'origins'
        
class Locations(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    dimension = models.CharField(max_length=255)
    residents = models.TextField()
    url = models.URLField()
    created = models.DateTimeField()

    class Meta:
        db_table = 'locations'

class Episodes(models.Model):
    name = models.CharField(max_length=255)
    air_date = models.DateTimeField()
    episode = models.CharField(max_length=255)
    characters = models.ManyToManyField('Characters', through='Characters2Episodes', related_name='characters_reverse')
    url = models.URLField()
    created = models.DateTimeField()

    class Meta:
        db_table = 'episodes'

class Characters(models.Model):
    STATUS_CHOICES = (
        (0, 'Dead'),
        (1, 'Alive'),
        (2, 'Unknown'),
    )
    GENDER_CHOICES = (
        (0, 'Female'),
        (1, 'Male'),
        (2, 'Genderless'),
        (3, 'Unknown'),
    )
    SPECIES_CHOICES = (
        (0, 'Human'),
        (1, 'Alien'),
        (2, 'Mythological'),
        (3, 'Unknown'),
        (4, 'Animal'),
        (5, 'Disease'),
        (6, 'Robot'),
        (7, 'Croneberg'),
    )
    
    name = models.CharField(max_length=255, unique=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    species = models.IntegerField(choices=SPECIES_CHOICES)
    type = models.CharField(max_length=255)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    origin = models.ForeignKey(Origins, on_delete=models.CASCADE)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    episodes = models.ManyToManyField('Episodes', through='Characters2Episodes', related_name='episodes_reverse')
    image = models.CharField(max_length=255)
    url = models.URLField()
    created = models.DateTimeField() 

    class Meta:
        db_table = 'characters'

class Characters2Episodes(models.Model):
    characters = models.ForeignKey(Characters, on_delete=models.CASCADE)
    episodes = models.ForeignKey(Episodes, on_delete=models.CASCADE)

    class Meta:
        db_table = 'characters2episodes'