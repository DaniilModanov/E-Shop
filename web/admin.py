from django.contrib import admin
from web import models

shopModels = [models.GoodCard, models.GoodCategory]
admin.site.register(shopModels)
