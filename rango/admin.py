from django.contrib import admin
from rango.models import Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
	list_display = ['title','category','url', 'views']

	fieldsets = [
	('Page', {'fields': ['title','url','category']}),
	('Stats', {'fields': ['views']})
	]

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','views','likes']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)