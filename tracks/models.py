from django.db import models

#We are just defining objects here that will be used to store data and retrieve data from.
#This is also referred to mapping tables to objects, a technology known as ORM(Object Relational Mapping is what allows us to do this) so ORM is applied within this models module
class Artist(models.Model):
    name = models.CharField(max_length=200, db_index=True, help_text='Artist name')

    def __str__(self):
        """string for displaying the Artist object"""
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=200, db_index=True, help_text='Genre of music(i.e Blues)')

    """string for displaying the Genre object"""
    def __str__(self):
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=200, db_index=True, help_text='Album titile')
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)

    """String for displaying the Album object"""
    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=200, db_index=True, help_text='Track title')
    rating = models.IntegerField(null=True)#optional or nullable with an integer datatype hence numbers only
    length = models.IntegerField(null=True)#optional or nullable with an integer datatype hence numbers only
    count = models.IntegerField(null=True)#optional or nullablee with an integer datatype hence numbers only
    album= models.ForeignKey('Album', on_delete=models.CASCADE)
    gendre = models.ForeignKey('Genre', on_delete=models.SET_NULL,null= True)
    
    """string to display the Track object"""
    def __str__(self):
        return self.title
