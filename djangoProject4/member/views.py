from django.http import HttpResponse
from django.shortcuts import render, redirect
from member.models import Question, Test
# Create your views here.
import member.views


def start(req):
    return HttpResponse('<h3>시작페이지</h3>' +
                        '<a href=/member/>회원정보 사이트</a><br>' +
                        '<a href=/question/>질문정보 사이트</a><br>'
                        )


def index(req):
    return render(req, 'member/index.html')


def insert(req):
    return render(req, 'member/insert.html')


def insert2(req):
    # 1.입력한 정보 받아서
    data = req.POST  # POST로 넘어온 것 전부다 data로 받음
    print('서버에서 받은 데이터(views.py)>> ', data)
    print('name:', data['name'])
    print('tel:', data['tel'])
    print('addr:', data['addr'])
    # 2.db처리하고
    # 2-1. 객체 생성(import)
    one = Test(name=data['name'], tel=data['tel'], addr=data['addr'])
    # 2-2. 파이썬에 저장 save()
    one.save()
    # 3.결과를 알려주자.
    return render(req, 'member/insert2.html')


def delete(req):
    return render(req, 'member/delete.html')


def delete2(req):
    # 1.입력한 정보 받아서
    data = req.POST  # POST로 넘어온 것 전부다 data로 받음
    print('서버에서 받은 데이터(views.py)>> ', data)
    print('name:', data['id'])
    # 2.db처리하고
    # 2-1. 검색을 먼저 하고
    # get을 쓰면 검색 결과가 많아도 값 하나만  가져옴
    # filter을 사용하면 여러값을 지울 수 있다.(인덱스 지정 해줘야한다.)
    one = Test.objects.get(id=data['id'])
    # 2-2. 지워주세요
    one.delete()
    # 3.결과를 알려주자.
    return render(req, 'member/delete2.html')


def one(req):
    return render(req, 'member/one.html')


def one2(req):
    # 1.입력한 정보 받아서
    data = req.POST  # req파라메터에 POST로 넘어온 것 전부다 data로 받음
    print('서버에서 받은 데이터(views.py)>> ', data)
    print('id:', data['id'])
    # 2.db에서 값을 가져와보자.
    # get을 쓰면 검색 결과가 많아도 값 하나만  가져옴
    idValue = data['id']
    one = Test.objects.get(id=idValue)
    print('db검색한 결과', one)
    result = {'one': one,
              'test': 100}
    # 3.결과를 딕셔너리 형태로 템플릿으로 넘겨주자.
    # controller에서 template으로 값을 넘길때는
    # dictionary를 만들어 전달한다.
    return render(req, 'member/one2.html', result)


def one22(req, id):
    one = Test.objects.get(id=id)
    print('db검색한 결과', one)
    result = {'one': one,
              'test': 100}
    # 3.결과를 딕셔너리 형태로 템플릿으로 넘겨주자.
    # controller에서 template으로 값을 넘길때는
    # dictionary를 만들어 전달한다.
    return render(req, 'member/one2.html', context=result)


def up(req, id):  # get방식으로 받아온id 를 받아준다.
    # get(주소와 함께 전달되는 값은 컨트롤러의 함수안에
    #     같은 이름의 변수를 선언해주면 장고가 받아서 넣어준다.
    ##검색할 id를 받아와서
    print('전달받은 검색할 id는 ', id)
    ##db검색을 한후,
    one = Test.objects.get(id=id)
    print('db검색한 결과: ', one)
    context = {'one': one}
    ##db검색한 결과를 context로 전달
    # 결과를 딕셔너리 형태로 템플릿으로 넘겨주자.
    # controller에서 template으로 값을 넘길때는
    # dictionary를 만들어 전달한다.
    return render(req, 'member/up.html', context)


def up2(req):
    # 1. 전달되는 값 post방식으로 받고
    data = req.POST
    # 2. id를 가지고 검색 후,
    one = Test.objects.get(id=data['id'])
    print('수정할 데이터를 찍어보자.up2> ', one)
    # 3. update처리함.각 컬럼값을 one안에 넣어주고 save해주자.
    one.name = data['name']
    one.tel = data['tel']
    one.addr = data['addr']
    one.save()
    # 4. 결과를 알려줌

    # 5. 검색을 해서 확인해보자. 해당주소로 바로이동해보도록 하자.
    return redirect('/member/one22/' + data['id'])


# 회원전체검색
def all(req):
    all = Test.objects.all()
    context = {'all': all}
    return render(req, 'member/all.html', context)


# 로그인처리
def login(req):
    return render(req, 'member/login.html')


def login2(req):
    one = Test.objects.get(id=req.POST['id'])
    print('db검색한 결과: ', one)
    if one != None:
        result = '로그인 성공'
        req.session['logid'] = req.POST['id']
    else:
        result = '로그인 실패'
    print(result)
    # controller에서 template으로 값을 넘길때는
    # dictionary를 만들어 전달한다.
    return redirect('/member/')  # redirect는 get방식으로만 가능.


###question curd만들기
def qindex(req):
    return render(req, 'member/qindex.html')


def write(req):
    return render(req, 'member/write.html')


def write2(req):
    # 1.입력한 정보 받아서
    data = req.POST  # POST로 넘어온 것 전부다 data로 받음
    print('서버에서 받은 데이터(views.py)>> ', data)
    print('qtext:', data['question_text'])
    print('qwrite:', data['question_writer'])
    # 2.db처리하고
    # 2-1. 객체 생성(import)
    one = Question(question_text=data['question_text'], question_writer=data['question_writer'])
    # 2-2. 파이썬에 저장 save()
    one.save()
    # 3.결과를 알려주자.
    return render(req, 'member/write2.html')


def qdelete(req):
    return render(req, 'member/qdelete.html')


def qdelete2(req):
    # 1.입력한 정보 받아서
    data = req.POST  # POST로 넘어온 것 전부다 data로 받음
    print('서버에서 받은 데이터(views.py)>> ', data)
    print('question_writer:', data['question_writer'])
    # 2.db처리하고
    # 2-1. 검색을 먼저 하고
    # get을 쓰면 검색 결과가 많아도 값 하나만  가져옴
    # filter을 사용하면 여러값을 지울 수 있다.(인덱스 지정 해줘야한다.)
    one = Question.objects.get(question_writer=data['question_writer'])
    # 2-2. 지워주세요
    one.delete()
    # 3.결과를 알려주자.
    return render(req, 'member/qdelete2.html')


def qone(req):
    return render(req, 'member/qone.html')


def qone2(req):
    # 1.입력한 정보 받아서
    data = req.POST  # req파라메터에 POST로 넘어온 것 전부다 data로 받음
    print('서버에서 받은 데이터(views.py)>> ', data)
    print('id:', data['question_writer'])
    # 2.db에서 값을 가져와보자.
    # get을 쓰면 검색 결과가 많아도 값 하나만  가져옴
    writerValue = data['question_writer']
    one = Question.objects.get(question_writer=writerValue)
    print('db검색한 결과', one)
    result = {'one': one,
              'test': 100}
    # 3.결과를 딕셔너리 형태로 템플릿으로 넘겨주자.
    # controller에서 template으로 값을 넘길때는
    # dictionary를 만들어 전달한다.
    return render(req, 'member/qone2.html', result)


def qone22(req, question_writer):
    one = Question.objects.get(question_writer=question_writer)
    print('db검색한 결과', one)
    result = {'one': one,
              'test': 100}
    # 3.결과를 딕셔너리 형태로 템플릿으로 넘겨주자.
    # controller에서 template으로 값을 넘길때는
    # dictionary를 만들어 전달한다.
    return render(req, 'member/qone2.html', context=result)


def qup(req, question_writer):  # get방식으로 받아온id 를 받아준다.
    # get(주소와 함께 전달되는 값은 컨트롤러의 함수안에
    #     같은 이름의 변수를 선언해주면 장고가 받아서 넣어준다.
    ##검색할 id를 받아와서
    ##db검색을 한후,
    one = Question.objects.get(question_writer=question_writer)
    print('db검색한 결과: ', one)
    context = {'one': one}
    ##db검색한 결과를 context로 전달
    # 결과를 딕셔너리 형태로 템플릿으로 넘겨주자.
    # controller에서 template으로 값을 넘길때는
    # dictionary를 만들어 전달한다.
    return render(req, 'member/qup.html', context)


def qup2(req):
    # 1. 전달되는 값 post방식으로 받고
    data = req.POST
    # 2. id를 가지고 검색 후,
    one = Question.objects.get(question_writer=data['question_writer'])
    print('수정할 데이터를 찍어보자.up2> ', one)
    # 3. update처리함.각 컬럼값을 one안에 넣어주고 save해주자.
    one.question_text = data['question_text']
    one.question_writer = data['question_writer']
    one.save()
    # 4. 결과를 알려줌
    # 5. 검색을 해서 확인해보자. 해당주소로 바로이동해보도록 하자.
    return redirect('/question/qone22/' + data['question_writer'])

# #글전체검색
def qall(req):#함수이름 qall은 urls.py와 맞춰주면 된다.
    #아래 딕셔너리qall은 html에서 출력해야함. {{ qall }}을 html에 적어줘야한다.
    qall = Question.objects.all()
    context = {'qall': qall}#왼쪽 qall이 딕셔너리의 key 이고, 오른쪽 qall이 value이다.
    print('qall은 >>> ', qall)#value는 db의 행 N 줄. 전체 글이 나온다.
    return render(req, 'member/qall.html',context)
