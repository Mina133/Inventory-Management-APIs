from django.contrib import admin
from .models import Items, Categories, staff_member, Store
# Register your models here.

admin.site.register(Items)
admin.site.register(Categories)
admin.site.register(staff_member)
admin.site.register(Store)
