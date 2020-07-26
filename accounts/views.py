from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import redirect,render,resolve_url
from .forms import SignupForm
# from .forms import SignupForm     # Form을 재정의 할때 사용

# 함수 기반 뷰
'''
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # DB에 회원정보가 들어간 시점

            # 로그인 처리 구현
            # form_valid() <= is.valid()가 참일때 호출되는 함수
            auth_login(request, user)

            # return redirect(settings.LOGIN_URL)
            return redirect('profile') # 로그인 후에 profile 창으로 이동

    else:
        form = UserCreationForm()    
    return render(request, 'accounts/signup.html',{
        'form':form,
    })
'''

# 함수 기반 재정의 뷰
'''
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # DB에 회원정보가 들어간 시점
            
            # 로그인 처리 구현
            # form_valid() <= is.valid()가 참일때 호출되는 함수
            auth_login(request, user)

            # return redirect(settings.LOGIN_URL)
            return redirect('profile') # 로그인 후에 profile 창으로 이동
    else:
        form = SignupForm()    
    return render(request, 'accounts/signup.html',{
        'form':form,
    })
'''

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return resolve_url('profile')

    def form_valid(self,form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())  # redirect('profile') 도 가능

# 클래스 기반 뷰 
signup = SignupView.as_view()   # CreateView를 SignupView에서 상속받아 위에서 재정의


@login_required
def profile(request):
    return render(request,'accounts/profile.html')
