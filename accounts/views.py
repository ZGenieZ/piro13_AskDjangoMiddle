from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import redirect,render
# from .forms import SignupForm     Form을 재정의 할때 사용

# 함수 기반 뷰
'''
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
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
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()    
    return render(request, 'accounts/signup.html',{
        'form':form,
    })
'''

# 클래스 기반 뷰 
signup = CreateView.as_view(model=User,
form_class=UserCreationForm,        # 재정의 할때는 form_class = SignupForm으로 지정
success_url=settings.LOGIN_URL,
template_name='accounts/signup.html')


@login_required
def profile(request):
    return render(request,'accounts/profile.html')
