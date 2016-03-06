from django.db import models


class Ruta(models.Model):
	trailId=models.CharField(max_length=100)
	originStationName=models.CharField(max_length=100)
	destinationStationName=models.CharField(max_length=100)
	transportType=models.CharField(max_length=100)
	maxTariff=models.CharField(max_length=100)
	photoUrl=models.URLField(max_length=500)
	notes=models.TextField()
	totalMinutes=models.IntegerField()
	totalMeters=models.FloatField()
	gtfsStatus=models.IntegerField()
	primerPuntolat=models.CharField(max_length=100,blank=True,null=True)
	primerPuntolon=models.CharField(max_length=100,blank=True,null=True)
	ultimoPuntolat=models.CharField(max_length=100,blank=True,null=True)
	ultimoPuntolon=models.CharField(max_length=100,blank=True,null=True)
	def __str__(self):
		return self.originStationName + " -- "+self.destinationStationName

class Punto(models.Model):
	latitude=models.FloatField()
	longitude=models.FloatField()
	ruta_id=models.CharField(max_length=100)
	trail=models.ForeignKey(Ruta,related_name='puntos')

	def __str__(self):
		return self.ruta_id


