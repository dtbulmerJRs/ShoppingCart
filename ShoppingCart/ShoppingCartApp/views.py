from django.http import HttpResponse, HttpResponseRedirect
from ShoppingCartApp.forms import ShoppingCartUserForm
from django.contrib.auth.models import *
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.context_processors import csrf

def index(request):
    some_string = "Hello!"
    return HttpResponse(some_string)

def register_user(request):
    if request.method == 'POST':
        form = ShoppingCartUserForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = form.save()
            group = Group.objects.get(name=cleaned_data['user_type'])
            group.user_set.add(user)
            return HttpResponseRedirect('/ShoppingCartApp/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = ShoppingCartUserForm()
    #print args
    return render_to_response('register.html',args)


def register_success(request):
    return render_to_response('register_success.html')