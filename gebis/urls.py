from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from djgeojson.views import GeoJSONLayerView
from gebis.models import Gebaeude, Raeume, Mitarbeiter

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'gebis.views.index'),
    url(r'^data_gebaeude.geojson$', GeoJSONLayerView.as_view(model=Gebaeude), name='data_gebaeude'),
    url(r'^data_raeume.geojson$', GeoJSONLayerView.as_view(model=Raeume, properties=('raum_nr','nutzung','abteilung','flaeche','etage', 'mitarbeiter_by_room')), name='data_raeume'),
)
