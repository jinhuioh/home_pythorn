from django.contrib import admin

# Register your models here.
import bbs.models
import member.models

admin.site.register(bbs.models.Bbs)