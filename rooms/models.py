from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


# Create your models here.
class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # foreign key는 한 모델을 다른 모델과 연결시켜주는 역할을 한다.
    # foreign key는 일대다 관계이다.
    # 100개의 룸을 만들면 그 룸은 한 user를 가리킬 것이다.
    # user는 foreign key가 필요없기 때문에 따로 필드를 가지고 있지 않다.
    # 해당 내용은 #4.2 참조
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
