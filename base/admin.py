from django.contrib import admin

# Register your models here.



from django.contrib import admin
from .models import Project, Tag, Skills


# Register your models here.
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Skills)