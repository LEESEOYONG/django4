from django.db import models

'''
models.py : 해당 어플리케이션에서 데이터베이스에 저장할 데이터 형태를 정의하는곳
자동 임포트된 models 라는 파이썬파일에는 모델클래스를 정의할때 필요한 클래스,함수가 정의됨

model 클래스 개발 및 뭽프로젝트 반영 순서
1) 모델클래스를 정의하면서 models.Model 클래스를 상속
2) 모델클래스에서 저장할 값의 타입과 이름을 클래스변수로 지정
3) 정의된 모델클래스를 migration 파일로 변환  -> 바로 해석이 안되서 db에 저장을해줘야한다
  project-Django-Make migration
  project-
4) migration 파일을 웹프로젝트에 반영(migration)

models.XXXXField : 클래스변수에 어떤 형태의 값을 저장하도록 정의할지 객체를 생성할때
사용하는 클래스
models.CharField : 글자수제한이 있는 문자열을 저장할때 사용하는 클래스
필수 매개변수로 max_length 라는 최대글자수 길이를 입력해야함
models.URLFiled : 인터넷(URL) 을 저장할 떄 사용하는 클래스 
매개변수가 따로 없어서 () 안에는 입력할 필요 없다
'''
#북마크 모델클래스
#즐겨찾기 이름(문자열), 클릭시 이동할 사이트주소(URL)

class Bookmark(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    #__str__: 객체를 화면에 출력할때 어떤형태로 띄울지 정의된 함수
    def __str__(self):
        return self.name



# Create your models here.
