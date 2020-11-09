from django.shortcuts import render
from .models import Board
from .models import Member
from datetime import datetime
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.


def main(request):
    return render(request, 'home/main.html')

class Login(View):
    def get(self, request):
        return render(request, 'home/login.html')

    def post(self, request):
        userid = request.POST.get('userid')
        userpw = request.POST.get('userpw')

        querySet = Member.objects.filter(userid=userid, userpw=userpw)

        if len(querySet) == 1:
            login = querySet[0]
            request.session['login_userid'] = login.userid
            request.session['login_username'] = login.username
            return HttpResponseRedirect('/')      
        else:
            js = '''<script>
                    alert('아이디 또는 비밀번호가 잘 못 되었습니다.');
                    history.go(-1);
                </script>'''
            return HttpResponse(js)

def logout(request):
    del request.session['login_userid']
    del request.session['login_username']
    return HttpResponseRedirect('/')

class Signup(View):
    def get(self, request):
        return render(request, 'home/signup.html')

    def post(self, request):
        userid = request.POST.get('userid')
        userpw = request.POST.get('userpw')
        username = request.POST.get('name')
        birth = request.POST.get('birth')
        phonenum = request.POST.get('phonenum')

        duplicate = Member.objects.filter(userid=userid)
        if len(duplicate) != 0:
            js = ''' <script>
                alert('이미 사용중인 ID입니다');
                history.go(-1);
            </script>'''
            return HttpResponse(js)
        
        newbie = Member()

        newbie.userid = userid
        newbie.userpw = userpw
        newbie.username = username
        newbie.birth = birth
        newbie.phonenum = phonenum

        newbie.save()
        
        return HttpResponseRedirect('/login/')

def index(request):
    querySet = Board.objects.filter(isDeleted=False)
    context = {
        'boardList' : querySet,
    }
    return render(request, 'home/index.html', context)

def notice(request, idx):
    query = Board.objects.get(idx=idx)
    context = {
        'board' : query,
    }
    return render(request, 'home/notice.html', context)

class Write(View):
    def get(self, request):
        return render(request, 'home/write.html')

    def post(self, request):
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        content = request.POST.get('content')

        now = datetime.today()

        write = Board()
        write.title = title
        write.writer = writer
        write.content = content
        write.datetime = now
        write.save()

        last = Board.objects.last()
        url = '/board/notice/' + str(last.idx) +'/'
        return HttpResponseRedirect(url)

def delete(request, idx):
    target = Board.objects.get(idx=idx)
    target.delete()
    return HttpResponseRedirect('/')

class Modify(View):
    def get(self, request, idx):
        query = Board.objects.get(idx=idx)
        context = {
            'board' : query,
        }
        return render(request, 'home/modify.html', context)
    
    def post(self, request, idx):
        query  = Board.objects.get(idx=idx)

def video(request):
    user = request.session['login_userid']

    if user == 0:
        return HttpResponseRedirect('login/')
    else:
        return render(request, 'home/video.html')
        