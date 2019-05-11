'''
Created on 2019. 4. 21.

@author: 405-6
'''
'''
어플리케이션별로 별도의 URL conf를 만들수있음
단, app_name와 urlpatterns 변수를 정의해야함(이름이 틀리면 URL Conf 가 설정되지않음)
app_name : 이파일에 정의한 URL 들의 그룹이름(문자열)
urlpatterns : path 함수를 이용해 뷰함수를 등록하는 변수(리스트)
만들어진 urls.py 를 프로젝트의 폴더의 urls.py에 알려줘야함
'''
from django.urls import path 
from vote.views import *
app_name = 'vote'
#기본 도메인 주소: 127.0.0.1:8000/vote
urlpatterns = [
    #127.0.0.1:8000/vote/ 요청이 들어오면 index 함수 호출
    path('',index),
    #127.0.0.1:8000/vote/숫자값 요청이 들어오면 detail 함수 호출 숫자값은 q_id 매개변수에 값으로 사용됨
    path('<int:q_id>/',detail),
    #127.0.0.1:8000/vote/vote  -> vote함수호출
    path('vote/',vote),
    #127.0.0.1:8000/vote/result/숫자값  -> result함수호출
    #숫자값은 q_id매개변수에 사용
    path('result/<int:q_id>/',result),
    #127.0.0.1:8000 /vote/qr/ -> qregiste 함수호출
    #파이썬코드나 HTML에서 vote:qr 별칭으로 URL을 찾을 수 있음
    path('qr/',qregiste,name='qr'),
     #127.0.0.1:8000 /vote/cr/ -> cregiste 함수호출
     #파이썬 코드나 HTML에서 cote:cr 별칭으로 URL을 찾을수 있음
    path('cr/',cregiste,name='cr'),
    path('<int:q_id>/change/',qupdate,name='qu'),
    path('<int:q_id>/delete/',qdelete,name='qd'),
    path('<int:c_id>/cdelete/',cdelete,name='cd'),
    path('<int:c_id>/cchange/',cupdate,name='cu')
    

    ]