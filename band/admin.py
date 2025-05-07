from django.contrib import admin
from band.models import Musician

@admin.register(Musician)

class MusicianAdmin(admin.ModelAdmin):
    pass
# Register your models here.
