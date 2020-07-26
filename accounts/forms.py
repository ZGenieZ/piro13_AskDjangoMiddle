from django.contrib.auth.forms import UserCreationForm

# Form을 재정의 하고 싶을때 (id,pwd는 이미 상속받아서 있음)
class SignupForm(UserCreationForm):
    pass