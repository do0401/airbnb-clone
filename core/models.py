from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """
    # 장고가 새로운 모델을 만들면 현재 날짜와 시간을 여기에 넣어준다.
    created = models.DateTimeField(auto_now_add=True)
    # 모델을 저장할 때마다 항상 새로운 날짜를 써준다.
    updated = models.DateTimeField(auto_now=True)

    class Meta:
      abstract = True
