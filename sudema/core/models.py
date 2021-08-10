from django.contrib.gis.db import models


class AreaInteresse(models.Model):
	nome = models.CharField('nome da área', max_length=20)
	validado = models.BooleanField('esta área foi validada?', default=False)
	geom = models.PolygonField('geom', srid=4326)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = "Área de Interesse"
		verbose_name_plural = "Áreas de Interesse"


