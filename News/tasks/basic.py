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