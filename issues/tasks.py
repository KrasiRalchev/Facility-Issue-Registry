from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_issue_email(issue_id, created_at, description, requester, email):
    print("TASK STARTED")
    send_mail(
        subject='Facility Issue',
        message=f"Issue with number ISD-{issue_id} from {created_at.date()} with comment "
                f"'{description}' registered from {requester}"
                f" has been created!",
        from_email=settings.FROM_EMAIL,
        recipient_list=[email],
    )

