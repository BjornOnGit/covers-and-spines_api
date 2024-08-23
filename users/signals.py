from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry
from .models import CustomAdminLog

@receiver(post_save, sender=LogEntry)
def create_custom_log(sender, instance, **kwargs):
    CustomAdminLog.objects.create(
        action_time=instance.action_time,
        user=instance.user,
        content_type=instance.content_type,
        object_id=instance.object_id,
        object_repr=instance.object_repr,
        action_flag=instance.action_flag,
        change_message=instance.change_message,
    )
