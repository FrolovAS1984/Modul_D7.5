from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from news.models import Post
from project import settings
from news.tasks import send_notifications

# def send_notifications(preview, pk, title, subscribers):
#     html_content = render_to_string(
#         'post_created_email.html',
#         {
#             'text': preview,
#             'link': f'{settings.SITE_URL}/news/{pk}'
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject=title,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers,
#     )
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()


@receiver(post_save, sender=Post)
def notify_about_new_post(instance, created, **kwargs):
    if not created:
        return
    categories = instance.category
    subscribers: list[str] = []
    subscribers += categories.subscribers.all()
    subscribers = [s.email for s in subscribers]

    send_notifications.delay(instance.preview(), instance.pk, instance.title, subscribers)


