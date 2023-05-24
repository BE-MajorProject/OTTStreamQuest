from django.contrib import admin

from movie.models import ConfirmBooking, Movie, ott_plans

# Register your models here.

admin.site.register(Movie)
admin.site.register(ott_plans)
admin.site.register(ConfirmBooking)