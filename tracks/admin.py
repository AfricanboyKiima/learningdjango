from django.contrib import admin
from .models import Track,Album,Artist,Genre
# Register your models here.


admin.site.register(Track)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Artist)