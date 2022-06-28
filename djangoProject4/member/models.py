from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=500)
    question_writer = models.CharField(max_length=500)


    def __str__(self):
        return str(self.id) + "," + \
               self.question_text + "," + \
               self.question_writer


class Test(models.Model):
    # id는 default로 만들어진다.
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    addr = models.CharField(max_length=200)

    # python override
    # 내장함수를 오버라이드
    def __str__(self):
        # class를 나타내는 키워드인 self를 꼭 써줘야한다. self.name 이런식으로 접근하기때문에..
        # 자바에서 this역할
        return str(self.id) + "," + self.name + "," + self.tel + "," + self.addr
