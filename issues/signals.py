from django.db.models.signals import post_save
from django.dispatch import receiver

from issues.models import Issue
from .tasks import send_issue_email


@receiver(post_save, sender=Issue)
def send_new_issue_notification(sender, instance, created, **kwargs):
    if created:
        send_issue_email.delay(
            instance.id,
            instance.created_at,
            instance.description,
            instance.requester,
            instance.requester_email,
        )



