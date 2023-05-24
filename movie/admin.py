from django.contrib import admin

from movie.models import Movie, ott_plans

# Register your models here.

admin.site.register(Movie),
admin.site.register(ott_plans)