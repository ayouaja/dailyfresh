from django.shortcuts import render, redirect
import re
from user.models import User
from django.core.urlresolvers import reverse

# Create your views here.

def register(request):
    return render(request, 'register.html')


def register_handle(request):
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')
    # print(username)
    if not all([username, password, email]):
        return render(request, 'register.html', {'errmsg':'shujuerror'})

    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'register.html', {'errmsg':'emailerror'})

    if not allow == 'on':
        return render(request, 'register.html', {'errmsg':'allowerror'})

    # user = User()
    # user.email = email
    # user.password = password
    # user.username = username
    # user.save()
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None

    if user:
        return render(request, 'register.html', {'errmsg': 'yonghumingyijchuunz'})


    user = User.objects.create_user(username,email,password)
    user.is_active = 0
    user.save()

    return redirect(reverse('goods:index'))


