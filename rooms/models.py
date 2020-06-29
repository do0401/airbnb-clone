from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract: True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Model Definition """
    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """ Amenity Model Definition """
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Factility Model Definition """
    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """
    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    # 파이썬은 파일을 상하수직방향으로 읽는다.
    # 그래서 아래 "Room"을 string 방식이 아닌 그냥 Room 으로 정의하면
    # Room class는 Photo class보다 아래에 있으므로 찾지 못한다.
    # 이런 경우, Photo class를 Room class 밑으로 옮겨주거나
    # 아래와 같이 string 방식으로 사용하면 된다.
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


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
    # on_delete는 User 모델이 삭제되면 해당 User 모델에 속해있던 Room도 삭제된다는 것이다.
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    factilites = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
