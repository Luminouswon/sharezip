from django.db import models
from django.utils import timezone

# Create your models here.
class Room(models.Model):
    start_date=models.DateField(default=timezone.now())
    end_date=models.DateField(default=timezone.now())
    rent_type=models.IntegerField(default=-1) # 양도 1, 기간대여 2, 룸메이트 3
    roomate_num=models.IntegerField(default=-1) # 구하는 룸메이트 수, 양도,기간 대여라면 0
    building_type=models.IntegerField(default=-1) # 아파트 1, 오피스텔 2, 빌라 3
    period=models.IntegerField(default=-1) # 하루 1, 월세 2, 전세 3
    cost=models.IntegerField(default=-1) # 만원 단위로, 2만원이라면 2
    university=models.IntegerField(default=-1)
    gender=models.IntegerField(default=-1) # 남자 1, 여자 2
    addr_gu=models.CharField(max_length=5)
    addr_dong=models.CharField(max_length=5)
    image1=models.ImageField(upload_to='images/')
    image2=models.ImageField(upload_to='images/')
    image3=models.ImageField(upload_to='images/')
    detail=models.TextField(default="")
    deposit=models.IntegerField(default=-1) # 보증금
    rooms=models.IntegerField(default=-1)

    def pGender(self):
        if self.gender==1:
            return "남"
        if self.gender==2:
            return "여"
    
    def pRentType(self):
        if self.rent_type==1:
            return "양도"
        if self.rent_type==2:
            return "대여"
        if self.rent_type==3:
            return "룸메이트"

    def pBuildingType(self):
        if self.building_type==1:
            return "아파트"
        if self.building_type==2:
            return "오피스텔"
        if self.building_type==3:
            return "빌라"

    def pPeriod(self):
        if self.period==1:
            return "하루 "
        if self.period==2:
            return "월 "
        if self.period==2:
            return "전세 "

    def pCost(self):
        if self.period==1:
            return str(self.cost)
        if self.period==2:
            return str(self.cost)+"/"+str(self.deposit)
        if self.period==3:
            return str(self.cost)

