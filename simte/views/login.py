from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user: #if we have a user, we can continue
            if user.is_active: #user account could be deactivated
                login(request, user)
                return httpResponseRedirect('/inspection_list/')
            else:
                return HttpResponse('Sua conta foi desativada')
        else:
            return HttpResponse('Usuario e senha nao condizem')

    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/inspection_list/')
    return render(request,'simte/login.html')

