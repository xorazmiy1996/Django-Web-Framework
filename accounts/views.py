
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import UserProfileForm


# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Tizimga kirish yoki boshqa amallar
            return redirect("foodie_app:index")

    else:
        form = UserCreationForm()

    return render(request, "accounts/register.html", {"form": form})

def edit_user_profile(request):
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("foodie_app:index")
    else:
        form = UserProfileForm(instance=request.user.profile)
    return render(request, "accounts/edit_profile.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('foodie_app:index')  # O'zgaritiring
            else:
                # Foydalanuvchi topilmadi
                return render(request, 'accounts/login.html', {'error': 'Foydalanuvchi ismi yoki parol noto\'g\'ri.'})
        else:
            return render(request, 'accounts/login.html',
                          {'error': 'Iltimos, foydalanuvchi ismini va parolni kiriting.'})

    return render(request, 'accounts/login.html')





