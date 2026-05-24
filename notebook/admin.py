from django.contrib import admin
from .models import MainCategory, SubCategory, Note, Command

# Register your models here.
admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Note)
admin.site.register(Command)