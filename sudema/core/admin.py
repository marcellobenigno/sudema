from django.contrib import admin
from django.forms.widgets import Textarea

from .models import *


class AreaInteresseAdmin(admin.ModelAdmin):
	list_display = ['nome', 'validado']
	search_fidels = ['nome',]
	list_filter = ['validado',]

	formfield_overrides = {
		models.PolygonField: {'widget': Textarea}
	}


admin.site.register(AreaInteresse, AreaInteresseAdmin)