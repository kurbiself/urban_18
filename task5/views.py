from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


def sign_up_by_django(request):
    users = ['Tanos', 'Duolingo', 'monster']
    info = {}
    error = []
    template_name = 'fifth_task/registration_page.html'
    form = UserRegister(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        age = form.cleaned_data['age']
        info = {
            'username': username,
            'password': password,
            'repeat_password': repeat_password,
            'age': age,
            'form': form
        }
        is_passwords_correct = bool(password == repeat_password)
        is_user_found = bool(username in users)
        is_age_correct = bool(int(age) >= 18)
        if (not is_user_found and
                is_passwords_correct and
                is_age_correct):
            return render(request, template_name, info)
        if is_user_found:
            error.append('Пользователь уже существует')
            info.update({'error': error})
            return render(request, template_name, info)
        if not is_passwords_correct:
            error.append('Пароли не совпадают')
            info.update({'error': error})
            return render(request, template_name, info)
        if not is_age_correct:
            error.append('Вы должны быть старше 18')
            info.update({'error': error})
            return render(request, template_name, info)
    else:
        form = UserRegister()
    return render(request, template_name, info)


def sign_up_by_html(request):
    users = ['Tanos', 'Duolingo', 'monster']
    info = {}
    template_name = 'fifth_task/registration_page.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        error = []
        info = {
            'username': username,
            'password': password,
            'repeat_password': repeat_password,
            'age': age
        }
        info = {
            'username': username,
            'password': password,
            'repeat_password': repeat_password,
            'age': age,
        }
        is_passwords_correct = bool(password == repeat_password)
        is_user_found = bool(username in users)
        is_age_correct = bool(int(age) >= 18)
        if (not is_user_found and
                is_passwords_correct and
                is_age_correct):
            return render(request, template_name, info)
        if is_user_found:
            error.append('Пользователь уже существует')
            info.update({'error': error})
            return render(request, template_name, info)
        if not is_passwords_correct:
            error.append('Пароли не совпадают')
            info.update({'error': error})
            return render(request, template_name, info)
        if not is_age_correct:
            error.append('Вы должны быть старше 18')
            info.update({'error': error})
            return render(request, template_name, info)
    return render(request, template_name)
