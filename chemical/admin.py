from django.contrib import admin

# Register your models here.

# import model Chemical_Reaction
from .models import Chemical_Reaction

admin.site.register(Chemical_Reaction)
