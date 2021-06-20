from django.contrib import admin
from .models import *


admin.site.register(Article)
admin.site.register(News)
admin.site.register(Tag)
admin.site.register(TypeTag)

