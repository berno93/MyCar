from django.contrib import admin

# Importation de notre models
from django.apps import apps
CarPost = apps.get_model(app_label='MyCar', model_name='CarPost')


class MyCarPostAdmin(admin.ModelAdmin):
    list_display = ("title","price","photo","content","published", "created_on", "last_updated")
    list_editable = ("published", )
    
admin.site.register(CarPost, MyCarPostAdmin)