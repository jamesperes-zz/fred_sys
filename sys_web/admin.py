from django.contrib import admin

# Register your models here.
from .models import Decisor, Criterio, Alternativa


admin.site.register(Decisor)

admin.site.register(Criterio)
admin.site.register(Alternativa)