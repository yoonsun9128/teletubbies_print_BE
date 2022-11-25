from django.contrib import admin
from store.models import Filter, Filter_option, Review
# Register your models here.

admin.site.register(Filter)
admin.site.register(Filter_option)
admin.site.register(Review)
