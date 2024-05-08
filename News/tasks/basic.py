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
        user_name.append(user.email)
    return user_name

def new_post_subscription(instance):
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