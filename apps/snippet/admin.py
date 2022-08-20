from django.contrib import admin
from snippet.models import Snippet


@admin.register(Snippet)
class AllFieldsAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
