from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from .models import Task

@receiver(post_save, sender=Task)
def task_reminder_email(sender, instance, created, **kwargs):
  if not instance.is_complete:
    now = timezone.now()
    one_hour_from_now = now + timedelta(hours=1)
    if now < instance.due_date <= one_hour_from_now:
      subject = f"Reminder: Your task '{instance.title}' is due soon!"
      message = (
        f"Hello {instance.user.username}, \n\n"
        f"Your task '{instance.title}' is due on {instance.due_date.strftime('%Y-%m-%d at %H:%M %Z')}. \n\n"
        f"Description: {instance.description or 'No description.'}\n\n"
        f"You still have time to complete it!\n\n"
      )
      from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'webmaster@localhost')
      recipient_list = [instance.user.email]

      if recipient_list[0]:
        try:
          send_mail(subject, message, from_email, recipient_list, fail_silently=False)
          print(f"Email reminder for '{instance.title}' sent to {instance.user.email}")
        except Exception as e:
          print(f"Error sending email for '{instance.title}': {e}")
      else:
        print(f"Skipping email for '{instance.title}', user {instance.user.username} email not found.")
    else:
      print(f"Task '{instance.title}' due date is not within an hour from now, or has already passed.")
  else:
    print(f"Task: {instance.title} is already complete.")