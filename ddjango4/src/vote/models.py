from django.db import models

# Create your models here.

#Question 모델클래스
#설문제목, 설문 생성일
class Question(models.Model):
    name = models.CharField(max_length=200)
    #models.DateField : 난짜 데이터를 저장할 수 있는 공간
    #models.DateTimeField : 날짜 + 시간 데이터를 저장할 수 있는 공간
    pub_date = models.DateField()
    def __str__(self):
        return self.name
    
#Choice 모델클래스
#답변 항목 내용, 투표수 어떤 Question 과 연결되어있는지?(외래키)
class Choise(models.Model):
    name = models.CharField(max_length =50)
    #models.IntegerField : 정수값 데이터를 저장할 수 있는 공간
    #default : 모든 Field 클래스에 존재하는 매개변수로, 객체 생성시 기본값설정을 할수 있음
    votes = models.IntegerField(default=0)
    #Question 모델클래스와 1:n 관계를 가지는 설정
    #Choice 객체가 연결한 Question 객체가 삭제가 되면, 자신도 삭제되도록 설정
    #ex) 글 삭제하면 그글에 작성된 댓글이 같이 삭제됨
    q = models.ForeignKey(Question,on_delete=models.CASCADE)  #하나의 Question 이 여러개의  Choice 객체에 연결됨
    #q는 Question의 id값과 연결을한다 그리고 Choise.q.pub_date같은걸 꺼내서 사용가능!!
    def __str__(self):
        #self.q.name : 현재 Choice 객체가 연결한 Question 객체의 name 변수값 접근
        return self.q.name +'/' + self.name
'''
models.ForeignKey : 다른 모델클래스의 객체와 해당 모델클래스의 객체가 연결 관계를 가지는 저장공간
ForeignKey(연결할 모델클래스 ,on_delete = 연결객체 삭제시, 삭제방식)
현재 choice 모델클래스의 q변수는 연결한 Question 객체를 의미함
 -> Choice 객체.q.name 이나 q.pub_date로 연결한 Question 객체의 변수값을 사용할 수 있음
 
 매개변수 on_delete : 연결된 모델클래스의 객체가 삭제될 때 연결한 객체들을 어덯게 처리할지 지정하는 변수
 models.CASCADE : 연결된 모델클래스의 객체가 삭제될때, 같이삭제
 models.PROTECT : 연결된 모델클래스가 삭제되지 않도록 막아줌
 models.SET_NULL : 연결된 객체가 삭제되면 아무것도 연결하지 않은 상태유지
 models.SET(연결할객체) : 연결된 객체가 삭제되면 매개변수로 넣은 객체와 연결
 models.SET_DEFAULT : 연결된 객체가 삭제되면 기본값 객체와 연결
 
'''
    
    
    
    