# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models

class Flure(models.Model):
    id = models.IntegerField(primary_key=True)
    etage = models.CharField(max_length=10)
    gebaeude = models.CharField(max_length=20)
    geom = models.PolygonField(srid=3857, blank=True, null=True)
    art = models.CharField(db_column='Art', max_length=10, blank=True) # Field name made lowercase.
    objects = models.GeoManager()
    class Meta:
        managed = True
        db_table = 'flure'

class Gebaeude(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    stadt = models.CharField(max_length=20)
    land = models.CharField(max_length=20)
    geom = models.PolygonField(srid=0, blank=True, null=True)
    objects = models.GeoManager()
    class Meta:
        managed = True
        db_table = 'gebaeude'

class Installationen(models.Model):
    id = models.IntegerField(primary_key=True)
    etage = models.CharField(max_length=10)
    gebaeude = models.CharField(max_length=20)
    art = models.CharField(max_length=10)
    geom = models.PolygonField(srid=3857, blank=True, null=True)
    objects = models.GeoManager()
    class Meta:
        managed = True
        db_table = 'installationen'

class Mitarbeiter(models.Model):
    id = models.IntegerField(primary_key=True)
    fk_raeume = models.ForeignKey('Raeume', db_column='fk_raeume', blank=True, null=True, related_name="mitarbeiter")
    name = models.CharField(max_length=20,blank=True)
    info = models.CharField(max_length=40,blank=True)
    class Meta:
        managed = True
        db_table = 'mitarbeiter'
    def __unicode__(self):
        return self.name or u'Kein Name'

class Raeume(models.Model):
    id = models.IntegerField(primary_key=True)
    raum_nr = models.CharField(max_length=20)
    abteilung = models.CharField(max_length=20)
    gebaeude = models.CharField(max_length=20)
    flaeche = models.FloatField()
    geom = models.PolygonField(srid=3857, blank=True, null=True)
    nutzung = models.CharField(db_column='Nutzung', max_length=20, blank=True) # Field name made lowercase.
    etage = models.SmallIntegerField(db_column='Etage', blank=True, null=True) # Field name made lowercase.
    objects = models.GeoManager()
    @property
    def mitarbeiter_by_room(self):
        return [mitarbeiter.name for mitarbeiter in self.mitarbeiter.all()]
    def __unicode__(self):
        return self.raum_nr or u''
    class Meta:
        managed = True
        db_table = 'raeume'

