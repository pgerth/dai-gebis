from django.contrib.gis import admin
from gebis.models import Raeume, Mitarbeiter, Gebaeude, Flure

class MitarbeiterInline(admin.TabularInline):
	model = Mitarbeiter
	extra = 0

class GebisAdmin(admin.OSMGeoAdmin):
	fields = ['id', 'raum_nr', 'flaeche', 'nutzung','abteilung', 'etage', 'gebaeude']
	inlines = [MitarbeiterInline]
	list_display = ['raum_nr','nutzung','gebaeude','flaeche','mitarbeiter_by_room']
	list_filter = ['abteilung']
	search_fields = ['raum_nr','nutzung']

admin.site.register(Raeume, GebisAdmin)
admin.site.register(Mitarbeiter, admin.OSMGeoAdmin)