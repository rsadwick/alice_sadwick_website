from django.contrib import admin
from baby.models import Baby, Rsvp, Article

class BabyAdmin(admin.ModelAdmin):
    # ...
    list_display = ('week', 'baby_title')

class RsvpAdmin(admin.ModelAdmin):
    list_display = ('name', 'coming')

class Articledmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


admin.site.register(Baby, BabyAdmin)
admin.site.register(Rsvp, RsvpAdmin)
admin.site.register(Article, Articledmin)