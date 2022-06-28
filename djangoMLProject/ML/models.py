from django.db import models

# Create your models here.

class Tag(models.Model):
    #id는 default로 만들어진다.
    #평일휴일 , 요일, 시간대, 성별, 연령대, 건수합계, 네이버 태그 클릭량
    week1 = models.CharField(max_length=10)
    week2 = models.CharField(max_length=10)
    hour = models.IntegerField()
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    size = models.IntegerField()
    tag_click = models.IntegerField()

    def __str__(self):
        return str(self.id) + "," + \
               str(self.week1) + "," + \
               str(self.week2) + "," + \
               str(self.hour) + "," + \
               str(self.gender) + "," + \
               str(self.age) + "," + \
               str(self.size) + "," + \
               str(self.tag_click)
