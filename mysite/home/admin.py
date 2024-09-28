from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import HomePage

class HomePageAdmin(ModelAdmin):
    model = HomePage
    menu_label = 'Home Page'
    menu_icon = 'home'
    list_display = ('title',)

modeladmin_register(HomePageAdmin)
