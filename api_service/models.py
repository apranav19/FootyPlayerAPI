from django.db import models

'''
    This model represents a football (soccer) player
    The attributes include:
        first_name - The first name of the player
        last_name - The last name of the player
        club - The player's club
        country - The international team that the player plays for
        age - The player's age
        position - The player's position on the field
        kit_number - The player's kit number
'''
class FootballPlayer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    club = models.CharField(max_length=50) # In the future, we'll replace this field type
    country = models.CharField(max_length=50) # Also requires an update in the future
    position = models.CharField(max_length=50)
    kit_number = models.IntegerField()
