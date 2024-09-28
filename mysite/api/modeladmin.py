from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import SubscriptionPlan, UserSubscription

class SubscriptionPlanAdmin(ModelAdmin):
    model = SubscriptionPlan
    menu_label = 'Subscription Plans'
    menu_icon = 'doc-full-inverse'
    list_display = ('name', 'price', 'description')

class UserSubscriptionAdmin(ModelAdmin):
    model = UserSubscription
    menu_label = 'User Subscriptions'
    menu_icon = 'group'
    list_display = ('user', 'plan', 'active', 'start_date', 'end_date')

modeladmin_register(SubscriptionPlanAdmin)
modeladmin_register(UserSubscriptionAdmin)
