from django.shortcuts import render
from registration.models import UserProfileInfo
from registration.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register(request):
    registered = False
    if request.method == "POST":
        form_user = UserForm(data = request.POST)
        form_por = UserProfileInfoForm(data = request.POST)
        if form_user.is_valid() and form_por.is_valid():
            user = form_user.save()
            user.set_password(user.password)
            user.save()
            profile = form_por.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(form_user.errors, form_por.errors)
    else:
        form_user = UserForm()
        form_por = UserProfileInfoForm()
    return render(request, 'registration/registration.html', {'user_form':form_user,\
        'profile_form': form_por, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password )
        if user:
            if user.is_active:
                login(request, user)
                result = 'Chào bạn ' + username
                return render(request, 'catalog/home.html', {'result': result})
        else:
            result = "Username và password không hợp lệ"
            return render(request, 'catalog/home.html', {'result': result}) 
    else:
        return render(request, 'registration/login.html')

@login_required
def user_logout(request):
    logout(request)
    result = "Bạn đã đăng xuất. Vui lòng chọn 'Đăng nhập'"
    return render(request, "catalog/home.html", {"result":result})