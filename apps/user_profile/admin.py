from django.contrib import admin
from user_profile.models import UserProfile


@admin.register(UserProfile)
class AllFieldsAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
