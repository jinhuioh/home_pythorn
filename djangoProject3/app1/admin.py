from django.contrib import admin

# Register your models here.
import app1.models

admin.site.register(app1.models.product)