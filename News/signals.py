from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import PostCategory
from .tasks import send_welcome_email, new_post_subscription
from django.contrib.auth.models import User
from celery import shared_task


@shared_task
@receiver(m2m_changed, sender=PostCategory)
def notify_subscribers(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        pass
        new_post_subscription(instance)

@shared_task
@receiver(post_save, sender=User)
def create_user_welcome_email(sender, instance=None, created=False, **kwargs):
    if created:
        send_welcome_email(instance)

