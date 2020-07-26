from django.conf import settings
from django.db.models.signals import post_save
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    bio = models.TextField(blank=True)
    website_url = models.URLField(blank=True)

def on_post_save_for_user(sender, **kwargs):    # kwargs에는 instance와 created라는 이름의 인자가 담겨서 온다
    if kwargs['created']:  # 현재 유저 모델에 대해 처음 생성이 되었을 때
        user = kwargs['instance']
        Profile.objects.create(user=user)

# connect(호출될 함수, 어떠한 모델 객체가 저장되고 나서)
post_save.connect(on_post_save_for_user,sender = settings.AUTH_USER_MODEL)