from django.contrib import admin
# import your models here
from .models import Finch, Feeding, Toy

admin.site.register(Finch)
# Register your models here.
admin.site.register(Feeding)
admin.site.register(Toy)