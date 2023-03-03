from django.contrib.auth import login
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from userApp.form import RegisterForm
from django.urls import reverse

def register(request: HttpRequest):
    #POST
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterForm()

    #GET
    context = {'form':form}
    return render(request, 'userApp/register.html', context)
