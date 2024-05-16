from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
def get_subscribers(category):
    user_email = []
    for user in category.subscribers.all():
        user_email.append(user.email)
    return user_email

def get_names(category):
    user_name = []
    for user in category.subscribers.all():
        user_name.append(user.username)
    return user_name



def new_post_subscription(instance,):
    template = 'mail/new_post.html'

    for category in instance.category.all():
        email_subject = f"New post in category: '{category}' "
        user_emails = get_subscribers(category)
        user_names = get_names(category)

        html = render_to_string(
            template_name=template, 
            context={
                'category': category,
                'post': instance,
                'username': user_names,
                'link': f'http://127.0.0.1:8000/post/{instance.id}'
                }

        )
        msg = EmailMultiAlternatives(
            subject = email_subject,
            body = '',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=user_emails

        )

        msg.attach_alternative(html, 'text/html')
        msg.send()


def send_welcome_email(user):
    template = 'mail/welcome.html'

    html = render_to_string(
        template_name=template,
        context={
            'username': user.username,
        }
    )

    msg = EmailMultiAlternatives(
        subject = 'Welcome to our NewsPortal!',
        body = '',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
    )

    msg.attach_alternative(html, 'text/html')
    msg.send()




import logging
 
from django.conf import settings
 
from News.models import Post, Category
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
import datetime
from celery import shared_task


logger = logging.getLogger(__name__)
 
 
# наша задача по выводу текста на экран
@shared_task
def notify_every_monday():
    #  Your job processing logic here... 
   today = datetime.datetime.now()
   last_week = today - datetime.timedelta(days=7)
   posts = Post.objects.filter(time_in__gte=last_week)
   categories = set(posts.values_list('category__name', flat=True))
   link = 'http://127.0.0.1:8000'
   subscribers = Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True)
   html_content = render_to_string(
       'daily_mail.html',
       {'posts': posts,
        'link': link})
   
   msg = EmailMultiAlternatives(
       subject='Новости за неделю',
       body='',
       from_email=settings.EMAIL_HOST_USER,
       to=subscribers,)
   
   msg.attach_alternative(html_content, "text/html")
   msg.send()


