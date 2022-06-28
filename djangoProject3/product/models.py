from django.db import models
#장고는 sql문을 몰라도 테이블을 생성할 수 있도록 제공하고있다.
#ORM을 models.py에 정의해주세요.
#테이블하나당 클래스 하나로 정의
#vo역할
class product(models.Model):
    no = models.IntegerField(100)
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=500)
    writer = models.CharField(max_length=500)

    def __str__(self):
        return str(self.no) + "," + \
         self.title + "," + \
         self.content + "," + \
         self.writer