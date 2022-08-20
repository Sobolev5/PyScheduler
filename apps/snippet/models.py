from django.db import models


class Snippet(models.Model):
    user_profile = models.ForeignKey("user_profile.UserProfile", blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField("Cron", max_length=100, blank=True, null=True)
    description = models.CharField("Cron", max_length=1000, blank=True, null=True)
    cron_time = models.CharField("Cron", max_length=255)  
    exact_time = models.DateTimeField("Exact time", blank=True, null=True)
    code = models.TextField("Code", blank=True, null=True)
    last_execution_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
