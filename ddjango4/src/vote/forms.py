'''
Form : django 에서 HTML 코드에 들어갈 <input> 태그를 파이썬 코드 형태로 관리할 수
있도록 제공하는 기능

Form 은 모델클래스를 기반으로 입력공간을 생성할 수도 있고, 커스텀 입력 양식을 생성할 
수도 있음.

ModelForm : 모델클래스와 연동된 폼을 만들떄 상속받는 클래스
Form : 커스텀 입력양식으로만 폼을 만들때 상속받는 클래스

장점
Model 클래스에 변동사항을 자동으로 Form 클래스가 인지해서 사용자가 입력할수 있는
공간을 변경해줌. 디자이너가 직접 입력양식을 만들지 않아도 됨

'''

from django.forms.models import ModelForm
from vote.models import Question,Choise

#Question 모델클래스와 연동된 모델 폼클래스 정의
#클라이언트가 Question 객체를 추가/수정 할 때 사용
class QuestionForm(ModelForm):
    #Meta 클래스: 연동하고자하는 모델클래스에 대한 정보를 정의하는 클래스
    #밑에 전부다 무조건 저글자로 사용해야한다. 
    class Meta:
        #model,fields,exclude,widgets
        #model : 연동할 모델클래스 이름을 저장하는 변수
        model =Question
        #fields : 사용자가 입력할 수 있는 <input> 태그를 생성할 때,
        #모델클래스에 정의된 변수들 중 어떤변수를 클라이언트에게 제공할 것인지 지정
        #exclude : 모델클래스에 정의된 변수중 어던 변수를 제외하고 클라이언트 에게 제공할 것인지 지정
        #변수이름은 문자열 형태로, 저장하는 타입은 리스트 형태로
        #fields 나 exclude 변수 중 한개만 사용
        fields = ['name']
        #exclude = ['pub_date']
#choice 모델클래스와 연동된 모델폼클래스 정의
#클라이언트가 choice 객체를 추가 /수정할 때 사용
class ChoiseForm(ModelForm):
    class Meta:
        model = Choise
        fields=['q','name']
        #exclude = ['votes']




