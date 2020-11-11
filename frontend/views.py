from django.shortcuts import render, redirect
from .forms import MainForm
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    if request.method == "POST":
        form = MainForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            mail = send_mail(f'Заявка с сайта SinklitHome', f'Добрый день!\nМеня заинтересовало ваше предложение.\nМои данные:\nИмя: {name}\nТелефон: {phone}\nE-mail: {email}\n', 'sinklit.home@gmail.com', ['viperovm@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('thanks')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = MainForm()
    context = {
        'form': form,
    }

    return render(request, 'frontend/index.html', context)


def thanks(request):
    return render(request, 'frontend/thanks.html')
