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

            next_url = request.GET.get('next') or 'profile'     # 값이 없으면 값은 'profile'

            # return redirect(settings.LOGIN_URL)
            # return redirect('profile') # 로그인 후에 profile 창으로 이동
            return redirect(next_url)
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
        next_url = self.request.GET.get('next') or 'profile'
        # return resolve_url('profile')   # 리턴값을 redirect로 주면 HttpResponse가 반환되기때문에 url을 반환하는 resolve_url 사용 
        return resolve_url(next_url)

    def form_valid(self,form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())  # redirect('profile') 도 가능

# 클래스 기반 뷰 
signup = SignupView.as_view()   # CreateView를 SignupView에서 상속받아 위에서 재정의


@login_required
def profile(request):
    return render(request,'accounts/profile.html')
